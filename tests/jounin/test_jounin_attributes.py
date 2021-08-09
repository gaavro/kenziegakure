from ..helpers import kakashi
from src.models.jounin_model import Jounin
from pytest import fail


def test_jounin_class_attribute(cria_jutsu_rasengan):
    try:
        result = Jounin.ninja_level
    except AttributeError:
        fail('Verifique se ninja_level é um atributo de CLASSE' +
             ' da classe Jounin.')

    expected = 'Jounin'

    assert result == expected, 'Verifique se o atributo de classe ' + \
        'ninja_level foi criado corretamente'


def test_jounin_attributes(cria_jounin_kakashi):
    assert cria_jounin_kakashi.name == kakashi.get('name'), \
        f'Verifique se o atributo name da classe Jounin' + \
        f' está sendo criado corretamente.'

    assert cria_jounin_kakashi.clan == kakashi.get('clan'), \
        'Verifique se o atributo clan da classe Jounin' + \
        ' está sendo criado corretamente.'

    assert cria_jounin_kakashi.village == kakashi.get('village'), \
        'Verifique se o atributo village da classe Jounin' + \
        ' está sendo criado corretamente.'

    assert cria_jounin_kakashi.ninja_level == 'Jounin', \
        'Verifique se o atributo ninja_level da classe Jounin' + \
        ' está sendo criado corretamente.'

    assert cria_jounin_kakashi.proficiency == kakashi.get('proficiency'), \
        'Verifique se o atributo proficiency da classe Jounin' + \
        ' está sendo criado corretamente.'

    assert cria_jounin_kakashi.is_in_mission is False, \
        'Verifique se o atributo is_in_mission da classe Jounin' + \
        ' está sendo criado corretamente.'
