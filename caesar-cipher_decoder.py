# caesar-cipher decoder in python - github.com/damnicolussi/caesar-cipher/blob/main/caesar-cipher_decoder.py

def rot(phrase, rotation):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out = ""
   for char in phrase:
       out += abc[(abc.find(char)+(26-rotation))%26]
   return out

phrase = input('Enter your phrase: ')
rotation = int(input('Enter the rotation: '))

print(rot(phrase, rotation))
