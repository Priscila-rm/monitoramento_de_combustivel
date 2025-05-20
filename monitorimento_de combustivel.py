distancia = float(input("qual é a distancia percorrida?: "))
combustivel = float(input("quanto de combustivel foi gasto?: "))


consumo_medio = distancia / combustivel 


if consumo_medio < 8:
    print (" Alto consumo 🚨")
elif 8> consumo_medio <12:
    print ("Consumo moderado ⚠️")
else:
    print( "Econômico! 🚗💨")

print(consumo_medio)