def calcular_horas_extras(salario_base, horas):

    valor_extra = salario_base * 0.015
    valor_final = valor_extra * horas
    return valor_final

def calcular_bonus(cargo, recebeu_bonus: str):
    
    if recebeu_bonus.lower() == 's':
        match cargo:
            case 1:
                valor_bonus = 1000
            
            case 2:
                valor_bonus = 500
            
            case 3:
                valor_bonus = 300
            
            case 4:
                valor_bonus = 100
    else:
        valor_bonus = 0
    return valor_bonus


def calcular_descontos_faltas(salario_base, faltas):
    desonto = salario_base * 0.02

    desconto_final = desonto * faltas

    return desconto_final






nome = str(input('Nome:\n'))
cargo = int(input('Cargo:\n'))
salario = float(input('Salario:\n'))
extra = float(input('Horas extras trabalhadas(1h e 30min = 1.5):\n'))
falta = int(input('Quantidade de faltas:\n'))
bonus = str(input('Recebeu Bonus?\n'))




total_bonus = calcular_horas_extras(salario, extra) + calcular_bonus(cargo, bonus)
total_descontos = calcular_descontos_faltas(salario, falta)
salario_final = (salario - total_descontos) + total_bonus




print(f'Salario Bruto: {salario}')
print(f'Total de acréscimos: {total_bonus}')
print(f'Total de descontos: {total_descontos}')
print(f'Salario final: {salario_final}')