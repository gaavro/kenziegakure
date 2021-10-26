from src.models.jutsu_model import Jutsu
class Ninja: 
    

    def __init__(self, name: str, clan: str, village: str, ninja_level="Unranked"):
        self.name= name
        self.clan= clan
        self.village= village
        self.ninja_level= ninja_level 
        self.jutsu_list= []
        self.health_pool= 100
        self.chakra_pool= 100
        self.concious= True

    def learn_jutsu(self, jutsu: Jutsu):
        self.jutsu_list.append(jutsu)
        return f'O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name}'           
    @staticmethod
    def check_health(self):
        if self.health_pool < 0:
            self.health_pool= 0
            self.concious= False
        return self.concious

    def cast_jutsu(self, jutsu: Jutsu, adversary: 'Ninja'):
        if adversary.concious is False:
            return False
        else: 
            if jutsu in self.jutsu_list and self.chakra_pool > jutsu.chakra_spend:
                 adversary.health_pool -= jutsu.jutsu_damage
                 self.chakra_pool -= jutsu.chakra_spend
                 return True
            return False

