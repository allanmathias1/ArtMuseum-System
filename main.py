from classes import *
import sys
import getpass


def getMenuOption():
  try:
    opt = int(input('Insira o número correspondente à opção desejada:'))
    return opt
  except:
    print(TypeError("\n\n\nApenas numerais são aceitos.\nPor favor, tente novamente."))
    return None

def validateLogin(access = bool):
  if access == True:
    #Validar Usuário Tipo Admin
    pass
  else:
    #Validar Usuário Tipo Common
    pass

def publicSystem():
  while True:
    print("""\n\n\n---- Sistema Público de Acesso ao Museu de Arte SaquArte (v0.5) ----\n\n
Escolha uma opção abaixo:
1. Cadastre-se
2. Login
3. Consulta virtual ao acervo
0. Sair
""")
    opt = getMenuOption() 
    match opt:
      case 1:
        newUser(False)
      case 2:
        print('Login ainda não implementado.')
      case 3:
        print('Consulta virtual ainda não implementada.')
      case 0:
        print('O Sistema Público de Acesso ao Museu de Arte SaquArte será encerrado agora.')
        exit()
      case None:
        pass
      case _:
        print('Opção inválida, por favor tente novamente.\n\n\n')


def maintSystem():
  print("""\n\n\n---- Sistema de Manutenção e Gestão de Acervo do Museu de Arte SaquArte (v0.5) ----\n\n
Escolha uma opção abaixo:
1. Gerenciar Obras de arte
2. Gerenciar Autores
3. Gerenciar Estilos
4. Gerenciar Rotas
5. Gerenciar Usuarios
6. Gerenciar Visitas
0. Sair
""")
  opt = getMenuOption()
  match opt:
    case 1:
      print("Funcionalidade não implementada.")
    case 2:
      print('Funcionalidade não implementada.')
    case 3:
      print('Funcionalidade não implementada.')
    case 4:
      print('Funcionalidade não implementada.')
    case 5:
      print('Funcionalidade não implementada.')
    case 6:
      print('Funcionalidade não implementada.')
    case 0:
      print('O Sistema de Manutenção e Gestão de Acervo será encerrado.')
    case None:
      pass
    case _:
      print('Opção inválida, por favor tente novamente.\n\n\n')


if __name__ == "__main__":
  while True:
    print("""Bem vindo ao Ambiente Virtual do Museu de Arte SaquArte.
  Escolha no menu abaixo, o sistema que deseja acessar:
    1. Sistema Público de Acesso;
    2. Sistema de Manutenção e Gestão do Acervo;
  """)
    opt = getMenuOption()
    match opt:
      case 1:
        publicSystem()
      case 2:
        print('Por favor, realize o login para continuar:')
        if validateLogin(True) == True:
          maintSystem()
      case None:
        pass
      case _:
        print('Opção inválida, por favor tente novamente.\n\n\n')


