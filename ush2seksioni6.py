from time import sleep

def cache_results(f): # dekoratori
  cache = {} #dict data structure
  def inner(a, b):
    if b > a:
      temp = b
      b = a
      a = temp
    key = (a, b) # formoj nje tuple per key
    if key not in cache:
      value = f(a, b)
      cache[key] = value

    return cache[key]
  return inner

@cache_results
def lazy_add(a, b):
  sleep(5)
  return a + b

@cache_results
def lazy_mul(a, b):
  sleep(5)
  return a * b

print(lazy_add(1, 2)) # do haje 5 sekonda
print(lazy_add(2, 1)) # do ekzekutohet menjehere
print(lazy_add(1, 2)) # do ekzekutohet menjehere
print("-----------")
print(lazy_mul(1, 2)) # do haje 5 sekonda
print(lazy_mul(2, 1)) # do ekzekutohet menjehere
print(lazy_mul(1, 2)) # do ekzekutohet menjehere

''' MENYRE TJETER PER IMPLEMENTIMIN E DEKORATORIT'''
'''
  def cache_results(func):
    cache = {}
    def inner(a, b):
        if a not in cache and b not in cache:
            value = func(a, b)
            cache[a] = value
            cache[b] = value

        return (str(cache[a]) + "\n" + str(cache[b]))
    return inner

'''
