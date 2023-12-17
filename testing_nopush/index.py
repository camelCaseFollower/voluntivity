global gay;
gay = False;
def sayHi(name):
    returning_string = "Hello " + name;
    if gay == True:
        return returning_string + ", im gay";
    else:
        return returning_string;
    
class human:
    def __init__(this, name, age):
        this.name = name;
        this.age = age;
    def __str__(this):
        return f"name:{this.name},\nage:{this.age}";
    def birthday(this):
        this.age += 1

class programmer(human): #to inherit human
    def __init__(this,age,name,salary):
        human.__init__(this,age,name) #To inherit parents constructor
        this.salary = salary

Adam = human("Adam",2023);
Eve = human("Eve",2023);
Jacob = programmer("Jacob",18,900);

print(Jacob.salary);
print(Eve.age);
Eve.birthday();
print(Eve.age);
print(sayHi(Adam.name));
print(sayHi(Eve.name));

for x in range(2,4):
    print(x)