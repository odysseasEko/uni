message = input("parakalw valte keimeno gia na kriptografithei:\n") #to minima pou tha kriptografithei
translated = "" #variable pou tha hriastoume gia tin apothikefsi toy encrypted minimatos

i = len(message)-1 #me to len metrame ton arithmo twn haraktirwn etsi wste na xeroume poses fores na epanalavoyme ton vroho
while i >= 0: #o vrohos
    translated = translated + message[i] #epidi i python vlepei ta string ws listes haraktirwn kanoume tin alagi se dio listes
    i = i-1 #counter gia na vgoume apo ton vroho

print(message)
print(translated)
