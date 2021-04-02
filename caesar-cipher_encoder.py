# caesar-cipher encoder in python - github.com/damnicolussi/caesar-cipher/blob/main/caesar-cipher_encoder.py

def rot(phrase, rotation):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out = ""
   for char in phrase:
       out += abc[(abc.find(char)+rotation)%26]
   return out

phrase = input('Enter your phrase: ')
rotation = int(input('Enter the rotation: '))

print(rot(phrase, rotation))
