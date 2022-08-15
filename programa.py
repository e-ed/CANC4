while True:
    print("1) Converter da base 10 para outra base")
    print("2) Converter de outra base para a base 10")
    print("999) Sair")
    novoNumero = []
    numeroConvertido = ""
    escolha = int(input())
    if escolha == 1:
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

        
        print(numeroOriginal, end='\N{SUBSCRIPT ONE}\N{SUBSCRIPT ZERO}')
        
        print(f" = {numeroConvertido} na base {base}")
    elif escolha == 2:
        numeroConvertido = 0
        numero = int(input("Numero a ser convertido: "))
        base = int(input("Base do numero: "))

        for n in str(numero):
            novoNumero.append(n)
        
        for i in range(len(novoNumero)):
            resultado = pow(base, i) * int(novoNumero[len(novoNumero) - i - 1])
            numeroConvertido += resultado

        print(numeroConvertido)
    elif escolha == 999:
        break