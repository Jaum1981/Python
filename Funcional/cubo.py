cubo = lambda x: x**3

L=[1,2,3,4,5]

def cuboLista(L):
    return list(map(cubo,L))

print(cuboLista(L))
