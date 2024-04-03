# this creates the db using engine provided in the connection string 
from sqlalchemy import create_engine
# it avails the session object to run query methods on my db 
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.base import Base

# creating the db // table
DATABASE_URI  = "sqlite:///persons.db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# metadata object  // create table with defined models 
Base.metadata.create_all(engine)

# create sample persons 
person1 = "Joseph"
email1 = "josephbill00@gmail.com"

person1_record = session.query(User).filter_by(username=person1).first()
print("person 1 records", person1_record)
if not person1_record:
    # create the object 
    person1_record = User(username=person1, email=email1)
    session.add(person1_record)


# delete 
# 1. look for the record to delete if it exists 
# 2. sesison.delete(persontodelete)
# 3. session.commit() 



# # update 
# persontoUpdate = session.query(User).filter_by(username=person1).first()
# if not persontoUpdate:
#     print("user cannot be found")
# else: 
#     persontoUpdate.username = "Mary"
#     persontoUpdate.email = "mary00@gmail.com"
#     session.commit()

# read the data 
all_persons  = session.query(User).all()
# this returns the records as a list of objects 
# [<object 894385985> , <]
for person in all_persons:
    print("User name ", person.username, person.id)


# commit changes 
session.commit()

session.close()