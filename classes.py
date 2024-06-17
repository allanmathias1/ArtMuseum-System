import pandas as pd
import os
from main import *
import getpass

class Visits:
   VISITAS_FILEPATH = './files/visits.csv'

class Art:
  ART_FILEPATH = './files/art.csv'
  def __init__(self,id, title, date, theme, style, description, technique, author, location):
    self.id = id
    self.title = title
    self.date = date
    self.theme = theme
    self.style = style
    self.description = description
    self.technique = technique
    self.author = author
    self.location = location
    self.related_docs = []
    self.vip = []

class Author:
  AUTHOR_FILEPATH = './files/author.csv'
  def __init__(self, id, name, birth_date, birth_place, bio, styles):
    self.id = id
    self.name = name
    self.birth_date = birth_date
    self.birth_place = birth_place
    self.bio = bio
    self.styles = styles

class Style:
  STYLE_FILEPATH = './files/style.csv'
  def __init__(self, id, name, time_influence, characteristics, school):
    self.id = id
    self.name = name
    self.time_influence = time_influence
    self.characteristics = characteristics
    self.school = school

class Route:
  ROUTE_FILEPATH = './files/routes.csv'
  def __init__(self, id, name, content):
    self.id = id
    self.name = name
    self.content = content

class User:
  def __init__(self, name, login = str, password = str, access = False):
    self.name = name
    self.login = login
    self.password = password
    self.access = access

class Common(User):
    COMMON_FILEPATH = './files/common.csv'
    def __init__(self, name, login = str, password = str, access = False, origin = str):
      User.__init__(self, name, login, password, access)
      self.origin = origin

class Maintenance(User):
  MAINT_FILEPATH = './files/maint.csv'
  def __init__(self, name, login = str, password = str, access = True, role = str):
    User.__init__(self, name, login, password, access)
    self.role= role
  #Acesso para cadastro de obras, cadastro de usuarios, emprestimo de obras, logbooks e afins.
  pass

def makeDict(object):
    if isinstance(object, Art):
        return {
            'id': object.id,
            'title': object.title,
            'date': object.date,
            'theme': object.theme,
            'style': object.style,
            'description': object.description,
            'technique': object.technique,
            'author': object.author,
            'location': object.location,
            'related_docs': object.related_docs,
            'vip': object.vip
        }
    elif isinstance(object, Author):
        return {
            'id': object.id,
            'name': object.name,
            'birth_date': object.birth_date,
            'birth_place': object.birth_place,
            'bio': object.bio,
            'styles': object.styles
        }
    elif isinstance(object, Style):
        return {
            'id': object.id,
            'name': object.name,
            'time_influence': object.time_influence,
            'characteristics': object.characteristics,
            'school': object.school
        }
    elif isinstance(object, Route):
        return {
            'id': object.id,
            'name': object.name,
            'content': object.content
        }
    elif isinstance(object, Common):
        return {
            'name': object.name,
            'login': object.login,
            'password': object.password,
            'access': object.access,
            'origin': object.origin
        }
    elif isinstance(object, Maintenance):
        return {
            'name': object.name,
            'login': object.login,
            'password': object.password,
            'access': object.access,
            'role': object.role
        }
    
    else:
        raise TypeError("Unsupported object type")

def saveCsv(filepath, object):
    dict_object = makeDict(object)
    df = pd.DataFrame([dict_object])
    try:
        if os.path.isfile(filepath):
            df.to_csv(filepath, mode='a', header=False, index=False)
        else:
            df.to_csv(filepath, mode='w', header=True, index=False)
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")
        exit()
    print('As informações foram salvas com sucesso.')

def createUser(access = bool):
   cadastro = True
   if access == False:
    while cadastro == True:
        print('Insira seu nome:')
        name = input()
        print('Insira o login desejado:')
        login = input()
        print('Insira a senha desejada:')
        password = getpass.getpass()
        school = 'Turista'
        while True:
            print("Representa alguma escola?\n1. Sim\n2. Não")
            opt = getMenuOption()
            if opt == 1:
                print('Insira o nome da escola:')
                school = input()
                break
            elif opt == 2:
                break
            elif opt == None:
                pass
            else:
                print('Opção inválida. Por favor, tente novamente.')
        print('Informações recebidas com sucesso.')
        while True:
            print(f'''Por favor confirme as informações:
Nome:{name}
Login: {login}
Senha: {len(password)*'*'}''')
            if school == 'Turista':
                print('Turista sem associação escolar.')
            else:
                print(f'Escola: {school}')
            print('Confirma as informações acima?\n1. Sim\n2. Não')
            opt = getMenuOption()
            match opt:
              case 1:
                cadastro = False
                break
              case 2:
                print('Reiniciando cadastro de usuário.\n\n\n\n')
        newUser = Common(name,login,password,False,school)
        saveCsv(Common.COMMON_FILEPATH,newUser)

if __name__ == '__main__':
    object = Art('01','Noite','18/10/2000','Natureza','Impressionismo','A bela noite representada em pintura à óleo.','Pintura à óleo','Desconhecido','Sala 01, Estande 03')
    read = makeDict(object)
    print(read)
    createUser(False)