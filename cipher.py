import math
#MonoAlphabetic Cipher
#Caesar Cipher
def CCencrypt(string, CCkey):
    return ''.join([chr((ord(letter) + CCkey - 97) % 26 + 97) for letter in string])

def multiplicative(string, key):
    return ''.join([chr(((ord(letter) * key) - 97) % 26 + 97) for letter in string])
 
 
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

#transposition Cipher [Keyed and keyless]
def transposition(msg,key):
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
    #keyless encryption        
    transpose_matrix = ["".join([blocks[j][i] for j in range(len(blocks))]) for i in range(len(blocks[0]))]
    keyless_cipher = "".join([block for block in transpose_matrix]) #keyless cipher
    return msg,keyless_cipher, key_cipher
    
    
def main():
    message = input("Enter Message: ").lower().replace(' ','')
    print('!!!All Operations will be carried out in Lower case!!!\n')  
    print('*********MonoAlphabetic Cipher [Ceaser Cipher]*********\n')
    CCkey = int(input("Ceaser Encryption Key:"))
    CCcipher = CCencrypt(message, CCkey)
    print("\nOriginal message : ", message,"\nafter Encryption : ",CCcipher,'\nAfter Decryption : ', CCdecrypt(CCcipher, CCkey))
    print('\n\n*********PolyAlphabetic Cipher*********\n *********[Vigenere Ciphering]*********\n')
    key = input('Enter Vigenere Key:').lower().replace(' ','')
    print("\nOriginal message : ",message,"\nafter Encryption : ", vigenere_encrypt(message,key))
    print('\n\n*********PolyAlphabetic Cipher *********\n*********[Autokey Cipher]*********\n')
    key = input('Enter Autokey Ciphering Key:').lower().replace(' ','')
    print("\nOriginal message : ",message,"\nafter Encryption : ", autokey_encrypt(message,key))
    print('\n\n*********PolyAlphabetic Cipher *********\n*********[Playfair Cipher]*********\n')
    key = input('Enter Playfair Keyword:').lower().replace(' ','')
    msg,cipher,key_matrix = playfair(message,key)
    print('The Message after pair correction is : ',msg)
    print('The generated key matrix is : ', key_matrix)
    print("\nOriginal message   : ", message,"\nAfter Encryption : ",cipher)

    print('\n\n*********Transposition Cipher [Keyed and Keyless]*********\n')
    key = input('Enter Transposition Key:').lower().replace(' ','')
    res = transposition(message, key)
    print("\nOriginal message   : ", res[0],"\nKeyless Encryption : ",res[1],"\nKeyed Encryption   : ",res[2])

if __name__=='__main__':
    main()