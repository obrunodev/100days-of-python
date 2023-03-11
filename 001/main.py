# Introdução do app para o usuário.
print('Seja bem-vindo ao gerador de nomes para bandas!')

# Receber cidade natal.
cidade_natal = input('Digite o nome da sua cidade natal: ')

# Receber o nome do pet.
nome_pet = input('Digite o nome do seu pet: ')

# Gerar nome e apresentar para o cliente.
nome_gerado = '%s %s' % (cidade_natal, nome_pet)
print('O nome da sua banda é: %s' % (nome_gerado,))
