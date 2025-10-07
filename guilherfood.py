import os

# Database dos restaurantes cadastrados
registered_restaurants = [
    {'nome': 'Guilherante', 'tipo': 'Português', 'ativo': True},
    {'nome': 'Gui-shi-min', 'tipo': 'Vietnamita', 'ativo': False},
    {'nome': 'OolaVea', 'tipo': 'Havaiano', 'ativo': True}
]

def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_program_name():
    """Exibe o nome do programa em ASCII art"""
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ██████  ██    ██ ██ ██      ██   ██ ███████ ██████     ║
║  ██       ██    ██ ██ ██      ██   ██ ██      ██   ██    ║
║  ██   ███ ██    ██ ██ ██      ███████ █████   ██████     ║
║  ██    ██ ██    ██ ██ ██      ██   ██ ██      ██   ██    ║
║   ██████   ██████  ██ ███████ ██   ██ ███████ ██   ██    ║
║                                                          ║
║  ███████  ██████   ██████  ██████                        ║
║  ██      ██    ██ ██    ██ ██   ██                       ║
║  █████   ██    ██ ██    ██ ██   ██                       ║
║  ██      ██    ██ ██    ██ ██   ██                       ║
║  ██       ██████   ██████  ██████                        ║
║                                                          ║
║       SISTEMA DE GERENCIAMENTO DE RESTAURANTES           ║
╚══════════════════════════════════════════════════════════╝
""")

def display_options():
    '''Exibe o menu principal'''
    print('┌─────────────────────────────────────────┐')
    print('│         MENU PRINCIPAL                  │')
    print('├─────────────────────────────────────────┤')
    print('│  1. Cadastrar restaurante               │')
    print('│  2. Listar restaurantes                 │')
    print('│  3. Alternar status do restaurante      │')
    print('│  4. Sair                                │')
    print('└─────────────────────────────────────────┘\n')

def wait_for_enter():
    '''Espera uma entrada do usuário para prosseguir'''
    input('\n Pressione ENTER para continuar...')

def finalize_app():
    '''Encerra o programa'''
    clear_screen()
    print('\n╔═══════════════════════════════════════╗')
    print('║  Encerrando o sistema...                ║')
    print('║  Obrigado por usar o GuilherFood!       ║')
    print('╚═════════════════════════════════════════╝\n')

def invalid_option():
    '''Sinaliza entrada inválida para o usuário'''
    print('\nOpção inválida! Por favor escolha um número de 1 a 4')
    wait_for_enter()

def register_restaurant():
    '''Cadastra um restaurante novo'''
    clear_screen()
    print('╔═══════════════════════════════════════════╗')
    print('║   CADASTRO DE NOVOS RESTAURANTES          ║')
    print('╚═══════════════════════════════════════════╝\n')
    
    restaurant_name = input('Digite o nome do restaurante: ').strip()
    
    if not restaurant_name:
        print('\nNome não pode estar vazio!')
        wait_for_enter()
        return
    
    restaurant_type = input('Digite o tipo de culinária: ').strip()
    
    if not restaurant_type:
        print('\nTipo não pode estar vazio!')
        wait_for_enter()
        return
    
    restaurant = {
        'nome': restaurant_name,
        'tipo': restaurant_type,
        'ativo': False
    }
    
    registered_restaurants.append(restaurant)
    
    print(f"\nO restaurante '{restaurant_name}' foi cadastrado com sucesso!")
    print(f"   Tipo: {restaurant_type}")
    print(f"   Status: Inativo")
    wait_for_enter()

def list_restaurants():
    '''Lista os restaurantes cadastrados'''
    clear_screen()
    
    if not registered_restaurants:
        print('╔═══════════════════════════════════════════╗')
        print('║   NENHUM RESTAURANTE CADASTRADO           ║')
        print('╚═══════════════════════════════════════════╝')
        wait_for_enter()
        return
    
    print('╔═══════════════════════════════════════════════════════════════════╗')
    print('║                  RESTAURANTES CADASTRADOS                         ║')
    print('╚═══════════════════════════════════════════════════════════════════╝\n')
    
    print(f"{'N°':<4} {'NOME':<25} {'TIPO':<20} {'STATUS':<10}")
    print('─' * 70)
    
    for i, restaurant in enumerate(registered_restaurants):
        status = 'Ativo' if restaurant['ativo'] else 'Inativo'
        print(f"{i + 1:<4} {restaurant['nome']:<25} {restaurant['tipo']:<20} {status:<10}")
    
    wait_for_enter()

def toggle_restaurant_status():
    '''Ativa/Desativa restaurantes já cadastrados'''
    clear_screen()
    
    if not registered_restaurants:
        print('╔═══════════════════════════════════════════╗')
        print('║   NENHUM RESTAURANTE CADASTRADO           ║')
        print('╚═══════════════════════════════════════════╝')
        wait_for_enter()
        return
    
    print('╔═══════════════════════════════════════════════════════════════════╗')
    print('║              ALTERNAR STATUS DO RESTAURANTE                       ║')
    print('╚═══════════════════════════════════════════════════════════════════╝\n')
    
    print(f"{'N°':<4} {'NOME':<25} {'TIPO':<20} {'STATUS':<10}")
    print('─' * 70)
    
    for i, restaurant in enumerate(registered_restaurants):
        status = 'Ativo' if restaurant['ativo'] else 'Inativo'
    print(f"{i + 1:<4} {restaurant['nome']:<25} {restaurant['tipo']:<20} {status:<10}")
    
    try:
        choice = int(input('Digite o número do restaurante (0 para cancelar): '))
        
        if choice == 0:
            return
        
        if 1 <= choice <= len(registered_restaurants):
            index = choice - 1
            restaurant = registered_restaurants[index]
            restaurant['ativo'] = not restaurant['ativo']
            
            new_status = 'ativo' if restaurant['ativo'] else 'inativo'
            print(f"\nStatus do restaurante '{restaurant['nome']}' alterado para {new_status}!")
            wait_for_enter()
        else:
            print('\nNúmero inválido!')
            wait_for_enter()
    except ValueError:
        print('\nPor favor, digite um número válido!')
        wait_for_enter()

def choose_option():
    '''Seleciona a opção do menu com base na escolha do usuário'''
    try:
        chosen_option = int(input('Escolha uma opção: '))
        
        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            toggle_restaurant_status()
        elif chosen_option == 4:
            return 4
        else:
            invalid_option()
    except ValueError:
        invalid_option()
    
    return None

def main():
    '''Gerencia as demais funções'''
    while True:
        clear_screen()
        display_program_name()
        display_options()
        
        exit_program = choose_option()
        
        if exit_program == 4:
            break
    
    finalize_app()

if __name__ == '__main__':
    main()