#File app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hom/')
def home():
    return render_template('basicstructure.html')

if __name__ == '__main__':
    app.run()
