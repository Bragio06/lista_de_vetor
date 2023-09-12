lista = [1,2,3,4,5,6,7,8,9,10]
vazia = []

for n in range(0,10):
    vazia.append(n)
    
    if n % 2 == 0:
        vazia.remove(n)

print(vazia)

