#De la tastatură se întroduce numărul de rînd al culorii curcubeului. De afişat
#denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.
culoare = int(input("dati numarul culorii curcubeului: "))
if (culoare == 1):
    print("acesta este numarul culorii rosu")
elif (culoare == 2):
    print("acesta este numarul culorii oranj")
elif (culoare == 3):
    print("acesta este numarul culorii galben")
elif (culoare == 4):
    print("acesta este numarul culorii verde")
elif (culoare == 5):
    print("acesta este numarul culorii albastru")
elif (culoare == 6):
    print("acesta este numarul culorii indigo")
elif (culoare == 7):
    print("acesta este numarul culorii violet")
else:
    print("invata culorile curcubeului")