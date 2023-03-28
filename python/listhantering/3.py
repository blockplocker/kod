
lista = [2, 3, 5, 6, 7, 6, 2, 6, 8, 7, 6, 4, 3]
print("En lista:", lista)

Första = []
Andra = []


x = len(lista)/2-1
n = 0
while n < x:
    tal = lista.pop(0)
    Första.append(tal)

    tal = lista.pop()
    Andra.append(tal)

    n += 1


print("Mitersta:", lista)
print("Första halvan:", Första)
print("Andra halvan:", Andra)
