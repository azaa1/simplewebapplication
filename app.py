from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime

app = Flask(__name__)

# Render index.html
@app.route('/')
def home():
   return render_template('index.html')

# Render about.html
@app.route('/about')
def about():
   return render_template('about.html')

# datetime
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


       
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = True)
