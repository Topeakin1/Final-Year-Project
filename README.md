Student Name: Temitope Akinwale.
Student Number: 16308933.
Supervisor: Brian MacNamee.
Project Title : Spoiler BeGone.

The goal of my project was to create a platform that can remove spoilers on the internet using machine learning principles. The development of my model and API was completed in Python a while the Chrome extension was developed in JavaScript as well as using HTML and CSS. 

This repository contains all of my code including the model, the api, and the chrome extension code. I included the many machine learning algorithms that I tested until I found one that works best for my data set. 

The following steps are needed to run this project.
- Download all of the folders created in the repository.
- Download Google Chrome.
- In the top right hand corner there is an icon containing three dots.
- Click the icon.
- Navigate to More tools --> Extensions --> Enable Developer Mode. 
- Click the "Load Unpacked" button in the top left corner.
- Select the folder containing the extension code (it is called "extension").
- This should load in the Spoiler BeGone extension.
- Click the activate button on the bottom right corner of the extension.

- On your desktop navigate to command prompt.
- Make sure to have a python version installed or download one at: https://www.python.org/downloads/
- We need to install the libraries used.
- Enter in the following commands : "pip install numpy" & "pip install nltk".
- If a ModuleNotFoundError occurs, enter in the "pip install" command followed by the name of the module thats missing.
- Enter in the command "pip install Flask" / "pip3 install Flask" for python 3 users.
- Use the cd command to navigate to the api folder.
- Enter in the command "python app.py". 
- This will genenerate a local host that will then connect to the chrome extension.

- Go back to Google Chrome
- You should see an S icon beside the "star" icon for bookmarking.
- Navigate to any webpage and if a spoiler is detected the model should black out the paragraph containing the spoiler.

The data set used in this project is too large to upload on GitHub, the Google Drive link below should be used to download all of the files to run the code properly. Go to the FYP Data Sets folder.
Download these files and place them in the same directory.
The json files go into the src--> model folder.
The pickle file goes into the src --> model folder and the api folder.
https://drive.google.com/drive/folders/1wngzUuMIhBsjualNI2ChMjxXm-0U09uA
