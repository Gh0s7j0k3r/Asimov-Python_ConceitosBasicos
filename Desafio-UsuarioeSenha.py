'''Desafio-Crie um programa que:
Pede por um nome de usuário e uma senha.
Se ambos forem corretos, exibe uma mensagem de sucesso.
Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
quando o usuário está incorreto, e quando a senha está incorreta.
O usuário/senha "corretos" podem ser definidos como
variáveis dentro do próprio código.'''

senha_correta=123456
user_correto='miguel'
user=str(input('Digite o nome do usuário: '))
senha=int(input('Digite sua senha de 6 digitos: '))
if user == user_correto:
    if senha == senha_correta:
        print('Usuário e senha validados!')
    else:
        print('Usuário valido e senha invalida.')
elif user != user_correto:
    if senha == senha_correta:
        print('Usuário invalido e senha correta.')
    else:
        print('Usuário e senha invalida.')