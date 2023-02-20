from database import db,Puppy

#create all the tables i.e transform the model class
#into a db table.
db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Frankie',5)

#none
#none
print(sam.id)
print(frank.id)

#you can add objects in one line or individually
# db.session.add(sam)
# db.session.add(frank)

db.session.add_all([sam,frank])

#commit will actuallyu save in the database
db.session.commit()

#in sqlalchemy the index starts from 1
print(sam.id)
print(frank.id)
