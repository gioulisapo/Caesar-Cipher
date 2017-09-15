#!/usr/bin/env python3
import optparse
import sys

desc="""This python scripts take as an input a string and the decrypts or encrypts it using the caesar cipher.\
 The term key, refers to the number of times the Alphabet will shift to the right."""
Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def Decrypt(plain_text, key):
	'''Encryption/Decryption algorithm'''
	cipher_text=""
	for i in range(len(plain_text)):
            if plain_text[i]==" ":
                cipher_text+= (" ")
            elif plain_text[i].isupper():
                cipher_text+= (Alphabet[(Alphabet.index(plain_text[i].upper())+key)%26])
            elif plain_text[i].islower():
                cipher_text+= ((Alphabet[(Alphabet.index(plain_text[i].upper())+key)%26]).lower())
            else: #either a number or a symbol
                cipher_text+= plain_text[i]
	return cipher_text

def All_keys(plain_text):
        for key in range(1,26):
                print ("\033[92mWith key: \033[0m"+repr(key)+"\033[92m Cipher Text: \033[0m"+''.join(Decrypt(plain_text, key)))

def main():
	parser = optparse.OptionParser(description=desc)
	parser.add_option('-a', '--all', action="store_true", default=False, help='All the possible keys (i.e. al 26 of them)\
																onwill be used on the input string')
	parser.add_option("-i", "--input_file",  dest="input_filename",  help="Read input from FILE", metavar="FILE")
	parser.add_option("-o", "--output_file",  dest="output_filename",  help="Write result in FILE", metavar="FILE")
	(opts, args) = parser.parse_args()

	if opts.input_filename == None:
		plain_text=input('Enter your message: ')
	else:
		f = open(opts.input_filename, 'r')
		plain_text = f.read()
	if opts.all == True:
		All_keys(plain_text)
	else:
		Shifted_Alphabet=[]
		try:
		    key=int(input('Choose Your key: '))
		except ValueError:
		    print ("The key should be a number")
		if (key==0) or (key==26):
		    print ("I would rethink your key if I were you...\n")
		for i in range(26):
		    Shifted_Alphabet.append(Alphabet[(i+key)%26])
		print ("\nYour enctyption Dictionary:\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\033[93m" + \
		            ', '.join(Alphabet) + \
		            "\033[0m\n-------------------------------------------------------------------------------------------------------------\n\033[92m" + \
		            ', '.join(Shifted_Alphabet) + \
		            "\n\033[0m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
		if opts.output_filename == None:
			print ("Cipher Text: "+' '+(Decrypt(plain_text, key)))
		else:
			f = open(opts.output_filename, 'w+')
			f.write(Decrypt(plain_text, key))

if __name__ == '__main__':
	main()
