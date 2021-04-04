#File app.py
from flask import Flask, render_template, request, jsonify 
import cipher
app = Flask(__name__, static_folder="static/")

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/encrypt/caeser')
def ceaser():
    pt = request.POST["plaintext"]
    key = request.POST["key"]
    ct = cipher.CCencrypt(pt,key)
    
if __name__ == '__main__':
    app.run(debug=True)
