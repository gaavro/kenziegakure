# Cole seu código aqui
class Jutsu:
    jutsu_ranks = ("D", "C", "B", "A", "S")

    def __init__(self, jutsu_name, jutsu_type, jutsu_level="Unranked", jutsu_damage=0, chakra_spend=100):
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = chakra_spend
        self.jutsu_level = jutsu_level

        if self.chakra_spend <= 0:
            self.chakra_spend = 100

        for level in self.jutsu_ranks:
            print(level)
            print(self.jutsu_level.upper())
            if level == self.jutsu_level.upper():
                self.jutsu_level = jutsu_level.upper()
                break

    def __str__(self) -> str:
        str(self.jutsu_name)


rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
print(rasengan.__dict__)
