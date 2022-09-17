
class Titandex:

    def __init__(self,name1,height,strength1,winningstreak=0):
             self.name1=name1
             self.height=height
             self.strength1=strength1
             self.winningstreak=winningstreak

    def TitanvsScout(self,name2,strength2):
        self.name2=name2
        self.strength2=strength2
        if(self.strength1>strength2):
            self.winningstreak=self.winningstreak+1
            print(f"{self.name1} wins over {name2}")

        elif self.strength1==strength2:
            self.winningstreak=self.winningstreak
            print(f"Match is a Draw")
        else:
            self.winningstreak=0
            print(f"{self.name1} loses from {name2}")

    def TitanvsTitan(self,name3,strength3):

        self.name3=name3
        self.strength3=strength3

        if (self.name1 == name3):
            print(f"You Cannot Make The Titan Fight Itself")
        elif self.strength1 > strength3:
            self.winningstreak=self.winningstreak+1
            print(f"{self.name1} wins over {name3}")
        elif self.strength1 == strength3:
            self.winningstreak=self.winningstreak
            print(f"draw")
        else:
            self.winningstreak = 0
            print(f"{self.name1} loses from {name3}")


Founding_Titan=Titandex("Founding Titan",13,350)
Attack_Titan=Titandex("Attack Titan",15,275)
Armored_Titan=Titandex("Armored Titan",15,250)
Colossal_Titan=Titandex("Colossal Titan",60,300)
War_Hammer_Titan=Titandex("War Hammer Titan",15,235)
Beast_Titan=Titandex("Beast Titan",17,250)
Cart_Titan=Titandex("Cart Titan",4,175)
Female_Titan=Titandex("Female Titan",14,270)
Jaw_Titan=Titandex("Jaw Titan",5,225)
Attack_Titan.TitanvsScout("Mikasa",275)
Attack_Titan.TitanvsScout("Eren",270)
Attack_Titan.TitanvsScout("Armin",250)
Attack_Titan.TitanvsScout("Erwin",275)
Attack_Titan.TitanvsScout("Hange",230)
Attack_Titan.TitanvsScout("Jean",230)
Attack_Titan.TitanvsScout("Sasha",200)
Attack_Titan.TitanvsScout("Connie",180)

Attack_Titan.TitanvsTitan("Attack Titan",275)
Attack_Titan.TitanvsTitan("Armored Titan",250)
Attack_Titan.TitanvsTitan("Colossal Titan",300)
Attack_Titan.TitanvsTitan("War Hammer Titan",235)
Attack_Titan.TitanvsTitan("Beast Titan",250)
Attack_Titan.TitanvsTitan("Cart Titan",175)
Attack_Titan.TitanvsTitan("Founding Titan",350)
print("winningstreak:",Attack_Titan.winningstreak)

