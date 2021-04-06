import os
import sys
import traceback
import json
import glob
import re
import base64
import markdown
from PIL import Image
from _operator import is_


eob_base_url = 'https://apps.sentinel-hub.com/eo-browser/?'
max_theme_image_width = 240
max_theme_image_height = 200
max_pin_image_width = 800
max_pin_image_height = 800


def log(message, do_clear=False):
    print(message)
    file = open('_build/build.log', 'a')
    if do_clear:
        file.seek(0, 0)
        file.truncate()
    file.write(message + "\n")
    file.close()

def resize_image(src_image_path, dest_image_path, max_width, max_height, do_crop):
    # resize and crop the images, that are too big 
    log('Checking image "' + src_image_path + '"')
    try:
        image = Image.open(src_image_path)
        width, height = image.size
        
        if (width > max_width) or (height > max_height):
            log('Resizing image "' + src_image_path + '" from ' + str(width) + ' x ' + str(height))
            is_wide = width * max_height > height * max_width
            small_width = int(width * max_height / height) if not is_wide else max_width
            small_height = int(height * max_width / width) if is_wide else max_height
            small_horiz_border = (small_width - max_width) / 2
            small_vert_border = (small_height - max_height) / 2
            
            image.thumbnail((small_width, small_height), Image.ANTIALIAS)
            if do_crop:
                image = image.crop((small_horiz_border, small_vert_border, small_width - small_horiz_border, small_height - small_vert_border))
            image.save(dest_image_path, 'jpeg', quality=95)
            log('Resized image "' + src_image_path + '" to ' + str(small_width) + ' x ' + str(small_height))
    except Exception as e:
        log('ERROR resizing image "' + src_image_path + '": ' + str(e))


log("Started the build process", True)

texts_per_theme = {}
        
with open('_build/container.html', 'r', encoding='utf-8') as html_container_file, \
    open('_build/pin.html', 'r', encoding='utf-8') as html_pin_file, \
    open('_build/theme.html', 'r', encoding='utf-8') as html_theme_file, \
    open('themes.json', 'r', encoding='utf-8') as themes_json_file:
    
    html_container_template = html_container_file.read()
    pin_html_template = html_pin_file.read()
    theme_html_template = html_theme_file.read()
    
    theme_html_content = '\t\t\t\t\t<h2>Themes</h2>\n' + \
                    '\t\t\t\t\t<div id="themes">\n'
    
    themes = json.load(themes_json_file)
    
    for theme in themes:
        theme_name = theme['name']
        theme_path = re.sub('[^a-zA-Z0-9]', '_', theme_name)
        
        theme_html_content += theme_html_template \
            .replace('{theme_path}', theme_path) \
            .replace('{theme_name}', theme_name)
        
        theme_img_path = '_themeimgs/' + theme_path + '.jpg';
        resize_image(theme_img_path, theme_img_path, max_theme_image_width, max_theme_image_height, True)
    
        pin_auto_group_serial = 0
        pins_per_group = {}
        
        for pins_json_file_name in glob.glob(os.path.join(theme_path, '*.json')):
            try:
                with open(pins_json_file_name, 'r', encoding='utf-8') as pins_json_file:
                    log('Processing JSON file "' + pins_json_file_name + '"')
                    pins = json.load(pins_json_file)
                    for pin in pins:
                        pin_id = pin.get('_id') or ''
                        is_location = 'lat' in pin and 'lng' in pin
                        is_eob = is_location and 'zoom' in pin
                        group = pin.get('group')
                        download_url = pin.get('highResImageUrl')
                        
                        pin_lib_extra = pin.get('extra')
                        thumbnail_path = pin_lib_extra.get('thumbnailPath') if pin_lib_extra else None
                        if thumbnail_path is None and pin_id:
                            thumbnail_path = 'fig/' + pin_id + '.jpg'
                            
                        resize_image(theme_path + '/' + thumbnail_path, theme_path + '/' + thumbnail_path, max_pin_image_width, max_pin_image_height, False)
                        
                        # generate EOB URL
                        eob_url = eob_base_url
                        for pin_key in pin.keys():
                            if pin_key not in ('title', 'description', 'group', 'highResImageUrl', 'extra'):
                                if pin_key == 'evalscript':
                                    eob_url += '&' + pin_key + '=' + base64.b64encode(bytes(str(pin.get(pin_key)), 'utf-8')).decode("utf-8")
                                else:
                                    eob_url += '&' + pin_key + '=' + str(pin.get(pin_key))
                                    
                        
                        # if group not specified, use the JSON "_id" field, otherwise autogenerate the groupID
                        if not group:
                            if pin_id:
                                group = '_$' + pin_id
                            else:
                                group = '_$' + str(pin_auto_group_serial)
                                pin_auto_group_serial += 1
                        
                        # get the group for this pin
                        pins_in_group = pins_per_group.get(group)
                        if not pins_in_group:
                            pins_in_group = []
                            pins_per_group[group] = pins_in_group
                        
                        # add current pin data to the group
                        pin_data = { \
                            'id': pin_id, \
                            'group': group, \
                            'is_location': is_location, \
                            'is_eob': is_eob, \
                            'title': pin.get('title') or '', \
                            'date': (pin.get('fromTime') or '')[:10], \
                            'type': pin.get('datasetId') or '', \
                            'thumbnail_path': thumbnail_path if thumbnail_path else '', \
                            'world_pos_x': str(int((pin['lng'] + 180) * 300 / 360)) if is_location else '0', \
                            'world_pos_y': str(int((-pin['lat'] + 90) * 150 / 180)) if is_location else '0', \
                            'eob_url': eob_url, \
                            'download_url': download_url if download_url else '', \
                            'description': markdown.markdown(pin['description']), \
                            'visible': 'true' \
                        }
                        pins_in_group.append(pin_data)    
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)               
        
        pin_html_content = \
            '\t\t\t\t\t<div>\n' + \
            '\t\t\t\t\t\t<a href="' + os.path.basename(pins_json_file_name) + '" class="right" target="_blank" download="' + os.path.basename(pins_json_file_name) + '">\n' + \
            '\t\t\t\t\t\t\t<img src="{layout_dir}/export.svg" title="Export pins to JSON file" />\n' + \
            '\t\t\t\t\t\t</a>\n' + \
            '\t\t\t\t\t\t<h2>Pins: ' + theme_name + '</h2>\n' + \
            '\t\t\t\t\t</div>\n'
        
        pin_javascript = '\t\t\tvar groups = [];\n'

        # put the first pin of each group into the HTML and append all pins to pin_javascript
        for group in pins_per_group:
            pins_in_group = pins_per_group[group]
            
            html_pager = ''
            if len(pins_in_group) > 1:
                for i in range(0, len(pins_in_group)):
                    pager_image = 'pager_current' if i == 0 else 'pager_other'
                    html_pager += '<img src="{layout_dir}/' + pager_image + '.png" id="' + group + '_pin' + str(i) + '" />'
            
            pin_javascript += "\t\t\tgroups['" + group +"'] = {\n\t\t\t\t'pins':[\n"
            for pin in pins_in_group:
                pin_javascript += '\t\t\t\t\t{'
                for pin_field in pin:
                    if not pin_field == 'group':
                        pin_javascript += "'" + pin_field + "': '" + str(pin[pin_field]).replace("'", "\\'") + "', "
                pin_javascript += '},\n'
            pin_javascript += '\t\t\t\t]\n\t\t\t};\n'
            
            pin = pins_in_group[0]
            
            pin_html_content += pin_html_template \
                .replace('{pager}', html_pager) \
                .replace('{group}', pin['group']) \
                .replace('{title}', pin['title']) \
                .replace('{date}', pin['date']) \
                .replace('{type}', pin['type']) \
                .replace('{thumbnail_path}', pin['thumbnail_path'] if pin['thumbnail_path'] else '') \
                .replace('{world_pos_x}', pin['world_pos_x']) \
                .replace('{world_pos_y}', pin['world_pos_y']) \
                .replace('{world_pos_display}', 'block' if pin['is_location'] else 'none') \
                .replace('{eob_url}', pin['eob_url']) \
                .replace('{eob_display}', 'block' if pin['is_eob'] else 'none') \
                .replace('{download_url}', pin['download_url']) \
                .replace('{download_display}', 'block' if pin['download_url'] else 'none') \
                .replace('{description}', pin['description']) \
                .replace('{arrow_right_display}', 'block' if len(pins_in_group) > 1 else 'none')
                
            texts_in_theme = texts_per_theme.get(theme_path)
            if texts_in_theme == None:
                texts_in_theme = ""
            
            texts_in_theme += pin['title'] + " " + pin['description'] + " "
            texts_per_theme[theme_path] = texts_in_theme
            
        pin_html_content += '\t\t\t\t\t</div>\n'
        
        html = html_container_template.replace('{content}', pin_html_content)
        html = html.replace('{script}', pin_javascript)
        html = html.replace('{layout_dir}', '../_layout')
        html = html.replace('{github_repo_url}', sys.argv[1] if len(sys.argv) > 1 else 'https://www.github.com')

        output_html_file = open(os.path.join(theme_path, 'index.html'), 'w', encoding='utf-8')
        output_html_file.write(html)
        output_html_file.close() 


    theme_html_content += '\t\t\t\t\t</div>\n'
    
    theme_javascript = '\t\t\tvar texts = {};\n'
    for theme_path in texts_per_theme:
        theme_javascript += '\t\t\ttexts["' + theme_path + '"] = "' + texts_per_theme[theme_path].replace('"', '\\"').replace('\n', ' ').replace('\r', ' ') + '";\n'

    html = html_container_template.replace('{content}', theme_html_content)
    html = html.replace('{script}', theme_javascript)
    html = html.replace('{layout_dir}', '_layout')
    html = html.replace('{github_repo_url}', sys.argv[1] if len(sys.argv) > 1 else 'https://www.github.com')

    output_html_file = open('index.html', 'w', encoding='utf-8')
    output_html_file.write(html)
    output_html_file.close()
    
log("Finished building HTML files")
