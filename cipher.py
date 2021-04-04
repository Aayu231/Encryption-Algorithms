import math
#MonoAlphabetic Cipher
#Caesar Cipher
def CCencrypt(string, CCkey):
    return ''.join([chr((ord(letter) + CCkey - 97) % 26 + 97) for letter in string])

def multiplicative(string, key):
    return ''.join([chr(((ord(letter) - 97) * key) % 26 + 97) for letter in string])
 
def affine(string, key, key2):
    string = string.lower()
    return ''.join([chr((((ord(letter) - 97) * key) + key2) % 26 + 97) for letter in string])

def CCdecrypt(string, CCkey):
    return ''.join([chr((ord(letter) - CCkey - 97) % 26 + 97) for letter in string])
    
#PolyAlphabetic Cipher [Vigenere, Autokey, Playfair] 
#Vigenere Cipher
def vigenere_encrypt(msg, key):
    return "".join([chr((((ord(msg[i])-97)+(ord(key[i%len(key)])-97))%26)+97) for i in range(len(msg))])
    
#Autokey Cipher  
def autokey_encrypt(msg,key):
    cipher = chr((ord(msg[0])-97 + int(key))%26 + 97)
    return cipher+''.join([chr((ord(msg[i])-97 + ord(msg[i-1])-97)%26 + 97)for i in range(1,len(msg))])

#playfair cipher 
def playfair(msg,keyword):
    key = ''
    key_matrix = []
    for letter in keyword:
        if letter not in key:
            key += letter
            
    for i in range(26):
        if chr(i+97) not in key:
            key += chr(i+97)
    i = 0
    key = key.replace('j','')
    while i < len(key):
        key_matrix.append(key[i:i+5])
        i += 5
    
    i = 0 
    while i < len(msg):
        if len(msg[i:]) > 1:
            if msg[i] == msg[i+1]:
                msg = msg[:i+1] +'x'+msg[i+1:]
        else:
            msg += 'z'
        i += 2
    cipher = ''
    i = 0 
    while i < len(msg):
        if msg[i] == 'j':
            msg[i] = 'i'
        col1 = ((key.index(msg[i])+1) % 5) -1
        row1 = math.ceil((key.index(msg[i])+1)/5) -1
        
        if msg[i+1] == 'j':
            msg[i+1] = 'i'
        col2 = ((key.index(msg[i+1])+1) % 5) -1
        row2 = math.ceil((key.index(msg[i+1])+1)/5) - 1
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
            cipher += key_matrix[row1][col1] + key_matrix[row2][col2]
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
            cipher += key_matrix[row1][col1] + key_matrix[row2][col2]
        else:
            cipher += key_matrix[row1][col2] + key_matrix[row2][col1]
        
        i += 2
    return msg,cipher,key_matrix

#transposition Cipher [Keyed]
def columnar_transposition(msg,key):
    blocks = []
    key_length = len(key)
    i = 0
    key_cipher = ''
    if len(msg)%len(key) != 0:     #Balancing letters in message. making it multiple of key by adding bogus character '_'
        msg += '_'*(len(key) - len(msg)%len(key))
    
    while (i < len(msg)):   #dividing in blocks
        blocks.append(msg[i:i+key_length])
        i+=key_length
    
    for index in key:   #keyed encryption
        for block in blocks:
            key_cipher+= block[int(index)-1]
    return msg, key_cipher
    
#transposition Cipher [keyless]
def keyless_transposition(msg,block_size):
    msg = msg.replace(' ','_')
    blocks = []
    key_length = block_size
    i = 0
    key_cipher = ''
    if len(msg)%key_length != 0:     #Balancing letters in message. making it multiple of key by adding bogus character '_'
        msg += '_'*(key_length - len(msg)%key_length)
    
    while (i < len(msg)):   #dividing in blocks
        blocks.append(msg[i:i+key_length])
        i+=key_length
        
    transpose_matrix = ["".join([blocks[j][i] for j in range(len(blocks))]) for i in range(len(blocks[0]))]
    print(transpose_matrix)
    keyless_cipher = "".join([block for block in transpose_matrix])
    return msg,keyless_cipher #, key_cipher
