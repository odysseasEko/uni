# Filename: using_list.py
# Αυτή είναι η λίστα αγορών μου
shoplist = ['magioneza', 'stafilia', 'tsigara', 'melitzanes'] #dimiourgw mia lista 
print('Πρέπει ν\' αγοράσω', len(shoplist), 'πράγματα.') #me to len() metraw ta items mesa sti lista
print('Τα πράγματα αυτά είναι:', end=' ') #to end me tin hrisi tou broxou emfanizei ta items tis listas
for item in shoplist: #o vrohos emfanizei ta items
    print(item, end=' ')
print('\nΠρέπει επίσης ν\' αγοράσω harti igias.')
shoplist.append('harti igias') #prosthetoume to rizi sti lista
print('Η λίστα αγορών μου τώρα είναι:', shoplist) #emfanizw updated lista
print('Θα ταξινομήσω τη λίστα μου τώρα')
shoplist.sort() #etimo func gia short tis listas
print('Η ταξινομημένη λίστα μου είναι', shoplist) #xanaemfanizw tin lista sorted
print('Το πρώτο πράγμα που θ\' αγοράσω είναι', shoplist[1]) #dialegw to deftero item apo ti lista
olditem = shoplist[1] #vazw to item se mia metavliti prin diagrafei
del shoplist[1] #diagrafo to deftero item apo ti lista
print('Αγόρασα το', olditem) #emfanize ti metavliti
print('Η λίστα αγορών μου τώρα είναι', shoplist) #updated lista horis to deftero item