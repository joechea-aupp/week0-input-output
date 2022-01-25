input("Welcome to myAPP(waf waf) registration, press any key to start")

first_name = input("First Name: ")
last_name = input("Last Name: ")
date_of_birth = input("Date of Birth: ")
dog_age = input("Your dog age: ")

dog_age_human = int(dog_age) * 7

user_information = f'''

Registration Information
First Name = {first_name}, Last Name = {last_name}
was born on {date_of_birth}

--------------------------------------------------------
owning a dog which age equivalent of {dog_age_human} age
--------------------------------------------------------
'''
print(user_information)
