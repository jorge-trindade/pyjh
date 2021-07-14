'''
# strings formatadas facilitam a leitura e facilitam a inserção de varíaveis, melhorando a leitura
'''

nome = 'Bill'
sobrenome = 'Gates'
profissao = 'Programador'

'''
# strings não formatadas 
'''
texto =  'O ' + nome + ' ' + sobrenome + ' e um excelente ' + '[' + profissao + ']'

print(texto)

'''
# abaixo um ex com strings formatadas diminuindo a quantidade de texto no code, sem precisar ficar colocando espaçõs
'''
texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'

print(texto2)