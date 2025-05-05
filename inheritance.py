class Superhero:
    def _init_(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self._power_level = power_level  
    def display_identity(self):
        print(f"{self.alias}, also known as {self.name}, is ready to save the day!")

    def use_power(self):
        print(f"{self.alias} uses their special power!")

    def get_power_level(self):
        return self._power_level

    def set_power_level(self, level):
        if level >= 0:
            self._power_level = level
        else:
            print("Power level can't be negative!")


class FlyingHero(Superhero):
    def use_power(self):
        print(f"{self.alias} takes to the skies and swoops down on enemies! ")


class StrengthHero(Superhero):
    def use_power(self):
        print(f"{self.alias} smashes through walls with superhuman strength! ")


hero1 = FlyingHero("Kara Zor-El", "Supergirl", 95)
hero2 = StrengthHero("Bruce Banner", "Hulk", 100)

hero1.display_identity()
hero1.use_power()

hero2.display_identity()
hero2.use_power()

print("Supergirl's Power Level:", hero1.get_power_level())
hero1.set_power_level(98)
