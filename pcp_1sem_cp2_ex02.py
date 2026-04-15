def ordena_lista(lista):
    tamanho = len(lista)-1
    for sla in range(len(lista)):
        for k in range(len(lista)):
            cont = 0
 
            for i in lista[:k] + lista[k+1:]:
                if lista[k] >= i:
                    cont+=1
            val = lista[k]
 
            lista.pop(k)
            lista.insert(tamanho-cont, val)
 
    return lista
val_1 = float(input('Insira o valor do lado 1: '))
val_2 = float(input('Insira o valor do lado 2: '))
val_3 = float(input('Insira o valor do lado 3: '))
valores = [val_1, val_2, val_3]
valores = ordena_lista(valores)
valor_A = valores[0]
valor_B = valores[1]
valor_C = valores[2]
 

if valor_A >= valor_B + valor_C:
    print("NAO FORMA TRIANGULO")
else:
    lados = sorted([valor_A, valor_B, valor_C], reverse=True)
    valor_A, valor_B, valor_C = lados
 
    if valor_A**2 == valor_B**2 + valor_C**2:
        print("TRIANGULO RETANGULO")
    elif valor_A**2 > valor_B**2 + valor_C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO valor_ACUTANGULO")
 
    if valor_A == valor_B == valor_C:
        print("TRIANGULO EQUILATERO")
    elif valor_A == valor_B or valor_A == valor_C or valor_B == valor_C:
        print("TRIANGULO ISOSCELES")