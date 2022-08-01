from ctypes.wintypes import tagPOINT
from os import remove


name = "tangpan"
print(name.title())

print(name.upper())

print(name.upper().title())

print(name.lower())

name = "tang meng"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

print("Hello, n         n")
print("Hello, n\nn")

favorite_langeuate = "python"
print(favorite_langeuate)
print(favorite_langeuate.rstrip("n"))
print(favorite_langeuate)

print(2+3)
print(3 - 2)
print(2 * 3)
print(3 ** 2)

a = 3_000_000
print(a)

x, y, z = 0, 1, 2
print(x)
print(y)
print(z)

MAX = 2
print(MAX)

# 此行为注释

"""
此为多行注释
"""

"""列表是由一系列按特定顺序排列的元素组成。列表通常包含多个元素，因此给列表指定一个复数的名称（letters、digits、names）"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
print(f"My favorite bicycle is {bicycles[0].title()}")

bicycles[0] = 'tre'
print(bicycles)

b = bicycles.append('a')
print(b)

b = 'tang'
print(b)

bicycles.insert(0, 'a')
print(bicycles)

c = bicycles.insert(1, 'b')
print(c)

print(bicycles)

del bicycles[0]
print(bicycles)

del bicycles[-1]
print(bicycles)

popped_bicycles = bicycles.pop()
print(popped_bicycles)
print(bicycles)

first_owned = bicycles.pop(0)
print(first_owned)
print(bicycles)


"""remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保每个值都删除。"""
bicycles.remove('cannondale')
print(bicycles)

bicycles.append('last')
print(bicycles)
bicycles.append(5)
print(bicycles)

a = 5 + bicycles[-1]
print(a)

bicycles.append(['1', '2', '3'])
print(bicycles)

print(bicycles[-1])

too_expensive = ['1', '2', '3']
bicycles.remove(too_expensive)
print(bicycles)

a = [1, 2, 3, 4, 5]
a.remove(3)
print(a)
a = a.remove(4)
print(a)
print()

original = 'tang'
original = [1, 2, 3]


print("原函数自身改动测试")
a = 'tang'
a = [1, 2, 3]
print(a)
a.pop()
print(a)
print()

print("自我改变不可赋值自身测试")
a = 'tang'
a = [1, 2, 3]
print(a)
print(a.pop())
print()

print("自我改变可赋值自身测试")
a = 'tang'
a = [1, 2, 3]
print(a)
a = a.pop()
print(a)
print()

print("自我改变可赋值给新变量测试")
a = 'tang'
a = [1, 2, 3]
print(a)
b = a.pop(2)
print(b)
print()

cars = [3, 1, 9, 5]
print(cars)
print(len(cars))


print(range(5))

a = range(5)
print(a)

a = list(range(5))
print(a)

print(max(a))

print(max(range(5)))

print(range(1,5))

for value in range(1, 5):
    print(value)

for value in list(range(1,5)):
    print(value)

print(sum(range(5)))
print()

squares = [value ** 2 for value in range(5)]
print(squares)

a = [1, 2, 3, 4, 5]
print(a)
print(a[1:3])

a = list(range(10))
print(a[0:8:3])

a = range(5)
print(a[-3:])

for value in a[-3:]:
    print(value)

a = list(range(10))
print(a)

b = a
print(b)
b.pop()
print(b)
print(a)
print()

a = list(range(5))
b = a[:]
print(b)
b.pop()
print(b)
print(a)

a = 'tang'
print(a)

print(a.strip("g") == 'tan')
print(a.strip("g") > 'tang')
print('tang' < 'tan')
print('tang' > 'tan')

age_0 = 32
age_1 = 28
print(age_0 > 30 and age_1 < 30)
print((age_0 < 30) and (age_1 < 30))

a = list(range(5))
print(2 in a)
print(2 not in a)

age = 19
if age >= 20:
    print("good!")

if age >= 20:
    print("good!")
else:
    print("bad!")

age = 12
if age < 4:
    print("small")
elif age < 14:
    print("middle")
else: 
    print("big")


"""最好不用else，而全部使用 elif"""

a = list(range(10))
print(a)
if a:
    print("good")
for i in range(10):
    a.pop()
if a:
    print("a have number")
else:
    print("a is empty")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

alien_0['x_position'] = 0
print(alien_0)

alien_0['color'] = 'red'
print(alien_0)

for key, value in alien_0.items():
    print(key)
    print(value)
print(f"key is {key}")

for key, value in alien_0.items():
    print(f"\nKey: {key}")
    if key == 'points':
        print(f"Value: {value}")

for key in alien_0.keys():
    print(key)

print(alien_0.keys())

for value in alien_0.values():
    print(value)

digits = {1, 2, 3, 2}
print(digits)
print(type(digits))

a = list(range(5))
print(a)

a.append(2)
print(a)
print(type(a))

print(set(a))
print(type(a))

a = ['a','b', 'b', 'c']
print(a)
print(set(a))
b = set(a)
print(b)
print(type(b))
b = list(b)
print(b)
print(type(b))

a = {'first': 'pan', 'last':'tang'}
b = {'first': 'meng', 'last':'tang'}
print(a)
print(b)
name = [a, b]
print(name)

class_1 = {'name':'九班', 'students': ['tang meng', 'tang heng', 'liu hui']}
print(class_1)
print(class_1.get('name'))
print(class_1.get('students'))
print(class_1.get('number'))


# prompt = "If you tell us who you are, I could personalize the messages you see."
# prompt += "\nWhat is your first name? Please input: "
# name = input(prompt)

# prompt = "How old are you? Please input: "
# age = input(prompt)

# print("type of age is type(age): ")
# print(type(age))
# age = int(age)
# print("type of age is type(age): ")
# print(type(age))

print(4 % 3)
print(5 % 3)
print(6 % 3)


# message = ""
# while message != 'quit':
#     message = input("Enter: ")

# active = True
# while active:
#     message = input("Enter: ")
#     if message == "quit":
#         active = False
#     else:
#         active = True

# while True:
#     city = input("Enter: ")
#     if city == "quit":
#         break
#     else:
#         print(f"{city}")

print()
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        print(f"{current_number}")
    else:
        continue

print()
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

animals = ['cats', 'dogs', 'rabbits', 'cats', 'cats']
print(animals)
while 'cats' in animals:
    animals.remove('cats')
print(animals)
print()

def greet_user():
    """显示简单的问候语"""
    print("Hello!")

greet_user()

print()
def greet_user(username):
    """显示简单问候语"""
    print(f"Hello, {username.title()}!")

greet_user("tang")


print()
def describe_pet(animal_type, pet_name):
    """描述宠物的类别和名字"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet("dog", 'marry')
describe_pet("marry", 'dog')
describe_pet(pet_name='marry', animal_type='dog')


print()
def describe_pet(pet_name, animal_type='dog'):
    """描述宠物的类别和名字"""
    print(f"\nI have a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}")

describe_pet('wille', animal_type='cat')
describe_pet(pet_name='willie', animal_type='cat')

def get_formatted_name(first_name, last_name):
    """返回整洁的函数名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('pan', 'tang')
print(musician)

print()
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的名字"""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

me = get_formatted_name('pan', 'tang')
print(me)
you = get_formatted_name(first_name='Qing', last_name='liu', middle_name='zai')
print(you)

unprinted_designs = ['a', 'b', 'c']
completed_models = []
print(unprinted_designs)

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print(unprinted_designs)

print()
unprinted_designs = ['a', 'b', 'c']
completed_models = []
unprinted_designs_1 = unprinted_designs[:]
# 模型打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其移到列表 completed_models 中。
while unprinted_designs_1:
    current_design = unprinted_designs_1.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print(unprinted_designs)

# 形参名 “*topping” 中的星号让 python 创建一个名为 topping 的空元组，并将收到的所有值都封装到这个元组中。
# 当前测试只能通过传这种形式：
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# 不能直接传列表（直接传列表会把列表当成一个个体，并不是多种）：
# foods = ['mushrooms', 'green peppers', 'extra cheese']
# make_pizza(foods)

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切信息。"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('pan', 'tang', location='shandong', field='computer vision')
print(user_profile)


# __init__(self) 是特殊的方法，当创建类的新实例时，python 会自动调用。self 让实例能够访问类中的属性和方法。
# __init__() 函数中的参数是利用该类创建新实例所必须输入的参数。

# 例如：
class Dog:
    """一次模拟小狗的尝试"""
    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age
    def sit(self):
        """模拟小狗收到命令时蹲下。"""
        print(f"{self.name.title()} is now sitting.")
    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name.title()} rolled over!")

my_dog = Dog('hua', 27)
my_dog.sit()
my_dog.roll_over()
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog's age is {my_dog.age}.")


class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回整洁的描述信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('byd', 'han', 2022)
print(my_new_car.get_descriptive_name())

class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __init__(self, make, model, year, odometer_reading=0):
        """初始化描述汽车属性 make, model, year"""
        self.odometer_reading = odometer_reading
my_car = Car('tang', 'pan', 2021)
print(my_car.odometer_reading)
my_car.odometer_reading = 23
print(my_car.odometer_reading)

class Car:
    """一次模拟汽车的就尝试。"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性 make, model, year"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.odometer_reading)
my_new_car.update_odometer(23)
print(my_new_car.odometer_reading)


class Car:
    """一次模拟汽车的简单尝试。"""
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性。"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """返回整洁的描述信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class ElectricCar(Car):
    """在 Car 的基础上，电动车的独特之处。"""
    def __init__(self, make, model, year):
        """初始化父类的属性。"""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model S', 2013)
print(my_tesla.get_descriptive_name())


class Car:
    """描述汽车的类"""
    def __init__(self, make, model, year):
        """初始化车的属性 make, model, year"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class ElectricCar(Car):
    """在 Car 类的基础上，电动车的独特之处。"""
    
    # def __init__(self, make, model, year):
    #     """初始化父类的属性，再初始化电动车的特有的属性。"""
    #     super().__init__(make, model, year)
    #     self.battery_size = 75

    def __init__(self, make, model, year, battery_size=75):
        """初始化"""
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def describe_battery(self):
        """描述电池的属性。"""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_car = ElectricCar('tesla', 'model s', 2020)
print(my_car.get_descriptive_name())
my_car.describe_battery()


print()
class Car:
    """模拟汽车创建该类。"""
    
    def __init__(self, make, model, year):
        """初始化汽车属性 make, model, year"""
        self.make = make
        self.model = model
        self.year = year

    def fill_gas_tank(self):
        """汽车加油。"""
        print("加油。")

# class ElectricCar(Car):
#     """在 Car 的基础上，电动车的独特之处。"""
    
#     def __init__(self, make, model, year):
#         """初始化父类的属性。再初始化电动车特有的属性。"""
#         super.__init__(make, model, year)

#     def fill_gas_tank(self):
#         """电动车没有油箱。"""
#         print("This car doesn't need a gas tank!")


class Battery:
    """模拟电动汽车电瓶的属性和方法。"""
    
    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """在 Car 类的基础上，电动车的独特之处。"""
    
    def __init__(self, make, model, year):
        """初始化父类的属性。再初始化电动车特有的属性。"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model', 2020)
my_tesla.battery.describe_battery()

print(r'''line1,\n
line2
line3''')
print('''line1...line2...line3''')

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello,  \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n, 
f, 
s1, 
s2, 
s3, 
s4)

import sys
print(sys.getdefaultencoding())

print()

tuple = ('a', 'b')

b = 0
for i in range(1,101):
    b += i
    print(b)