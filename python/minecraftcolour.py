from random import randrange

def hex():
    hex_tecken = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_code = "#"
    for i in range(6):
        hex_code += hex_tecken[randrange(0, len(hex_tecken))]

    return hex_code


print(hex())
