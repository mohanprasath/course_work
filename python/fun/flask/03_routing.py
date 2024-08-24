from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Main Page'

@app.route('/contact')
def contact_page():
    return 'Contact Page'

if __name__=='__main__':
    app.run()