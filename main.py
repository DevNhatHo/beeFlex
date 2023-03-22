class Person:
    def __init__(self, name, age, sex, weight, height, activity_level):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.sex = sex
        self.activity_level = activity_level

    def display_info(self):
        print("{name}, {sex} is currently {age}, height is {height} (cm) and weight is {weight} (kgs)".format(
            name=self.name, age=self.age, height=self.height, weight=self.weight, sex=self.sex))

    def calculate_daily_calories(self):
        if self.sex == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.sex == "female":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            raise ValueError("Invalid sex")

        if self.activity_level == "sedentary":
            tdee = bmr * 1.2
        elif self.activity_level == "lightly active":
            tdee = bmr * 1.375
        elif self.activity_level == "moderately active":
            tdee = bmr * 1.55
        elif self.activity_level == "very active":
            tdee = bmr * 1.725
        elif self.activity_level == "extra active":
            tdee = bmr * 1.9
        else:
            raise ValueError("Invalid activity level")

        return round(tdee)

def create_person_from_input():
    print("Please enter your information below.")
    name = input("Name: ")
    age = int(input("Age: "))
    sex = input("Sex: ")
    weight = float(input("Weight (in kg): "))
    height = float(input("Height (in cm): "))
    print("Activity level:")
    print("1. Sedentary")
    print("2. Moderately active")
    print("3. Very active")
    print("4. Extra active")
    activity_level = int(input("Enter the number corresponding to your activity level: "))

    if activity_level == 1:
        activity_level_str = "sedentary"
    elif activity_level == 2:
        activity_level_str = "moderately active"
    elif activity_level == 3:
        activity_level_str = "very active"
    elif activity_level == 4:
        activity_level_str = "extra active"
    else:
        print("Invalid input for activity level.")
        return None

    person = Person(name, age, sex, weight, height, activity_level_str)

    return person

person = create_person_from_input()
print(person.calculate_daily_calories())

