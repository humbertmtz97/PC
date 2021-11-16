import argparse
parser = argparse.ArgumentParser() 
parser.add_argument("-mensaje", dest="mensaje1", help="Ingresa el mensaje descifrar")
params = parser.parse_args()
print(params)
print(type(params))
print(params.mensaje1)
print(type(params.mensaje1))

message = input('Ingresa el mensaje para cifrar: ')
espacios = 1
while espacios > 0:
    clave = input('Ingresa tu palabra clave para cifrar: ')
    espacios = clave.count(' ')
    if clave.isalpha() == False:
        espacios += 1
key = len(clave)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex + key

        print(translatedIndex)
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

print(translated)

print ("\n")

message = input('Ingresa el mensaje para descifrar: ')
espacios = 1
while espacios > 0:
    clave = input('Ingresa la misma clave para descifrar: ')
    espacios = clave.count(' ')
    if clave.isalpha() == False:
        espacios += 1
key = len(clave)

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
    # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        translatedIndex = symbolIndex - key

        print(translatedIndex)
        
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

print(translated)


message = input('Ingresa el mensaje: ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


for key in range(len(SYMBOLS)):
    
    
    translated = ''

    

    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            
            translated = translated + SYMBOLS[translatedIndex]

        else:
            
            translated = translated + symbol

    
    print('Key #%s: %s' % (key, translated))
