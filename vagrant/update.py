from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

veggie_burgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggie_burger in veggie_burgers:
    print(veggie_burger.id)
    print(veggie_burger.price)
    print(veggie_burger.restaurant.name)
    print('\n')

urban_burger = session.query(MenuItem).filter_by(id=10).one()

#Atualiza preco
urban_burger.price = '$2.99'
session.add(urban_burger)
session.commit()