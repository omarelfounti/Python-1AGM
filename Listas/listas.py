temperatura = [-1, 8, 4, 5]
juegos = ["fc25", 
          "pacman", 
          "GTAV", 
          "WarThunder"]

print(juegos[1])
print(juegos[5])
print(juegos[3])
print(juegos[2])
print(juegos[0 : 2])


MyTradringPrices = [2000, 1500, 5220, 2110, 4522, 2522, 2555]
MyTradringPrices2 = [2043, 1504, 5440, 2440, 4422, 2622, 3555]

print(len(MyTradringPrices))
print(max(MyTradringPrices))
print(min(MyTradringPrices))
print(max(MyTradringPrices2))
print(min(MyTradringPrices2))
print(len(MyTradringPrices2))

minValor = MyTradringPrices[0]
for i in MyTradringPrices:
    if i < minValor:
        minValor = i

print("Mínimo:", minValor)

maxValor = MyTradringPrices[0]
for i in MyTradringPrices:
    if i > maxValor:
        maxValor = i

print("Máximo:", maxValor)



















