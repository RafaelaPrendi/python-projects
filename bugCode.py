'''
1. Supozoni se kemi funksionin e perkufizuar me poshte.

# Llogarit prodhimin e te gjithe numrave qe permbahen ne liste
def prodhimi(A):
    p = A[0]
    # kujtoni menyren sesi mund te perftojme 'segmente' nga lista
    # (quajtur ndryshe: slicing. Lexoni me teper ketu: https://www.learnbyexample.org/python-list-slicing/)
    for numer in A[1:]:
        p *= numer # shkurt per p = p * numer

    return p

# Pra:
#   prodhimi([1,2,3]) -> 6
#   prodhimi([1,2]) -> 2
#   prodhimi([1,2, 0]) -> 0

# Supozoni me tej se kemi keto variabla, te perkufizuara ne kete menyre:
numri0, numri1, numri2 = 1, 2, 3
numri3 = 0,

# Te cilat i vendosim ne nje liste
lista_fillestare = [numri0, numri1, numri2, numri3]

# Dhe i rendisim elementet e listes mbrapsh
lista_perfundimtare = list(reversed(lista_fillestare))

# Duke pare shembujt e meparshem, mendimi i pare qe duhet te keni eshte qe ky program do printoje 0
# Nese e ekzekutoni kete script, do te vini re qe printimi kthen nje vlere te cuditshme.
print(prodhimi(lista_perfundimtare))

# Kerkesat:
#   1. Gjeni, dhe shpjegoni pse output eshte ky qe shihni. (Per kete, vini re c'ndodh nese ekzekutoni kete komande: 'print([1] * 2)')
#   2. _Pa ndryshuar funksionin_. rregullojeni skriptin qe te prodhoje rezultatin '0' per kete rast. (mjafton te ndryshoni vetem 1 variabel)
'''
def prodhimi(A):
    p = A[0]
    for numer in A[1:]:
        p *= numer # p = p*numer

    return p

numri0, numri1, numri2 = 1, 2, 3
numri3 = 0,
lista_fillestare = [numri0, numri1, numri2, numri3]
lista_perfundimtare = list(reversed(lista_fillestare))
print(lista_fillestare)
print(lista_perfundimtare)

print(prodhimi(lista_perfundimtare))
print(prodhimi(lista_fillestare))
print(type(numri3))
print([1] * 2)
''' Numri 3 eshte inicializuar si tuple pasi ka nje presje ne fund, dhe eshte e dhene e pandryshueshme (immutable). Lista perfundimtare ka permbajtjen [(0,), 3, 2, 1],
 me numri3 ne fillim. Kur exe funksioni prodhimi , fillimisht p = (0, ) dhe cdo element tjeter i listes do shumezohet me p qe eshte tuple, pra do kryhet (0, )*numer  
  qe do shtoje 0 ne tuple aq here sa eshte numri. Prandaj si rezultat eshte nje tuple me 1 + 2 + 3 = 6 zero. Per te marre vetem nje zero si rezultat numri3 duhet te inicializohet si int
  numri3 = 0'''
