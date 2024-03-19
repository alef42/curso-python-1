import os

restaurantes = [{'nome' : 'Praça', 'categoria': 'Chinesa', 'ativo': False},
               {'nome' : 'pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
               {'nome' : 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exibir_nome_do_programa():
  
  print('🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n')

def exibir_opcoes():
      '''Essa função é responsavel por Exibir opções'''
  
      print('1. Cadastrar Restaurante')
      print('2. Listar Restaurante')
      print('3. Alternar estado do Restaurante')
      print('4. Sair\n')
      
def finalizar_app():
    exibir_subtitulos('Finalizar APP')
  
def voltar_ao_menu_principal():
      input('digite uma tecla para voltar \n')
      main()
      
def opcao_invalida():
     print('opcao invalida\n')
     voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
  

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    Inputs:
    - Nome do Restaurante
    - Categoria
    
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulos('Cadastrando restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: \n')
    categoria = input(f'Digite o nome da Categoria do Restaurante {nome_do_restaurante}\n')
    dados_do_restaurante = {'nome' : nome_do_restaurante, 'categoria' : categoria , 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    '''Essa função é responsavel por Listar os restaurante'''
    exibir_subtitulos('Listando Restaurante\n')    
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Staus')
    for restaurante in restaurantes :
     nome_restaurante = restaurante['nome']
     categoria = restaurante['categoria']
     ativo = 'ativado' if restaurante['ativo'] else 'desativado'
     print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
     
    voltar_ao_menu_principal()
    
def alternar_estado_do_restaurante():
  '''Essa função é responsavel por Alterar o estado do restaurante'''
  exibir_subtitulos('Alternando estado do Restaurante')
  nome_restaurante = input('digite o nome do restaurantre em que deseja alterar o estado: ')
  restaurante_encontrado = False
  
  for restaurante in restaurantes :
    if nome_restaurante == restaurante['nome']:
        restaurante_encontrado = True
        restaurante['ativo'] = not restaurante['ativo']
        menssagem = f'o restaurante{nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante{nome_restaurante} foi desativado com sucesso'
        print(menssagem)
    if not restaurante_encontrado : 
        print('o restaurante não foi encontrado')
  
  
  voltar_ao_menu_principal()
  
  
def escolher_opcao():
  '''Essa função é responsavel por escolher uma opção'''
  try: 
        opcao_escolhida = int(input('escolha uma opção: '))
        #opcao_escolhida = int(opcao_escolhida)
        print(f'Você escolheu a opção : {opcao_escolhida}')
        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4 :
          finalizar_app()
        else :
          opcao_invalida()
  except:
    opcao_invalida()
  
def main():
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcao()
     
if __name__ == '__main__':
        main()