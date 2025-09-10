nome = input ('digite o nome:')
telefone=input('digite o seu telefone:')
email= input ('digite o e-mail:')

with open ('contatos.txt', 'a') as arquivo:
    arquivo.write(nome +  '|' + telefone+ email)


