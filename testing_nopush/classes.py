class human:
    def __init__(this,name,age,country):
        this.name = name
        this.age = age
        this.country = country
        if age < 18:
            this.civil_state = "minor"

    def setCivil_state(this,civil_state):
        this.civil_state = civil_state
    def __str__(this):
        return f"My name is {this.name} and im {this.age} years old"

class programmer(human):
    def __init__(this,name,age,country,salary):
        human.__init__(this,name,age,country)
        this.salary = salary