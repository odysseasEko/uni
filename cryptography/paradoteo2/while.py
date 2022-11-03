num = 42 #orizoume ton arithmo pou theloume o hristis na mantepsei
running = True #boolean value pou tha kanei to vroho na epanalamvanete
while running:
    guess = int(input("eisagete enan akaireo:")) #zitame apo ton hristei na isagei ton arithmo pou pistevei
    if guess == num: #an o arithmos pou mantepse einai o swstos to programa mas kanei print tin parakatw protasi
        running = False #boolean value pou tha kanei to vroho na stamatisei
        print("\nBravo filtate\nH apadisi sti zoi, to simban kai ta pada\n")
    elif guess < num: #an o arithmos pou mantepse einai mikroteros apo ton num to programa mas kanei print tin parakatw protasi
        print("vale kialo")
    else:#an o arithmos pou mantepse einai megaliteros apo ton num to programa mas kanei print tin parakatw protasi
        print("parapiges man m")

print("telos")
    