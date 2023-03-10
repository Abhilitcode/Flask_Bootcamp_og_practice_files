#create entries into the tables
from models import db,Puppy,Owner,Toy

#create tow puppies
rufus = Puppy("Rufus")
fido = Puppy("Fido")

#add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

#check!
print(Puppy.query.all())

#grab rufus from db
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
#to get all the rufus you can simply do .all() or .all([0])

#Create owner object
abhi = Owner('abhi',rufus.id)

#give rufus some toys
toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)

db.session.add_all([abhi,toy1,toy2])
db.session.commit()

#grab rufus again after thise additons
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
