nome = input('digite seu nome:' )
peso = float(input('digite seu peso em quilogramas:'))
altura = float(input('digite sua altura em metros:'))

imc = peso / (altura * altura)
print('seu imc é igual a:', imc)

if imc <=18.5:
 print('o paciente (nome) esta abaixo do peso',imc)

elif imc >=18.5 and <=24.9: 
  print('o paciente (nome) tem o peso normal',imc)

elif imc >=25.0 and <=29.9:
  print('o paciente (nome) tem sobrepeso',imc)

elif imc >=30.0 and <=34.9:
  print('o paciente (nome) tem obesidade grau 1',imc)

elif imc >=35.0 and <=39.9:
  print('o paciente (nome) tem obesidade grau 2',imc)

elif imc >=40.0:
  print('o paciente (nome) tem obesidade grau 3',imc)



