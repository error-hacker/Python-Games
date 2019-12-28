# Ceaser Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you want to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message :')
    return input()

def getKey():
    key=0
    while True:
        print('Enter the key no. (1-%s)'%(MAX_KEY_SIZE))
        key = int(input())
        if(key>=1 and key<=MAX_KEY_SIZE) :
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0]== 'd' :
        key=-key
    translated = ''
    
    for letter in message:
        symbolIndex = SYMBOLS.find(letter)
        if symbolIndex == -1:
            translated += letter
        else:
            symbolIndex += key
            if symbolIndex>= MAX_KEY_SIZE:
                symbolIndex -= MAX_KEY_SIZE
            elif symbolIndex <0:
                symbolIndex += MAX_KEY_SIZE
                
            translated += SYMBOLS[symbolIndex]
    return translated

mode= getMode()
message = getMessage()
key = getKey()
print('Your translated text is :')
print(getTranslatedMessage(mode, message, key))