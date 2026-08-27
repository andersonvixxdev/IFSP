
//Programa: Este é o envio do desafio intermediário desta semana: o conversor de temperatura (Celsius para Fahrenheit, com o bônus de também calcular em Kelvin).
//Autor: Anderson Roberto Martins - ID: CV3132765
//Instituição: IFSP - Instituto Federal de São Paulo
//Atividade: Semana 3 - Exercício de Entrada e Saída de Dados


celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"Temperatura em Fahrenheit: {fahrenheit:.2f} °F")
print(f"Temperatura em Kelvin: {kelvin:.2f} K")