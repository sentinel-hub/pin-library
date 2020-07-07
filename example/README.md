# Example README

---

## How to modify and excisting pin set 

* Fork the repository to get your own copy of the EO Browser pins' repository
  *It is easiest to fork the repository on GitHub, but as some of you might not have a GitHub account, or don't want to bother with all this versioning and collaboration tools, you can also just download the whole repository as Zip file and work from there.*

* Import the pin set via the import link into EO Browser
  *Each theme has an import link at the top of each page*

### You want to suggest an improved description for one or more pins

* Modify the description or add new pins (including a description) that match the theme and export all pins
  *In EO Browser you can easily modify the description(s)*
  *Via export you can save all pins that belong to the theme as a JSON file*
  
* Replace the JSON file in the corresponding directory 

* And create a pull request :).
  *There is extensive help on creating pull requests on GitHub [help](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/), but if you feel overwhelmed by this step and would still like to contribute, send us the folder you've created and we will take care of it for you.*

## How to publish your own pin set

* Fork the repository to get your own copy of the EO Browser pins' repository
  *It is easiest to fork the repository on GitHub, but as some of you might not have a GitHub account, or don't want to bother with all this versioning and collaboration tools, you can also just download the whole repository as Zip file and work from there.*
  
* Create a new directory for your pin set in the root directory (main "folder" called `EO-Browser-pins-repository`)
  *Copy the `example` directory and rename it to a name that best represents the pins it will include, e.g. `Lakes_in_Europe`.*   
  *Preferably use ["snake_case"](https://simple.wikipedia.org/wiki/Snake_case) (underscores instead of spaces) if more than one word is used.*
  
* Go to [EO Browser](https://apps.sentinel-hub.com/eo-browser/?zoom=10&lat=41.9&lng=12.5&themeId=DEFAULT-THEME), create and export a JSON file including only pins you want to include
  *Each pin should have a description. You can add them directly in EO Browser. Formating the text as well as links to resources can be included using [markdown](https://help.github.com/categories/writing-on-github/).*
  *After the download rename your JSON file to match the name of your repository, e.g. `Lakes_in_Europe.json`*
  *Copy the JSON file into your directory*
  
* Fill in the details about the project in the `README.md` file.   
  *Obviously, you'll want to remove this chapter , but use the rest of the file as a template.*   
  *Have a look around at other `README.md` files to see how to include images, format the text and generally use the GitHub [markdown](https://help.github.com/categories/writing-on-github/) (e.g. [here](../Monitoring_Earth_from_Space/README.md). Images should be saved in a sepearte folder called `fig` *
  
* Add an entry pointing to your new directory to the [main](../README.md) README file.   
  *The name and a link will do.* 
  
* And create a pull request :).
  *There is extensive help on creating pull requests on GitHub [help](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/), but if you feel overwhelmed by this step and would still like to contribute, send us the folder you've created and we will take care of it for you.*

Publishing your product should be easy, nevertheless, any feedback and ideas how to improve or make the process simpler is very appreciated.

---

# Title

[Import](https://apps.sentinel-hub.com/eo-browser/?sharedPinsListId=1a13b4fd-47bc-4bb4-a03f-d386e0b1f728){:target="_blank"} pins directly into EO Browser or [download](Wildfires.json){:target="_blank"} the json for a later import into [EO Browser](https://apps.sentinel-hub.com/eo-browser/?zoom=10&lat=41.9&lng=12.5&themeId=DEFAULT-THEME){:target="_blank"}.

Following is a set of pins which are all connected to the topic __ENTER YOUR TOPIC HERE__. Each pin contains a brief description of what is displayed by the pin and a preview image linked to a high-resolution print on flickr.

## Included pins 

### Pin Name

Description
