def calcular_horas_extras(salario_base, horas):
    valor_extra = salario_base * 0.015
    valor_final = valor_extra * horas
    return valor_final


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() == 's':
        match cargo:
            case 1:
                return 1000            
            case 2:
                return 500            
            case 3:
                return 300            
            case 4:
                return 100
    else:
        return 0


def calcular_descontos_faltas(salario_base, faltas):
    desconto = salario_base * 0.02
    desconto_final = desconto * faltas
    return desconto_final


nome = str(input('Digite seu nome:\n'))
cargo = int(input('Digite seu cargo (1 a 4):\n'))
salario = float(input('Digite seu salário:\n'))
extra = float(input('Horas extras trabalhadas (1h e 30min = 1.5):\n'))
falta = int(input('Quantidade de faltas:\n'))
bonus = str(input('Recebeu Bonus?\n'))


total_bonus = calcular_horas_extras(salario, extra) + calcular_bonus(cargo, bonus)
total_descontos = calcular_descontos_faltas(salario, falta)
salario_final = (salario - total_descontos) + total_bonus


print(f'Salario Bruto: R$ {salario:.2f}')
print(f'Total de acréscimos: R$ {total_bonus:.2f}')
print(f'Total de descontos: R$ {total_descontos:.2f}')
print(f'Salario final: R$ {salario_final:.2f}')