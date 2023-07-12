# gamebase

Base source code for Gamebase application

The application runs from the `gamebase.py` file. In this file all the routes (urls) are defined that a user can navigate to. When a url is hit, the associated python function will be run, and the specified html page is returned to the user.

All `html` files are found in the `templates` directory. Static files such as images, javascript and css files are stored in the `static` directory.

To run the application locally on your computer, you can download the source code, navigate to the source directory and run the following comand:
```bash
# This command will run the application on your computer and you can access it by navigating to 'localhost:5000' in your browser
python gamebase.py
```
