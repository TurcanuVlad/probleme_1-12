"""Doi copii au primit acelaşi număr de mere Introducând de la tastatură numărul de mere
primite, afişaţi câte mere are fiecare copil după ce primul copil mănâncă un măr şi dă
unul celuilalt copil. Exemplu : Date de intrare : 10 Date de ieşire : primul copil 8
mere al doilea copil 11 mere. 
"""
mere_total = int(input("Dati numarul de mere: "))
copil1 = mere_total - 2
copil2 = mere_total + 1
print("primul copil a ramas cu ",copil1," mere, iar al doilea cu ",copil2," mere")