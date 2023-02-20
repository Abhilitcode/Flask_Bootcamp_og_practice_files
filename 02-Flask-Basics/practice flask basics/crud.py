from database import db,Puppy

#create
my_puppy = Puppy('rufus',4)
db.session.add(my_puppy)
db.session.commit()

#read
#returns the list of all puppies objects
all_puppies = Puppy.query.all()
print(all_puppies)

#select by # ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filters
#produce some sql code!
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
#['Frankie is 5 years old']

#update
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

#check changes
all_puppies = Puppy.query.all()
print(all_puppies)
