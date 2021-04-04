#File app.py
from flask import Flask, render_template, request, jsonify 
import cipher
app = Flask(__name__, static_folder="static/")

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/encrypt/caeser/',methods= ['POST'])
def ceaser():
    pt = request.form["plaintext"].lower()
    key = request.formpt = request.form["key"]
    ct = cipher.CCencrypt(pt,int(key))
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/multiplicative',methods= ['POST'])
def multiplicative():
    pt = request.POST["plaintext"]
    key = request.POST["key"]
    ct = cipher.multiplicative(pt,key)
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/affine/',methods= ['POST'])
def affine():
    pt = request.POST["plaintext"]
    multkey = request.POST["multkey"]
    addkey = request.POST["addkey"]
    ct = cipher.affine(pt,multkey,addkey)
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/vigenere/',methods= ['POST'])
def vigenere():
    pt = request.POST["plaintext"]
    keyword = request.POST["keyword"]
    ct = cipher.vigenere_encrypt(pt,keyword)
    if ct:
        return jsonify({'cipher': ct})
    return jsonify({'error' : 'Something went wrong'})

@app.route('/encrypt/autokey/',methods=['POST'])
def autokey():
    pt = request.POST['plaintext']
    key = request.POST['key']
    ct = cipher.autokey_encrypt(pt,key)
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
