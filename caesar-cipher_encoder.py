# rot13 encoder in python - github.com/damnicolussi/caesar-cipher

def rot13(phrase, rot):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""
   for char in phrase:
       out_phrase += abc[(abc.find(char)+rot)%26]
   return out_phrase

phrase = input('Enter your phrase: ')
rot = int(input('Enter the rotation: '))

print(rot13(phrase, rot))
