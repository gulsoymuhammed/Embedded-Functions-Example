#******************Dikdörtgen Alan Hesaplama******************#

def alanHesapla(liste):
       return liste[0]*liste[1]

kenarlar=[(3,4),(10,3),(5,6),(1,9)]
print(list(map(alanHesapla,kenarlar)))



