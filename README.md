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
- Navigate to More tools --> Extensions.
- Click the "Load Unpacked" button in the top left corner.
- Select the folder containing the extension code (it is called "extension").
- This should load in the Spoiler BeGone extension.
- Click the activate button on the bottom right corner of the extension.

- On your desktop navigate to command prompt.
- Use the cd command to navigate to the api folder.
- Enter in the command "python app.py". 
- This will genenerate a local host that will then connect to the chrome extension.

- Go back to Google Chrome
- You should see an S icon beside the "star" icon for bookmarking.
- Navigate to any webpage and if a spoiler is detected the model should black out the paragraph containing the spoiler.



