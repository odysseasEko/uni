import ceasarModule
def hackCeasar(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)): #vrohos me arithmo epanalipsewn oso i alfavita
        translated = '' #string gia na apothikeftei to teliko
        for symbol in message: # epanalipsi gia ossa gramata einai to minima
            if symbol in LETTERS: # an to grama einai mesa sto LETTERS tote:
                num = LETTERS.find(symbol) # vriskei to antistiho grama kai vazei ton arithmo sto pinaka letters
                num = num - key # kanei to shift
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + " " # an den eiparhei sto letters vazw space
        print('Hacking key #%s: %s' % (key, translated))

text = input("parakalw valte keimeno gia na kriptografithei (kefalea):\n")
s = 8
print ("Plain Text : " + text) 
message = ceasarModule.encrypt(text,s) #kalw to ceasarModule pou kanei encrypt to message
hackCeasar(message) #kalw tin hack ceasar apo panw