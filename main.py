### Validador de CPF ###

while True:
    cpf = input('Digite seu CPF (apenas numeros): ')
    new_cpf = cpf[:-2]              # Tira os dois ultimos digitos do CPF
    reverse = 10                    # Contador reverso
    total = 0

    if not cpf.isdigit():
        print('')
        print('Você deve digitar apenas numeros!')
        break
    # Loop do CPF
    for index in range(19):
        if index > 8:               # Primeiro indice que vai de 0 a 9
            index -= 9              # 9 primeiros digitos do CPF

        total += int(new_cpf[index]) * reverse  # Valor total da multiplicação do algoritmo, contador reverso e cpf

        reverse -= 1                # Diminui em 1 o contador reverso
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)
            if digit > 9:
                digit = 0
            total = 0               # Zera o total
            new_cpf += str(digit)   # Une/Liga o digito gerado com o novo CPF

    # Para não validar sequencias de cpf tipo, 111.111.111-11...
    sequence = new_cpf == str(new_cpf[0] * len(cpf))
    # Checagem final
    if cpf == new_cpf and not sequence:
        print('')
        print('CPf validado com sucesso!')
    else:
        print('')
        print('CPF não validado =(')
    
    # Opção de parar o loop infinito do CPF
    print('')
    sair = input('Deseja sair? Digite "s" ou "n": ')
    if sair == 's':
        print('')
        print('Saindo...')
        break