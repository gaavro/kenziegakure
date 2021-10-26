from src.models.ninja_model import Ninja
class Jounin(Ninja):
    ninja_level = 'Jounin'

    def __init__(self, name: str, clan: str, village: str, proficiency: dict):
        super().__init__(name, clan, village, ninja_level = 'Jounin')
        self.name = name
        self.clan = clan
        self.village = village
        self.proficiency = proficiency
        self.is_in_mission = False


    def list_best_proficiency(self):
        biggest_proficiency = max(self.proficiency, key=self.proficiency.get)
        return f'{self.name} demonstra maior proficiência em {biggest_proficiency}'


    def start_mission(self):
        if self.is_in_mission:
           return f'O ninja {self.name} {self.clan} já está em uma missão'
        else:
            self.is_in_mission = True
            return f'O ninja {self.name} {self.clan} saiu em missão'


    def return_from_mission(self):
        if self.is_in_mission:
            self.is_in_mission = False
            return f'O ninja {self.name} {self.clan} retornou em segurança da missão'
        else:
            return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'