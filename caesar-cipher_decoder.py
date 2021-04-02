# rot13 decoder in python - github.com/damnicolussi/caesar-cipher/blob/main/caesar-cipher_decoder.py

def rot(phrase, rot):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out = ""
   for char in phrase:
       out += abc[(abc.find(char)+(26-rot))%26]
   return out

phrase = input('Enter your phrase: ')
rot = int(input('Enter the rotation: '))

print(rot13(phrase, rot))
