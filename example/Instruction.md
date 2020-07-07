# How to modify and excisting pin set 



---

# How to publish your own pin set

* Fork the repository to get your own copy of the EO Browser pins' repository
  _It is easiest to fork the repository on GitHub, but as some of you might not have a GitHub account, or don't want to bother with all this versioning and collaboration tools, you can also just download the whole repository as Zip file and work from there._
  
* Create a new directory for your pin set in the root directory (main "folder" called `EO-Browser-pins-repository`)
  *Give the newly created directory a name that best represents the pins it will include, e.g. `Lakes_in_Europe`.*   
  *Preferably use ["snake_case"](https://simple.wikipedia.org/wiki/Snake_case) (underscores instead of spaces) if more than one word is used.*
  
* Go to [EO Browser](https://apps.sentinel-hub.com/eo-browser/?zoom=10&lat=41.9&lng=12.5&themeId=DEFAULT-THEME), create and export a JSON file including only pins you want to include
  *Each pin should have a description. You can add them directly in EO Browser. Formating the text as well as links to resources can be included using [markdown](https://help.github.com/categories/writing-on-github/).*
  *After the download rename your JSON file to match the name of your repository, e.g. `Lakes_in_Europe.json`*
  *Copy the JSON file into your directory*
  
* Copy the example README.md from [here](../example/README.md) into your folder and enter the missing infos.   
  *The `Import` link can be created directly in EO Browser via the share function.
  *Have a look around at other `README.md` files to see how to include images, format the text and generally use the GitHub [markdown](https://help.github.com/categories/writing-on-github/) (e.g. [here](../Monitoring_Earth_from_Space/README.md). Images should be saved in a sepearte folder called `fig` *
  
* Add an entry pointing to your new directory to the [main](../README.md) README file.   
  *The name and a link will do.* 
  
* And create a pull request :).
  *There is extensive help on creating pull requests on GitHub [help](https://help.github.com/categories/collaborating-with-issues-and-pull-requests/), but if you feel overwhelmed by this step and would still like to contribute, send us the folder you've created and we will take care of it for you.*

Publishing your product should be easy, nevertheless, any feedback and ideas how to improve or make the process simpler is very appreciated.