'''Desafio - Crie um programa que:
Pede pelo seu nome e idade
Dá oi para você
Conta quantas letras seu nome possui
Fala quantos anos você terá daqui a 5 anos'''

nome=str(input("Informe seu nome: "))
idade=int(input("Informe sua idade: "))
print(f"Olá {nome}, Tudo bem com você?")
print(f"Seu nome possui {len(nome)} letras.")
print(f"Em 5 anos você vai ter {idade+5}")