#!/usr/bin/env python
import optparse
import sys

desc="""This python scripts take as an input a string and the decrypts it using the caesar cipher. If the -a option is on, (./Caesar_Cipher.py -a) all the possible keys (i.e. al 26 of them) will be used and all possible decryptions of the input string will be displayed"""
Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def Decrypt(plain_text, key):
	cipher_text=[]
	for i in range(len(plain_text)):
            if plain_text[i]==" ":
                cipher_text.append(" ")
            elif plain_text[i].isupper():
                cipher_text.append(Alphabet[(Alphabet.index(plain_text[i].upper())+key)%26])
            elif plain_text[i].islower():
                cipher_text.append((Alphabet[(Alphabet.index(plain_text[i].upper())+key)%26]).lower())
            else: #either a number or a symbol
                cipher_text.append(plain_text[i])
	return cipher_text

def All_keys(option, opt, value, parser):
	plain_text=raw_input('Enter your message: ')
        for key in range(1,26):
                print "\033[92mWith key: \033[0m"+repr(key)+"\033[92m Cipher Text: \033[0m"+''.join(Decrypt(plain_text, key))
	sys.exit(0)

def main(): 
        parser = optparse.OptionParser(description=desc)
        parser.add_option('-a', '--all', action="callback", callback=All_keys, default=False, help='try all keys in the keyspace')
        (opts, args) = parser.parse_args()
	
	plain_text=raw_input('Enter your message: ')
	Shifted_Alphabet=[]
	try:
	    key=int(raw_input('Choose Your key: '))
	except ValueError:
	    print "The key should be a number"
	if (key==0) or (key==26):
	    print "I would rethink your key if I were you...\n"
	for i in range(26):
	    Shifted_Alphabet.append(Alphabet[(i+key)%26])
	print "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" + \
	            "Your enctyption Dictionary looks something like this: \n"+', '.join(Alphabet) + \
	            "\n-------------------------------------------------------------------------------------------------------------\n" + \
	            ', '.join(Shifted_Alphabet) + \
	            "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
	print "Cipher Text: "+''.join(Decrypt(plain_text, key))

if __name__ == '__main__': 
	main()
