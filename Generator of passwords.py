import random
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
people_lenght = int(input("Введите длину пароля"))
password = ""
for i in range(people_lenght):
    password += random.choice(elements)
print(password)
