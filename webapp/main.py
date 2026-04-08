from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This looks for index.html inside the 'templates' folder
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    # Cloud Shell uses port 8080 by default
    app.run(host='127.0.0.1', port=8080, debug=True)
