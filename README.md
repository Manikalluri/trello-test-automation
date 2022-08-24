# trello-test-automation
Trello test automation contains front end simulation using python
Repo trello-test-automation

## Packages to be installed
pip3 install selenium
sudo apt-get install firefox-geckodriver


## Project structure

```
branch master
|
|_ automation
|	|
|	|
|	|_ comm_utility (Utility classes)(Contains Action classes)
|   | 
|	|
|	|_ testsuites ( test case scripts)
|
|_ debug_logs (Python debug logs and Test Reports)
```

'''comm_utility''' contains below files and 

 ```ConfigParser.py is responsible for parsing the config file from UserConfig.ini```
 ```Constants.py is responsible for the Global constants```
``` DriverUtility.py will initialize the web driver with firefox browser```
 ```Logger.py will do the logging for all actions```
``` ResultReporter.py will prepare the result report```
``` trello_web_actions.py contains the web actions```
 
 '''testsuites''' contains the feature testcases
 
 '''UserConfig''' contains the environment details and user credentials
