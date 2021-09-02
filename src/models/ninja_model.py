
class Ninja:
    def __init__(self, name, clan, village, ninja_level="Unranked", jutsu_list=[], health_pool=100, chakra_pool=100, concious=True):
        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = []
        self.health_pool = health_pool
        self.chakra_pool = chakra_pool
        self.concious = concious

    def learn_jutsu(self, jutsu):
        self.jutsu_list.append(jutsu)
        # jutsu_name = self.jutsu_list[-1].jutsu_name
        return f"O ninja {self.name} {self.clan} acabou de aprender um novo jutsu: {jutsu.jutsu_name}"

    def cast_jutsu(self, jutsu, adversary):
        if adversary.concious is False:
            return False
        else:
            for jutsu_from_list in self.jutsu_list:
                if jutsu_from_list.jutsu_name == jutsu.jutsu_name and jutsu.chakra_spend <= self.chakra_pool:
                    adversary.health_pool -= jutsu_from_list.jutsu_damage
                    self.chakra_pool -= jutsu_from_list.chakra_spend
                    return True
                else:
                    return False

    @staticmethod
    def check_health(ninja_to_check):
        if ninja_to_check.health_pool < 0:
            ninja_to_check.health_pool = 0
            ninja_to_check.concious = False

        return ninja_to_check.concious


# naruto = Ninja("naruto", "uzumaki", "konoha")
# sasuke = Ninja("sasuke", "uchiha", "konoha")

# rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

# naruto.learn_jutsu(rasengan)

# print(naruto.jutsu_list)
# print(sasuke.jutsu_list)
