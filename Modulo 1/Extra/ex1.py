nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

except:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado. Criando agora...")

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("Arquivo criado automaticamente.\nVocê pode editar este conteúdo depois.")

    print("Arquivo criado com sucesso!")



# with faz o gerenciamento do arquivo
# open é o nome da funçao qeu rece dois parametros
# parametros do open a ,w ,r 


