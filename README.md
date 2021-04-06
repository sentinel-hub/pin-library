# Welcome to the Pin Library!

Welcome to the pin library, where anyone can browse and share satellite imagery of interesting locations and events of the Earth! There are several themes available, each holding many pins with images, descriptions and locations. We're hoping it can become a repository of remote sensing imagery, useful to any enthusiast, teacher, student or researcher. Don't forget to click on the EO Browser link for the pin that picks your interest, to explore it yourself! 

# Contribute to Pin Library

So you want to contribute to the wonderful world of satellite imagery? Just follow these instructions and you'll be started in no time!

The pins are exported from [EO Browser](https://apps.sentinel-hub.com/eo-browser/), where the satellite, date, location, visualization and description are all set, and finally uploaded to the Pin Library using git. 
If you're already familiar with how to configure and export the pins from EO Browser, jump to chapter 2 to learn how to import them to the Pin Library. 

When you commit your changes, our team will check your contribution in the shortest possible time. 

## 1. Export pins from EO Browser

The pins you will upload to Pin Library need to be configured in [EO Browser](https://apps.sentinel-hub.com/eo-browser/). If you don't know how to use EO Browser, check out [this tutorial](https://www.sentinel-hub.com/explore/eobrowser/).
 
### 1.1 Save your pins

Save your chosen location as pin, by clicking on the pin icon in the top menu on the left (as highlighted with a red rectancle). 

![save_pin](/_imgs/Readme/location.png =40px))

### 1.2. Edit your pins

Open the Pin tab on top (blue rectangle on the image above), to display all your pins. 

Edit each pin to change its name and add a description in [Markdown](https://learnxinyminutes.com/docs/markdown/). Click on the pen icon on the right to change the name, and confirm it by clicking the green check mark on the right. Then expand the arrows on bottom right, to open the description panel. Use Markdown to add a description and confirm it by clicking the green check mark on bottom right. 

![edit_pin](/_imgs/Readme/pin.png)

_**Mini Markdown guide:**_
- Headings are made using #. More #, smaller heading. For example: `# My Heading`, or `## My smaller heading`. Note that you need a space after the #. 
- Lists are made simply using - sign before each line. 
- To add links, write `[Text](www.url.com)`, which will display what you write in square brackets as clickable text with a link. 
- To add images, commit them to a folder and then access it with the following structure: `![ImageName](/imgFolder/imgName.png)`. Note that you can't do this in EO Browser directly. 
- Use ** before and after text to make it bold (e.g. `**Text**`) and use _ before and after text to make it italic (eg. `_Text_`)
- Use `<br/>` to make page breaks

You can delete the pins by clicking the trash can icon on the left, and you can organize the sequence of pins by clicking the drag icon (dots on the left) and rearranging them by dragging one on top of the other. The sequence of the pins in EO Browser will be the same as the sequence of pins in the Pin library, unless manually editing a JSON file. 

![delete_rearrange_pins](/_imgs/Readme/delete.png)

### 1.3. Export pins

Export pins from EO Browser by clicking the Export button. Note that all the pins in your list will be added - make sure to remove those you don't want included before hand (or remove them manually from the JSON file later).

![export_pins](/_imgs/Readme/export.png)

## 2. Contribute the Whole Theme

To contribute content to pin library, you need the following: 
- A JSON file with EO Browser pins (check section 2)
- Installed git and the Pin Library repository cloned (see [this guide](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners) to learn how to use git)
- Images for each pin downloaded

### 2.1. Examine the JSON file

The image below displays the structure of the JSON file exported from EO Browser. 
The red rectangle shows the structure of a single pin; each pin is included in curly brackets {}, which are all a part of a large array ([]) and separated by commas. 
- Pin ID: A unique pin ID, shown with a blue rectangle. You can find the ID next to the `"_id"`, first in line. Copy only the value between "". 
- Pin Title: Shown in green rectangle. It is a value of `"title"`. 
- Description: The description you added in EO Browser. You can edit this description anytime. Note that you can add links to image as well, and that the description is in Markdown. 
- Group: shown in purple rectangle. Optional parameter. You can use it to group pins together to be displayed as one group on the pin library. 
- highResUrl: If you have a high resolution image uploaded on Flickr or other similar website, you can add the link here. 

![json](/_imgs/Readme/json.png)

**Note that the only parameters you can edit are pinTitle, description, group and highResUrl. Changing any other existing parameter could cause your pin to not work!**

### 2.2. Set up folders 

In your local pin library repository, create a new folder with the name of your theme. Separate the words in the name using the `_` sign.
To demonstrate, we have added a folder called "Clouds_and_Hurricanes". 

![folder1](/_imgs/Readme/theme.png)

Copy your JSON file into this folder. Rename the JSON file so that it matches the name of your theme folder. For example, if the theme folder is named "Clouds_and_Hurricanes", the JSON file should also be named "Clouds_and_Hurricanes". Note that this is the name that will be displayed on the top of your theme in the Pin Library. If you would like to note your name, you simply add your name to the theme name like so: "themeName_by_yourName" (e.g. "Clouds_and_Hurricanes_by_Monja").

In the same folder, create another folder called `fig` (lowercase). 

![folder2](/_imgs/Readme/folder2.png)

### 2.3. Images

- Paste all your pin images corresponding to the same theme, into your newly created `fig` folder. 
- Next, replace the name of each image with the unique ID from the JSON file for the corresponding pin, like in the image below.

![arrow](/_imgs/Readme/image_rename.png)

- Next, you will need to add an image to represent your theme. As you can see on the image below, each theme has its own thumbnail, which is usually one of the pins, that best represents it. 

![first_page](/_imgs/Readme/lib_themes.png)

- To add a thumbnail for your new theme, just add a desired image into the folder `\_themeimgs` and **make sure the image is named exactly the same as your theme folder and JSON file**.

![thumbnail](/_imgs/Readme/theme_imgs.png)

### 2.4. OPTIONAL: Groups and High resolution links

If you leave your setup as it is, each pin will be a separate entity in your theme, such as with the Agriculture theme. 

![Agriculture](/_imgs/Readme/agriculture_pin.png)

If you would like to group pins by location, event or content, like for example in the Wildfires theme, where you can browse between several pins under the same category, you can do so using the optional `group` parameter in the JSON file. 

![Agriculture](/_imgs/Readme/croatia_pins.png)

You will have to open your JSON file and make sure that the pins you want grouped, have the same `group` value. The value can be anything - it can be a common theme, such as for example "Rice Fields", or it can be a number (e.g. 1). In the pin library, the group name will not be displayed - it will only be used to connect the pins together. It's crucial, that the same value is used for all the pins belonging to the same group. 

Make sure you add your group value in between the `""` signs, and not to accidentally delete anything. The JSON structure must stay like this: 

`"group":"Value",`

Note that you can also add a non-image element to the group, such as a photograph, a timelapse or a legend, by adding JSON content outside of the pin and adding the group parameter with the same value. (recommended only for experienced users). 

Additionally, you can add a URL link to a high resolution image of the pin, if available, to the `"highResImageUrl"` parameter. 

When you're done, commit your changes and push to the repository. Create a merge request. You're done!

### 2.5. Contribute to Existing Themes

- To add a new pin to the existing theme, export the particular pin from EO Browser and copy it from the JSON file (only the pin content, which is between the `{}` symbols) to the JSON file of the theme. Make sure that all pins have a comma at the end, except the last one. 
- Don't forget to add an image to the pin, if you're adding a new one. 
- To update an image, replace the image with another one, and make sure the name of the image stays the same, to keep the connection to the pin. 
- To edit a description, title or group, you need to edit it directly in the JSON file. 
- Check the previous chapters for more information.


