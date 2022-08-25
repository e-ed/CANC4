from unittest import result


def converterBase10ParaOutraBase(numero, base):
        if numero == 0:
            resultados = {
            "numeroOriginal": numero, 
            "numeroConvertido": 0, 
            "base": base
            }
            return resultados

        novoNumero = []
        numeroConvertido = ""
        numeroOriginal = numero
  
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
        if numero == 0:
            resultados = {
            "numeroOriginal": numero, 
            "numeroConvertido": 0, 
            "base": base
            }
            return resultados
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

def operacoesOutraBase(numero1, numero2, base, operacao):
    numero1Convertido = converterOutraBaseParaBase10(numero1, base)
    numero2Convertido = converterOutraBaseParaBase10(numero2, base)
    resultado = 0
    if operacao == 0:
        resultado = int(numero1Convertido.get("numeroConvertido")) + int(numero2Convertido.get("numeroConvertido"))
    else:
        resultado = int(numero1Convertido.get("numeroConvertido")) - int(numero2Convertido.get("numeroConvertido"))

    print(resultado)
    resultado = converterBase10ParaOutraBase(resultado, base).get("numeroConvertido")

    resultados = {
            "numero1Original": numero1, 
            "numero2Original": numero2, 
            "resultado": resultado, 
            "base": base
    }

    if operacao == 0:
        resultados["operacao"] = "+"
    else:
        resultados["operacao"] = "-"
    return resultados


while True:
    print("1) Converter da base 10 para outra base")
    print("2) Converter de outra base para a base 10")
    print("3) Adicionar/subtrair em outra base")
    print("999) Sair")
    escolha = int(input())
    if escolha == 1:
        numero = int(input("Numero a ser convertido: "))
        base = int(input("Base do numero: "))
        dicionarioResultados = converterBase10ParaOutraBase(numero, base)
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
    elif escolha == 3:
        numero1 = int(input("Numero 1: "))
        numero2 = int(input("Numero 2: "))
        base = int(input("Base dos numeros: "))
        operacao = int(input("0) Somar \n1) Subtrair"))
        dicionarioResultados = operacoesOutraBase(numero1, numero2, base, operacao)
        print(str(dicionarioResultados.get("numero1Original")) + str(dicionarioResultados.get("operacao")) + str(dicionarioResultados.get("numero2Original")) + " = " + str(dicionarioResultados.get("resultado")))

    elif escolha == 999:
        break

