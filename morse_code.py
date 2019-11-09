MORSE_CODE = { 'A':'.-',
                    'B':'-...', 
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.', 
                    'F':'..-.',
                    'G':'--.',
                    'H':'....', 
                    'I':'..',
                    'J':'.---',
                    'K':'-.-', 
                    'L':'.-..',
                    'M':'--',
                    'N':'-.', 
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-', 
                    'R':'.-.',
                    'S':'...',
                    'T':'-', 
                    'U':'..-',
                    'V':'...-',
                    'W':'.--', 
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..', 
                    '1':'.----',
                    '2':'..---',
                    '3':'...--', 
                    '4':'....-',
                    '5':'.....',
                    '6':'-....', 
                    '7':'--...',
                    '8':'---..',
                    '9':'----.', 
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-', 
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-', 
                    '(':'-.--.',
                    ')':'-.--.-',
                    "'":'.----.',
                    '!':'-.-.--',
                    '&':'.-...',
                    ':':'---...',
                    ';':'-.-.-.',
                    '=':'-...-',
                    '+':'.-.-.',
                    '-':'-....-',
                    '_':'..--.-',
                    '"':'.-..-.',
                    '$':'...-..-',
                    '@':'.--.-.'}

def main():
    print("")
    print("This program encodes and decodes Morse code.")
    print("")
    
    while True:             # Loop continuously
        option = input("Would you like to encode (e),decode (d) or quit (q): ")
        print("")
        if option == "e":
            message = input("What message would you like to encode: ")
            print("")
            message = encryption(message.upper())
            print (message)
            print("")
            
        elif option == "d":
            message = input("What message would you like to decode: ")
            print("")
            message = decryption(message.upper())
            print (message)
            print("")
            
            
        elif option == "q":
            print ("Thanks for using the program, goodbye!")
            break

        elif option != "":
            print("Invalid option please select the right option.")
            print("")

def encryption(message):
 
    encode = ''
    
    for x in message: 
        if x != ' ': 
            encode += MORSE_CODE[x] + ' '
        else: 
            encode += ' '
    return encode 
    
# This function is used to decode
# Morse code to English
def decryption(message):
   message += ' '
   decode = ''
   character = ''
   
   for x in message:
      # checks for space
      if (x != ' '):
         i = 0              # counter to keep track of space 
         character += x        # storing morse code of a single character 

      else: # in case of space
         i += 1             #indicates a new character 
         if i == 2 :        #indicates a new word
            decode += ' '   # adding space to separate words 
         else: # accessing the keys using their values (reverse of encryption)
            decode += list(MORSE_CODE.keys())[list(MORSE_CODE.values()).index(character)]
            character = ''
   return decode

   
# Executes the main function
if __name__ == '__main__':
   main()
