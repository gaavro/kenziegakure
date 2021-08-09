from ..helpers.ninja_attributes import luan, naruto


def test_ninja_attributes_naruto(cria_ninja_naruto):
    assert cria_ninja_naruto.name == naruto.get('name'), \
        'Verifique se o atributo name da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_naruto.ninja_level == naruto.get('ninja_level', 'Unranked'), \
        'Verifique se o atributo ninja_level da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_naruto.clan == naruto.get('clan'), \
        'Verifique se o atributo clan da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_naruto.village == naruto.get('village'), \
        'Verifique se o atributo village da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_naruto.jutsu_list == [], \
        'Verifique se o atributo jutsu_list da classe Ninja' + \
        ' está sendo inicializado como uma lista vazia.'

    assert cria_ninja_naruto.health_pool == 100, \
        'Verifique se o atributo health_pool da classe Ninja' + \
        ' está sendo inicializado com 100.'

    assert cria_ninja_naruto.chakra_pool == 100, \
        'Verifique se o atributo chakra_pool da classe Ninja' + \
        ' está sendo inicializado com 100.'

    assert cria_ninja_naruto.concious is True, \
        'Verifique se o atributo concious da classe Ninja' + \
        ' está sendo inicializado como True.'


def test_ninja_attributes_luan(cria_ninja_luan):
    assert cria_ninja_luan.name == luan.get('name'), \
        'Verifique se o atributo name da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_luan.ninja_level == luan.get('ninja_level', 'Unranked'), \
        'Verifique se o atributo ninja_level da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_luan.clan == luan.get('clan'), \
        'Verifique se o atributo clan da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_luan.village == luan.get('village'), \
        'Verifique se o atributo village da classe Ninja' + \
        ' está sendo criado corretamente.'

    assert cria_ninja_luan.jutsu_list == [], \
        'Verifique se o atributo jutsu_list da classe Ninja' + \
        ' está sendo inicializado como uma lista vazia.'

    assert cria_ninja_luan.health_pool == 100, \
        'Verifique se o atributo health_pool da classe Ninja' + \
        ' está sendo inicializado com 100.'

    assert cria_ninja_luan.chakra_pool == 100, \
        'Verifique se o atributo chakra_pool da classe Ninja' + \
        ' está sendo inicializado com 100.'

    assert cria_ninja_luan.concious is True, \
        'Verifique se o atributo concious da classe Ninja' + \
        ' está sendo inicializado como True.'
