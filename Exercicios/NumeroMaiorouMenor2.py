# Solicita 2 números ao usuario.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Compara os números e da uma resposta apropriada.
if num1 == num2:
    print("Os números são iguais!")

elif num1 > num2:
    print(f"O primeiro número: ({num1})é o maior!")

else:
    print(f"O segundo número: ({num2}) é o maior!")