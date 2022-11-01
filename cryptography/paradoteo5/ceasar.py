def encrypt(text,s): #xekinaei to function
    result = "" #string result pou tha gemisoume parakatw
    for i in range(len(text)): #setaroume ton vroho gia ton arithmo haraktirwn tis metavlitis text
        char = text[i] #char einai enas enas oi haraktires tou string text giati opos eidame sti proigoumeni ergasia ta string sti python einai pinakes
        if (char.isupper()): #an o haraktiras mas einai kefaleo benei edw
            result += chr((ord(char) + s - 65) % 26 + 65)
        else: #an o haraktiras mas einai otidipote allo benei edw
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result #epistrefoume to apotelesma tou shift

text = "WH OHI ME MAHAIROSAN POLLES FORES" #to keimeno pou tha kriptografisoume
s = 8 #poso shift tha kanei o algorithmos
print ("Plain Text : " + text) 
print ("Shift pattern : " + str(s))
print ("Cipher: " + encrypt(text,s))