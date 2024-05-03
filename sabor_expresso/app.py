import os

restaurants = []

def show_app_name():
    print("""
                 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def show_options():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finish_app():
    os.system('cls')
    print('finalziando app\n')

def invalid_option():
    print('opção inválida\n')    
    input('Digite alguma tecla para voltar para o menu principal: ')
    
    os.system('cls')

    show_options()
    chosen_option()

def register_new_restaurant():
        os.system('cls')
        print('CADASTRO DE NOVOS RESTAURANTES\n')

        restaurant_name = input('Digite o nome do restaurante: ')
        restaurants.append(restaurants)
        print(f'O nome do restaurante cadastro é {restaurant_name}\n')

        input('digite uma tecla para voltar para o menu principal\n')

        main()

def chosen_option():
    try:
        chosed_option =  int(input('Escolha uma opção: '))
    
        if chosed_option == 1:
            register_new_restaurant()
        elif chosed_option == 2:
            print('Listar restaurantes')
        elif chosed_option == 3:
            print('Ativar restaurante')
        elif chosed_option == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()



    


def main():
    show_app_name()
    show_options()
    chosen_option()

if __name__ == '__main__':
    main()