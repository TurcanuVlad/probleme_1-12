"""Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
iepuri sunt în crescătorie? Exemplu : Date de intrare : nr. Iepuri la început de luna 10
nr. iepuri morti 2 nr. iepuri nascuti 6 Date de ieşire : 14 iepuri. 
"""
ni = int(input("cati iepuri erau la inceput de luna: "))
nim = int(input("cati iepuri au murit: "))
nin = int(input("cati iepuri s-au nascut: "))
print(ni - nim + nin," iepuri")