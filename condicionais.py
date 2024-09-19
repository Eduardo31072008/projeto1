'''
entrada = input(' Você quer "entrar" ou "sair"?  ')

if entrada == 'entrar':
    print("você entrou no sistema")
elif entrada == 'sair':
    print("você saiu do sistema")

else:
    print("você não digitou nem entrar e nem sair.")
    '''


'''
condicao1 = False
condicao2 = False
condicao3 = False
if condicao1:
    print('Este é o codigo do if')
elif condicao2:
    print('segunda condição')
else:
    print('else do primeiro if')

if 10 == 10:
    print('outro if')


print("fora do if")
'''



primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('digite o segundo valor: ')

if primeiro_valor < segundo_valor:
    print(f'o {primeiro_valor=} é menor que o {segundo_valor=}')

elif primeiro_valor > segundo_valor:
    print(f'o {primeiro_valor=} é maior que o {segundo_valor=}')

elif primeiro_valor == segundo_valor:
    print('os dois valores são iguais.')
    
elif primeiro_valor != segundo_valor:
    print('os valores são diferentes')

else:
    print('você não digitou nenhum número')   
