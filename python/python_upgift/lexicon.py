# Skapa ett lexikon med några nyckel-värde-par
person = {"namn": "Noa", "ålder": 17, "yrke": "Elev", "ort": "Nyköping"}

# 1. Visa hela lexikon
print(person)

# 2. Hämta en värde baserat på en nyckel
print(person["ålder"])

# 3. Lägg till ett nyt nyckel-värde-par
person["favoritfärg"] = "blå"
print(person)

# 4. Uppdatera ett befintligt värde
person["yrke"] = "programmerare"
print(person)

# 5. Ta bort ett nyckel-värde-par
del person["ort"]
print(person)

# 6. Visa alla nycklar i lexikon
print(person.keys())

# 7. Visa alla värden i lexikon
print(person.values())

# 8. Visa alla nyckel-värde-par i en loop
for nyckel, värde in person.items():
    print(nyckel, värde)

# 9. Kontrollera om en nyckel finns i lexikon
if "namn" in person:
    print("Ja, 'namn' finns i lexikon.")

# 10. Kopiera en lexikon
person2 = person.copy()
print(person2)

# 11. Hämta ett värde baserat på en nyckel, med fallback om nyckel inte finns
print(person.get("lön", 0)) # Returnerar 0 eftersom "lön" inte finns

# 12. Uppdatera ett lexikon med ett annat lexikon
ny_info = {"yrke": "Spelutveklare", "hobby": "Spela"}
person.update(ny_info)
print(person)

# 13. Skapa ett lexikon från två separata listor med nycklar och värden
nycklar = ["a", "b", "c"]
värden = [1, 2, 3]
lexikon_från_lista = dict(zip(nycklar, värde))
print(lexikon_från_lista)

# 14. Rensa alla nyckel-värde-par från lexikon
person.clear()
print(person)