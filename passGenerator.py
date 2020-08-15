'''
# ------------------------------------------------------
2. Implementoni nje funksion 'def gjenero_password(): ...' qe kthen stringje, dhe ka keto veti:
    - sa here qe therritet, gjeneron nje password te ndryshem (idealisht, sepse mund te qelloje qe gjenerohet dy here i njejti password).
    - gjatesia e stringjeve te gjeneruar eshte 8.

Pra:
gjenero_password() -> '#avdExy0'
gjenero_password() -> '!u#1_?-B'
gjenero_password() -> '%43xKjIR'

Nje pakete qe do t'ju duhet per kete ushtrim eshte paketa 'random', qe mund ta importoni duke ekzekutuar ne
skriptin tuaj komanden 'import random'. (Mund te lexoni me shume ketu: https://docs.python.org/3/library/random.html)

Kjo pakete permban disa funksione, mes te cilave:

random.choice(<nje liste me elemente>).

Perdorni help(random.choice) per te kuptuar me mire se c'ben ky funksion, si dhe kujtoni operatoret qe kemi pare ne seancat e meparshme per listat dhe stringjet.
'''
import random
import string
def gjenero_password():
    allstring = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(0, 8):
        password += random.choice(allstring)
    return password

# print(gjenero_password())
# print(gjenero_password())
#
# help(random.choice)
def add(increment):
    def inner(arg):
        return arg + increment
    return inner
shto1 = add(1)
print(shto1(4))

