# app.py

# 1. Import necessary libraries
# Flask is the framework we use to create the web application.
# render_template is used to send an HTML file to the browser.
from flask import Flask, render_template

# 2. Create a Flask application instance
# __name__ is a special Python variable that gives the script a unique name.
# It's needed so Flask knows where to look for resources like templates and static files.
app = Flask(__name__)

# 3. Define a route for the homepage
# The @app.route('/') decorator tells Flask that the function below
# should be triggered when someone visits the main URL of the site (e.g., http://127.0.0.1:5000/).
@app.route('/')
def index():
    """
    This function handles requests to the homepage.
    It renders and returns the 'index.html' file from the 'templates' folder.
    """
    # You can pass variables to your template like this:
    # return render_template('index.html', page_title='My To-Do App')
    return render_template('index.html')

# 4. Run the application
# The if __name__ == '__main__': block ensures that this code only runs
# when you execute the script directly (e.g., by running `python app.py`).
# It won't run if this file is imported into another script.
if __name__ == '__main__':
    # app.run(debug=True) starts the Flask development server.
    # debug=True is very useful during development because it automatically
    # reloads the server when you make code changes and shows detailed error pages.
    # IMPORTANT: Do not use debug=True in a production environment!
    app.run(debug=True)
