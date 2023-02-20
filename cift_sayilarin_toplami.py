#******************Çift Sayıların Toplamı******************#
from functools import reduce
sayilar=list(range(0,15))
cift_sayilar=list(filter(lambda x:x%2==0,sayilar))
toplam=reduce(lambda x,y:x+y,cift_sayilar)
print(toplam)