from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#create_engine especifica qual banco de dados iremos nos comunicar
engine = create_engine('sqlite:///restaurantmenu.db')

#Vincula o mecanismo de banco de dados com a classe Base
Base.metadata.bind = engine

#Comunica engine com sessao que sera aberta
DBSession = sessionmaker(bind = engine)
session = DBSession()

#Cria um restaurante
myFirstRestaurant = Restaurant(name="Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

#busca todos os restaurantes inseridos
restaurantes = session.query(Restaurant).all()
print("=============Restaurantes=============")
print(restaurantes)
print()
pizza_de_queijo = MenuItem(name="Pizza de Queijo", description="Feito com ingredientes naturais e muzzarela", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(pizza_de_queijo)
session.commit()
items = session.query(MenuItem).all()
print("=============MenuItems=============")
print(items)
print()