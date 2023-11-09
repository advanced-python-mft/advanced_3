class person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def speak():
        print(f"hi my name is {self.name} im {self.age} and a {self.gender}")

ali = person("ali", 19, "male")

ali.speak()