# # Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só


classe = list()

for i in range(15): #para rodar 15x
    aluno = dict()
    aluno['nome'] = str (input('Digite o nome: '))
    aluno['notas'] = list()
    media = 0
    for j in range(15):
        nota = float(input('Digite a nota: ')) 
        aluno['notas'].append(nota)
        media += (nota/5)                  
    aluno['media'] = media      
    if aluno['media'] >= 7:
        aluno['situacao'] = 'aprovado'
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    classe.append(aluno)

for aluno in classe:
    print(f'''O {aluno['nome']}  teve as seguintes notas {aluno['notas']}, com média {aluno['media']:.2f}, e situação {aluno['situacao']}
''')


# Outra forma

# from random import uniform
# from names import get_first_name  #Pega nomes aleatorios, não precisa do input 

# classe = list()

# for i in range(15):
#     aluno = dict()
#     aluno['nome'] = get_first_name()
#     aluno['notas'] = list()
#     media = 0
#     for j in range(5):
#         nota =  round(uniform(0, 10), 2)
#         aluno['notas'].append(nota)
#         media += (nota/5)                  
#     aluno['media'] = media      
#     if aluno['media'] >= 7:
#         aluno['situacao'] = 'aprovado'
#     elif 5 <= aluno['media'] < 7:
#         aluno['situacao'] = 'recuperação'
#     else:
#         aluno['situacao'] = 'reprovado'
#     classe.append(aluno)

# for aluno in classe:
#     print(f'''O {aluno['nome']}  teve as seguintes notas {aluno['notas']}, com média {aluno['media']:.2f}, e situação {aluno['situacao']}''')