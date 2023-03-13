# Skapar en lista med nummer
nummer = [1, 2, 3, 4, 5]

# Använder pop() för att ta bort och returnera det sista elementet i listan
sista_numret = nummer.pop()

# Skriver ut den listan och det borttagna numret
print("lista:", nummer)
print("Borttaget nummer:", sista_numret)

# Använder remove() för att ta bort den första av ett nummer från listan
nummer.remove(3)

# Skriver ut den modifierade listan
print("Modifierad lista:", nummer)

# Använder clear() för att ta bort alla element från listan
nummer.clear()

# Skriv ut den tomma listan
print("Tom lista:", nummer)