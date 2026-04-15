def converte_toneladas(toneladas: int):
    return toneladas * 1000


def preco_por_codigo(codigo: int, kg: float):
    if codigo >= 10 and codigo <= 20:
        return kg * 100
    elif codigo >= 21 and codigo <= 30:
        return kg * 250
    elif codigo >= 31 and codigo <= 40:
        return kg * 340
    else:
        return 0
    

def imposto_por_estado(estado: int, preco: float):
    if estado == 1:
        return preco * 0.35
    elif estado == 2:
        return preco * 0.25
    elif estado == 3:
        return preco * 0.15
    elif estado == 4:
        return preco * 0.05
    else:
        return 0


estado = int(input("Digite o estado de origem da carga do caminhão (1 a 5): "))
toneladas = float(input("Digite o peso da carga do caminhão em toneladas: "))
codigo = int(input('Digite o código da carga do caminhão (10 a 40): '))

peso = converte_toneladas(toneladas)
preco = preco_por_codigo(codigo, peso)
imposto = imposto_por_estado(estado, preco)
preco_total = preco + imposto

print(f"""
O peso da carga é: {peso}kg;
O preço da carga, antes dos impostos, é: R${preco:.2f};
O valor do imposto aplicado foi de: R${imposto:.2f};
O valor total da carga é de: R${preco_total:2f}
""")


