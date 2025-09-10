nome= input('digite o nome')
email=input('digite o email')
telefone=input('digite o telefone')


with open('cadastro.txt', 'a')  as arquivo:
    arquivo.write('seu nome :'+ nome + 'seu email:'+email + 'seu telefone'+telefone)

 