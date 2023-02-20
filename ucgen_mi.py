#******************Üçgen Mi******************#
def ücgen_mi(liste):
    if(abs(liste[0]+liste[1])>liste[2] and 
       abs(liste[0]+liste[2])>liste[1] and 
       abs(liste[1]+liste[2])>liste[0]):
            return True
    else:
            return False

liste= [(3,4,5),(6,8,10),(3,10,7)]
print(list(filter(ücgen_mi,liste)))

