from sqlalchemy import create_engine, Column, INTEGER, FLOAT, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///CarData.db", echo=False)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = "carinfo"

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(FLOAT)
    quantity = Column(INTEGER)


class Customer(Base):
    __tablename__ = "customerinfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    age = Column(INTEGER)
    gender = Column(String)

Base.metadata.create_all(engine)

# ###########################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

# ###########################################

# car_1 = Car(brand = 'Benz', model = "G Class", price = 2000, quantity = 5)
# car_2 = Car(brand = 'BMW', model = "S 300", price = 1800, quantity = 8)

# customer_1 = Customer(name = "Jack", phone = "09124563657", age = 33 , gender = "male")
# customer_2 = Customer(name = "Rose", phone = "09368521466", age = 24 , gender = "female")

# sessionLocal.add(customer_1)
# sessionLocal.add(customer_2)
# sessionLocal.commit()

# ###########################################

# cars_obj = sessionLocal.query(Car).all() # list of car objects
# #print(cars_obj)


# for item in cars_obj:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print(20 * '~')


# ###########################################

# car1 = sessionLocal.query(Car).filter_by(id = 1).first() # object
# print(car1.brand)
# print(car1.model)
# print(car1.price)

# ###########################################

# car_bmw = sessionLocal.query(Car).filter_by(brand = "BMW").all() # list of car object

# for item in car_bmw:
#     print(item.brand)
#     print(item.model)
#     print(item.price)

# ###########################################

# car_price = sessionLocal.query(Car).filter_by(price = 1800).all() # list of car object

# for item in car_price:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print(20 * '~')

# ###########################################

# car = sessionLocal.query(Car).filter(Car.price > 1500).all()
# for item in car:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print(20 * '~')

# car_temp = sessionLocal.query(Car).filter(Car.model.like("%g%")).all()
# for item in car_temp:
#     print(item.brand)
#     print(item.model)
#     print(item.price)
#     print(item.quantity)
#     print(20 * '~')

car_temp = sessionLocal.query(Car).filter(Car.model.like("%g%")).first()

# car_temp.brand = "AUDi"
# sessionLocal.commit()

if car_temp != None:
    sessionLocal.delete(car_temp)
    sessionLocal.commit()