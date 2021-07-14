

mensagem = '     Eu adoro comida Caseira'
#index      0123456789
#normal
print(mensagem)
'''
#garantir que um input tenha somente uma
regra através de metordos para strings
assim fica mais fácil quando um user inputar algo
o formato do texto ficará da forma que você quer
'''
#tudo em letra minúscula
print(mensagem.lower())

#tudo em letra maiúscula
print(mensagem.upper())

#coloca a primeira letra maiúscula
print(mensagem.capitalize())

#pesquisa uma letra por posição através de um index na frase, ex c está na posição 9 sem espaço com espaço tem 14
print(mensagem.find('c'))

#replace substitui a letra por outro que vem após a virgula
print(mensagem.replace('a','e'))

#replace substitui a palavra por outro que vem após a virgula
print(mensagem.replace('Caseira','de rua'))

#strip remove espaçõs antes do primeiro caracter
print(mensagem.strip())