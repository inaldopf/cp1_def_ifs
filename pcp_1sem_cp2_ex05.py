def pode_aprovar(idade, renda, valor_emprestimo):
    if idade > 18 and valor_emprestimo <= renda * 20:
      return True
    else: 
       return False


def taxa_parcela(parcelas):
   if parcelas <= 6:
      return 0.05
   elif parcelas <= 12:
      return 0.08
   elif parcelas <= 24:
      return 0.1
   else:
      return 0


def parcelas_fixas(parcelas, valor_financiado, i):
   return  valor_financiado  * ((i * (1+i)^parcelas)/((1+i)^parcelas - 1))


def calcular_total(parcelas: int, valor):
   return parcelas * valor 


def calcular_juros(total, valor): 
   return total - valor
   

nome_cliente = input("Digite seu nome completo: ")
idade = int(input("Digite sua idade: ")) 
renda = float(input("Digite sua renda mensal: "))
valor_emprestimo = float(input("Digite o valor desejado do emprestimo: "))
parcelas = int(input("Digite o número de parcelas desejadas: "))


aprovado = pode_aprovar(idade, renda, valor_emprestimo)
if aprovado:
   i = taxa_parcela(parcelas)
   valor_parcela = parcelas_fixas(parcelas, valor_emprestimo, i)
   total_pago = calcular_total(parcelas, valor_parcela) 
   juros_pagos = calcular_juros(total_pago, valor_emprestimo)
   print(f"""O emprestimo foi aprovado, segue as informações abaixo:  
         Nome: ${nome_cliente}
         Valor Financiado: ${valor_emprestimo}
         Taxas de juro aplicadas: ${i}
         Valor da Parcela: ${valor_parcela}
         Valor total pago: ${total_pago}
         Total de juros pagos: ${juros_pagos}""")
else:
   print("O emprestimo não foi aprovado")





