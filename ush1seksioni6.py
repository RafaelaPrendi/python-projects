'''
1. Supozojme se jane dhene keto 2 funksione, qe dekorojne funksionin "f".
- Ekzekutoni programin dhe vini re vleren qe printohet.
- Nderroni rrjeshtat 164 me 165. Pra, rradha e dekoratoreve tani duhet te jete:
  -   @decorator2
  -   @decorator1
  -   def f ...

- Shpjegoni me detaje si llogaritet vlera qe printohet, pse ndryshon kur i nderrojme vendet dekoratoreve, dhe si
eshte rradha e aplikimit te funksioneve qe cojne ne printimin e vleres perfundimtare.

def decorator1(f):
  def inner(x):
    return f(x + 1)
  return inner

def decorator2(f):
  def inner(x):
    return f(x ** 2)
  return inner

@decorator1
@decorator2
def f(x): # funksioni qe dekorohet, thjesht kthen argumentin qe merr
  return x

print(f(2))

'''
def decorator1(f):
  def inner(x):
    return f(x + 1)
  return inner

def decorator2(f):
  def inner(x):
    return f(x ** 2)
  return inner

@decorator1 # f = decorator1(f)
@decorator2 # f = decorator2(f)
def f(x): # funksioni qe dekorohet, thjesht kthen argumentin qe merr
  return x
print("Rasti 1")
print(f(2))

'''
ZGJIDHJE
dekoratori i pare  merr si vlere funksionin f , kalon ne funksionin e brendshem i cili do marri si parameter vleren x = 2 
dhe kthen vleren qe do kthente funksioni f me parameter x + 1 pra f(3) => do ktheje 3.
dekoratori i dyte  merr si vlere funksionin f , kalon ne funksionin e brendshem i cili do marri si parameter vleren x = 2 
dhe kthen vleren qe do kthente funksioni f me parameter x ne katror pra f(4) => do ktheje 4

deklarimi :
@decorator2
def f(x): 
  return x
eshte i njejte me f = decorator2(f)
kur thirren dy dekoratoret njeri pas tjetrit , dekoratori i jashtem do te dekoroje funksionin e dale si produkt i dekoratorit te brendshem. 
pra ne rastin e pare dekoratori1 shkruet ndryshe si : f = decorator1(decorator2(f)). Prandaj nese ndryshohet rradha e dekorimit ,ndryshon rezultati.
Ne rastin e dyte do te shkruhej ndryshe : f = decorator2(decorator1(f)). Meqe dekoratoret e ndryshojne funksionin f ne menyre te ndryshme, ndryshimi
i rradhes ben qe rezultati te jete ndryshe.

NE RASTIN E PARE:
    @decorator1
    @decorator2
    def f(x): 
      return x
    
    print(f(2))
Ne fillim do exe dekoratori2, i cili therret dekoratorin 1 , i cili  merr si vlere funksionin f , kalon ne funksionin e brendshem i cili do marri si parameter vleren x = 2 
dhe kthen vleren qe do kthente funksioni f me parameter x + 1 pra f(2) => do ktheje 3.Pra tani x = 3. me pas do te exe funksioni inner i dekoratorit 2 
i cili do marri si parameter vleren x = 3 dhe kthen vleren qe do kthente funksioni f me parameter x ne katror pra f(3) => do ktheje 9

NE RASTIN E DYTE:
     @decorator2
     @decorator1
        def f(x): 
          return x
        
        print(f(2))
Ne fillim do exe dekoratori1, i cili therret dekoratorin 2 , i cili  merr si vlere funksionin f , kalon ne funksionin e brendshem i cili do marri si parameter vleren x = 2 
dhe kthen vleren qe do kthente funksioni f me parameter x **2 pra f(2) => do ktheje 4.Pra tani x = 4. me pas do te exe funksioni inner i dekoratorit1 
i cili do marri si parameter vleren x = 4 dhe kthen vleren qe do kthente funksioni f me parameter x + 1 pra f(4) => do ktheje 5.




'''
