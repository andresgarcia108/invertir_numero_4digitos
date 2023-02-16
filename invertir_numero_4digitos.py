#Programa para invertir un número de 4 digitos

print ("----------------------------------------")
print ("------------Invertir número-------------")
print ("----------------------------------------")

#input

n= int(input("Digite un número de 4 digitos:"))

#processing
d1=((n%10)*1000)
pe=((n//10))
d2=((pe%10)*100)
pe=((pe//10))
d3=((pe%10)*10)
d4=(pe//10)
ni=(d1+d2+d3+d4)


#output
print("----------------------------------")
print("------------RESULTADOS------------")
print("----------------------------------")

print("Número invertido: "+ str(ni))

