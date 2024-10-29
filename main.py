"""
fait par: Vincent Brouillet
groupe: 405
exercice 2 du TP4 (personnage Dnd)
"""

import random as r
from dataclasses import dataclass


def dice_roll(dice_type):
    if dice_type == "stat":
        dice_list = []
        for dice in range(4):
            dice = r.randint(1, 6)
            dice_list.append(dice)
        dice_list.remove(min(dice_list))
        roll = sum(dice_list)
    elif dice_type == "armure":
        roll = r.randint(1, 12)
    elif dice_type == "vie":
        roll = r.randint(1, 20)
    elif dice_type == "profession":
        profession_list = ["Guerrier", "Magicien", "Archer", "Voleur", "Healer", "Tank"]
        roll = r.choice(profession_list)
    elif dice_type == "espece":
        espece_list = ["Humain", "Kobold"]
        roll = r.choice(espece_list)
    elif dice_type == "Humain":
        race_list = ["Calishite", "Chondathan", "Damaran", "Illuskan",
                     "Mulan", "Rashemi", "Shou", "Tethyrian", "Turami"]
        roll = r.choice(race_list)
    elif dice_type == "Kobold":
        race_list = [""]
        roll = r.choice(race_list)
    elif dice_type == "name":
        roll = "error"
    else:
        roll = "error"
    return roll


@dataclass
class DataNpc:
    Force: int
    Agilite: int
    Constitution: int
    Intelligence: int
    Sagesse: int
    Charisme: int
    armure: int
    espece: str
    race: str
    nom: str
    vie: int
    profession: str


class Npc:
    def __init__(self):
        self.npcdata = DataNpc(dice_roll("stat"), dice_roll("stat"), dice_roll("stat"),
                               dice_roll("stat"), dice_roll("stat"), dice_roll("stat"), dice_roll("armure"),
                               "Humain", "race", "NPC", dice_roll("vie"), dice_roll("profession"))
        self.npcdata.race = dice_roll(self.npcdata.espece)

    def stat_info(self):
        print(f"Nom: {self.npcdata.nom} | Race: {self.npcdata.race} {self.npcdata.espece} | "
              f"Vie: {self.npcdata.vie} | Profession: {self.npcdata.profession}"
              f"\nDefense: {self.npcdata.armure}"
              f"\nForce: {self.npcdata.Force}    | Constitution: {self.npcdata.Constitution}"
              f"\nAgilité: {self.npcdata.Agilite}  | Intelligence: {self.npcdata.Intelligence}"
              f"\nCharisme: {self.npcdata.Charisme} | Sagesse: {self.npcdata.Sagesse}")

    def attaquer(self, cible):
        if self.npcdata.Force > cible.npcdata.armure:
            dmg = self.npcdata.Force - cible.npcdata.armure
            print(f"attaque réussis, fait {dmg} dmg")
            cible.npcdata.vie -= dmg
        else:
            print(f"attaque rater")

    def subir_dommage(self, dmg):
        print(f"recu {dmg} dmg")
        self.npcdata.vie -= dmg


class Kobold(Npc):
    def __init__(self):
        super().__init__()
        self.npcdata.espece = "Kobold"
        self.npcdata.race = dice_roll(self.npcdata.espece)


class Hero(Npc):

    def __init__(self):
        super().__init__()
        self.dice = 0

    def hero_attaquer(self, cible):
        self.dice = r.randint(1, 20)
        if self.dice == 1 or self.dice < cible.npcdata.armure:
            dmg = 0
            print(f"attaque rater")
        elif self.dice == 20:
            dmg = r.randint(1, 8)
            print(f"attaque critique réussis, fait {dmg} dmg")
        else:
            dmg = r.randint(1, 6)
            print(f"attaque réussis, fait {dmg} dmg")
        cible.npcdata.vie -= dmg


npc = Npc()
kobold = Kobold()
hero = Hero()
