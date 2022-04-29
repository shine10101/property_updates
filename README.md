# Automatic Rightmove Updates

The following demonstrative project provides users with automatic and consistent email updates relating to new rental/for sale properties within pre-defined search parameters.


## How to use

Step 1. Install requirements.txt. This project leverages the ![rightmove-webscraper](https://github.com/toby-p/rightmove_webscraper.py) package

Step 2. Input email address, email username, password, smpt server and smpt server port. If using a gmail address, smpt server and smpt server port will equal smtp.gmail.com, and 587, respectively. 

Note: It is advised to create a new Google account as you will need to Turn "Allow less secure apps" to ON. Be aware that this makes it easier for others to gain access to your account.

Step 3. Go to <a href="http://www.rightmove.co.uk/">rightmove.co.uk</a> and search for whatever listings you are interested in.

Step 4. Filter search as per requirements, run search and copy URL.

Step 5. Input recipient email address and search URL to scrape.py and run script.


## Note

The use of webscrapers is unauthorised by rightmove. The following project is for demonstrative purposes only.