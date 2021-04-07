#File app.py
from flask import Flask, render_template, request, jsonify 
import cipher
app = Flask(__name__, static_folder="static/")

@app.route('/')
@app.route('/home/')
def home():
    return render_template('encryption.html')
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/encrypt/caesar/', methods= ['POST'])
def caeser():
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

@app.route('/encrypt/vigenere/', methods= ['POST'])
def vigenere():
    pt = request.form["plaintext"]
    keyword = request.form["key"]
    print(pt,keyword)
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
    pt = request.form['plaintext']
    key = request.form['key']
    msg,ct,key_matrix = cipher.playfair(pt,key)
    if ct:
        return jsonify({'msg':msg,'cipher': ct,'key_matrix':key_matrix})
    return jsonify({'error':'Something went wrong'})

@app.route('/encrypt/keylesstrans/',methods=['POST'])
def keyless_transposition():
    pt = request.form['plaintext']
    block_size = request.form['block']
    msg,ct = cipher.keyless_transposition(pt,int(block_size))
    if ct:
        return jsonify({'msg': msg ,'cipher': ct})
    return jsonify({'error':'Something went wrong'})

@app.route('/encrypt/coltrans/',methods=['POST'])
def col_transposition():
    pt = request.form['plaintext']
    key = request.form['key']
    error,msg,ct = cipher.columnar_transposition(pt,key)
    if ct:
        return jsonify({'code':200 ,'msg': msg ,'cipher': ct})
    return jsonify({'code':400,'error': error})



@app.route('/decrypt/',methods=['GET'])
def decrypt():
    return render_template('decryption.html')

@app.route('/decrypt/caesar/', methods=['POST'])
def caesar():
    ct = request.form["cipher"].lower()
    key = request.form["key"]
    pt = cipher.CCdecrypt(ct,int(key))
    if ct:
        return jsonify({'plaintext': pt})
    return jsonify({'error' : 'Something went wrong'})

if __name__ == '__main__':
    app.run(debug=True)
