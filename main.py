n1 = int(input("Cual es el numero cuantico principal: "))

while n1 >=7 :
    n1 = int(input("Ingresa bien el cuanto principal: "))
if n1 == 1:
    cuanto = 1
elif n1 == 2:
    cuanto = 2
elif n1 == 3:
    cuanto = 3
elif n1 == 4:
    cuanto = 4
elif n1 == 5:
    cuanto = 5
elif n1 == 6:
    cuanto = 6

momento_angular = []

while cuanto > 0:
    momento_angular.append(cuanto-1)
    cuanto = cuanto - 1

momento_magnetico = []
for i in momento_angular:
    for j in range(-i, i+1):
        momento_magnetico.append(j)
        

print("El numero cuantico principal es: ", n1)
print("El numero cuantico del momento angular es: ", momento_angular)
print("El numero cuantico del momento magnetico es: ", momento_magnetico)
