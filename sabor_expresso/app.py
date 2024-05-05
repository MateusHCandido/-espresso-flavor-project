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

def chosen_option():
    try:
        chosed_option =  int(input('Escolha uma opção: '))
    
        if chosed_option == 1:
            register_new_restaurant()
            back_to_menu()
        elif chosed_option == 2:
            list_restaurants(restaurants)
            back_to_menu()
        elif chosed_option == 3:
            print('Ativar restaurante')
            active_restaurant(restaurants)
            back_to_menu()
        elif chosed_option == 4:

            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()

def invalid_option():
    print('opção inválida\n')    
    back_to_menu()

def register_new_restaurant():
        os.system('cls')
        print('CADASTRO DE NOVOS RESTAURANTES\n')

        restaurant_name = input('Digite o nome do restaurante: ')
        restaurant_category = input('Insira a categoria do restaurnte: ')
        restaurant_status = False

        restaurant = {'name': restaurant_name, 'category': restaurant_category, 'status': restaurant_status}

        restaurants.append(restaurant)
        print(f'O nome do restaurante cadastro é {restaurant_name}\n')

def list_restaurants(restaurants):
    print('Listar restaurantes\n')

    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_status = restaurant['status']

        print(f'NOME: {restaurant_name}   CATEGORIA: {restaurant_category}   ATIVO? {restaurant_status}\n')

def active_restaurant(restaurants):
    print(f'Listando restaurantes inativos: \n')

    for index, restaurant in enumerate(restaurants):
        if restaurant['status'] is False:
            restaurant_name = restaurant['name']
            restaurant_category = restaurant['category']
            restaurant_status = restaurant['status']

            print(f'{index} -  NOME: {restaurant_name} CATEGORIA: {restaurant_category} ATIVO? {restaurant_status}\n')
        
    chosen_restaraunt = int(input('Selecione o número do restaurante para ativar: '))

    restaurants[chosen_restaraunt]['status'] = True

def finish_app():
    os.system('cls')
    print('finalizando app\n')

def main():
    show_app_name()
    show_options()
    chosen_option()

def back_to_menu():
    input('Digite alguma tecla para voltar para o menu principal: ')
    os.system('cls')

    show_options()
    chosen_option()



if __name__ == '__main__':
    main()