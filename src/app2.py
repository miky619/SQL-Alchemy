from sqlalchemy import create_engine, Column, INTEGER, FLOAT, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("sqlite:///CarData_relation.db", echo=False)
engine.connect()

Base = declarative_base()

class Car(Base):
    __tablename__ = "carinfo"

    id = Column(INTEGER, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    price = Column(FLOAT)
    quantity = Column(INTEGER)

    customer_id = Column(INTEGER, ForeignKey("customerinfo.id"))

    customers = relationship("Customer", back_populates="owner")


class Customer(Base):
    __tablename__ = "customerinfo"

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    age = Column(INTEGER)
    gender = Column(String)

    owner = relationship('Car', back_populates='customers')


class Student(Base):
    __tablename__ = "student"

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(FLOAT)

Base.metadata.create_all(engine)

# ###########################################

Session = sessionmaker(bind=engine)
sessionLocal = Session()

# ###########################################

# customer1 = Customer(name = "Ali", phone = "09362164199", age = 36, gender = "male")
# cstomer2 = Customer(name = "Nima", phone = "09042004563", age = 29, gender = "male")

# sessionLocal.add_all([customer1, cstomer2])
# sessionLocal.commit()


# car1 = Car(brand ='Benz', model='G1 class', price = 2000, quantity =15, customer_id =1 )
# car2 = Car(brand ='BMW', model='AMG2', price = 1500, quantity =10, customer_id =1)
# sessionLocal.add_all([car1, car2])
# sessionLocal.commit()


# customer1 = sessionLocal.query(Customer).filter_by(id = 1).first()
# customer1 = sessionLocal.query(Customer).filter(Customer.name.like('Ali%')).first()


# print(customer1.owner)
# for car in customer1.owner:
#     print(car.brand)
#     print(car.model)
#     print('--'*30)

car1 = sessionLocal.query(Car).filter_by(id = 1).first()

# print(car1.brand)
# print(car1.customers.name)
# print(car1.customers.phone)


# ###########################################

def add_student(name, score):
    student = Student(name=name, score=score)
    sessionLocal.add(student)
    sessionLocal.commit()
    print(f"Student {name} added with id {student.id}")



def get_all_students():
    students = sessionLocal.query(Student).all()
    for s in students:
        print(s.id, s.name, s.score)
    return students



def update_student(student_id, name=None, score=None):
    student = sessionLocal.query(Student).filter_by(id=student_id).first()
    if student is None:
        print("Student not found")
        return
    if name is not None:
        student.name = name
    if score is not None:
        student.score = score
    sessionLocal.commit()
    print(f"Student {student_id} updated")



def delete_student(student_id):
    student = sessionLocal.query(Student).filter_by(id=student_id).first()
    if student is None:
        print("Student not found")
        return
    sessionLocal.delete(student)
    sessionLocal.commit()
    print(f"Student {student_id} deleted")



# add_student("Sara", 18.5)
# add_student("Reza", 15)


# print('--'*30)
# get_all_students()

# print('--'*30)
# update_student(1, score=19)
# update_student(2, name="Reza Ahmadi")
# get_all_students()

# print('--'*30)
# delete_student(2)
# get_all_students()