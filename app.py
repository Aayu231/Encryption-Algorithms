#File app.py
from flask import Flask, render_template, request, jsonify 
import cipher
app = Flask(__name__, static_folder="static/")

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/encrypt/caesar/', methods= ['POST'])
def ceaser():
    pt = request.form["plaintext"].lower()
    key = request.form["key"]
    ct = cipher.CCencrypt(pt,int(key))
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/multiplicative/', methods= ['POST'])
def multiplicative():
    pt = request.form["plaintext"].lower()
    key = request.form["key"]
    ct = cipher.multiplicative(pt, int(key))
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/affine/', methods= ['POST'])
def affine():
    pt = request.form["plaintext"]
    multkey = request.form["affine_key1"]
    addkey = request.form["affine_key2"]
    ct = cipher.affine(pt,int(multkey),int(addkey))
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/vigenere/',methods= ['POST'])
def vigenere():
    pt = request.form["plaintext"]
    keyword = request.form["keyword"]
    ct = cipher.vigenere_encrypt(pt,keyword)
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/autokey/',methods=['POST'])
def autokey():
    pt = request.form['plaintext']
    key = request.form['key']
    ct = cipher.autokey_encrypt(pt, int(key))
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error':'Something went wrong'})

@app.route('/encrypt/playfair/',methods=['POST'])
def playfair():
    pt = request.POST['plaintext']
    key = request.POST['key']
    msg,ct,key_matrix = cipher.autokey_encrypt(pt,key)
    if ct:
        return jsonify({'msg':msg,'cipher': ct,'key_matrix':key_matrix})
    return jsonify({'error':'Something went wrong'})

@app.route('/encrypt/keylessTransposition/',methods=['POST'])
def keyless_transposition():
    pt = request.POST['plaintext']
    block_size = request.POST['key']
    msg,ct = cipher.keyless_transposition(pt,block_size)
    if ct:
        return jsonify({'msg': msg ,'cipher': ct})
    return jsonify({'error':'Something went wrong'})

@app.route('/encrypt/colTransposition/',methods=['POST'])
def col_transposition():
    pt = request.POST['plaintext']
    key = request.POST['key']
    msg,ct = cipher.columnar_transposition(pt,key)
    if ct:
        return jsonify({'msg': msg ,'cipher': ct})
    return jsonify({'error':'Something went wrong'})

if __name__ == '__main__':
    app.run(debug=True)
