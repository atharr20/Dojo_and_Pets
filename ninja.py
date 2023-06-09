from pet import Pet

class Ninja(Pet):
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):

        if len(self.pet_food)>0:
            food=self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()

my_treats=['Snausage', 'bacon', 'trash']
my_pet_food = ['pizza','burger']

nibbles = Pet("Mr Nibbles", 'horse', ['nibbles on things', 'is invisible'], 'hey hey')

Athar= Ninja('Mohammed', 'last name', nibbles, my_treats,my_pet_food)

Athar.feed()
Athar.feed()
Athar.feed()
