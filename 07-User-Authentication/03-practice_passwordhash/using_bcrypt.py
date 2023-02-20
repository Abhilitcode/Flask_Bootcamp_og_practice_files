from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)
# print(hashed_password) --. commented to check T OR F

#if i have to check if th password id true or false

check = bcrypt.check_password_hash(hashed_password,'supersecretpassword')
print(check)
