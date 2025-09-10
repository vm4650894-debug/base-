
try:

    with open ('arquivo.txt' , 'r') as info:
        print (info.read())

except:
    print ('nao foi possivel fazer uma leitura, mas irei criar agora para voce')     
    with open ('arquivo.txt' , 'w') as info:
        info.write ('arquivo criado com sucesso')


