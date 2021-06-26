# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

cadastro = dict()
lista = list()
mulher = list()
pessoas = 0
soma_idade = 0

while True:
    cadastro['nome']= str(input('nome: ')).title()
    pessoas += 1
    cadastro['sexo_biologico'] = str(input('sexo[F/M]: ')).upper().strip()[0]
    while cadastro['sexo_biologico'] not in 'FM':
        cadastro['sexo_biologico'] = str(input('sexo[F/M]: ')).upper().strip()[0]
    cadastro['idade'] = int(input('idade: '))
    if cadastro['sexo_biologico'] == 'F':
        mulher.append(cadastro.copy())
    lista.append(cadastro.copy())
    soma_idade += cadastro['idade']

    continuar = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    while continuar not in 'SN':  
        continuar = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        break 

media = soma_idade / pessoas 

maior_media = list()
for n in lista:
    if n['idade'] > media:
        maior_media.append(n['idade'])

print(f'''
 A) Quantas pessoas estão cadastradas: {pessoas}.
 B) A média da idade: {media}.
 C) Uma lista com as mulheres: {mulher}.
 D) Uma lista com as idades que estão acima da média: {maior_media}.
''')

