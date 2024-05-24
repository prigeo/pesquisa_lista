# lista
nomes = ['Dirce', 'Amanda', 'Eduardo', 'Francisco', 'Priscilla', 'José', 'Nazaré', 'Elizabeth', 'Barbara', 'Vitória', 'Gal', 'Serena', "Gaia", 'Romeu', 'Rodrigo']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# retorna o ´ndice do nome pesquisado
indice = nomes.index(nome)

# verifica se o nome está na lista ou não
try:
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista')