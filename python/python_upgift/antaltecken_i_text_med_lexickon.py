text = "araz svarar varför med därför den jävla horan"

lex = {}

n = 0
for x in text:
    if x in lex:
        lex[x] += 1
    else:
        lex[x] = 1
    n += 1

lex["antal_tecken"] = n

print(lex)

