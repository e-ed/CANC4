def converterBase10ParaOutraBase():
        novoNumero = []
        numeroConvertido = ""
        numero = int(input("Numero na base 10 a ser convertido: "))
        numeroOriginal = numero
        base = int(input("Nova base: "))
        
        
        while (numero > 0):
            resto = int(numero % base)
            novoNumero.append(resto)
            numero = int(numero/ base)

        novoNumero.reverse()
        for numero in novoNumero:
            numeroConvertido+=str(numero)

        resultados = {
            "numeroOriginal": numeroOriginal, 
            "numeroConvertido": numeroConvertido, 
            "base": base
        }

        return resultados

def converterOutraBaseParaBase10(numero, base):
        novoNumero = []
        numeroConvertido = 0

        for n in str(numero):
            novoNumero.append(n)
        
        for i in range(len(novoNumero)):
            resultado = pow(base, i) * int(novoNumero[len(novoNumero) - i - 1])
            numeroConvertido += resultado


        resultados = {
            "numeroOriginal": numero, 
            "numeroConvertido": numeroConvertido, 
            "base": base
        }

        return resultados

while True:
    print("1) Converter da base 10 para outra base")
    print("2) Converter de outra base para a base 10")
    print("999) Sair")
    escolha = int(input())
    if escolha == 1:
        dicionarioResultados = converterBase10ParaOutraBase()
        print(dicionarioResultados.get("numeroOriginal"), end='\N{SUBSCRIPT ONE}\N{SUBSCRIPT ZERO}')
        print(" = "+ str(dicionarioResultados.get("numeroConvertido")) +  " na base "+str(dicionarioResultados.get("base")))
        print("\n")
    elif escolha == 2:
        numero = int(input("Numero a ser convertido: "))
        base = int(input("Base do numero: "))
        dicionarioResultados = converterOutraBaseParaBase10(numero, base)
        print(str(dicionarioResultados.get("numeroOriginal"))+" na base " + str(dicionarioResultados.get("base")) + " = ", end='')
        print(str(dicionarioResultados.get("numeroConvertido")), end='\N{SUBSCRIPT ONE}\N{SUBSCRIPT ZERO}\n')
        print("\n")
    elif escolha == 999:
        break


