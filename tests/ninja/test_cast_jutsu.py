def test_cast_jutsu_ninja_succeed(naruto_rasengan, cria_ninja_luan):
    naruto, rasengan = naruto_rasengan

    result = naruto.cast_jutsu(rasengan, cria_ninja_luan)

    # rasengan chakra_spend = 15
    assert naruto.chakra_pool == 100 - 15, 'Verifique se seu método ' + \
        'cast_jutsu está deduzindo corretamente o custo de chakra do ' + \
        'jutsu da chakra_pool do usuário que chamou o método.'

    # rasengan damage = 20
    assert cria_ninja_luan.health_pool == 100 - 20, 'Verifique se seu método ' + \
        'cast_jutsu está deduzindo corretamente o damage do jutsu da ' + \
        'health_pool do adversary.'

    assert result, 'Verifique se seu método cast_jutsu está retornando ' + \
        'um booleano True se o jutsu foi lançado.'


def test_cast_jutsu_ninja_failed_no_chakra(naruto_rasengan, cria_ninja_luan):
    naruto, rasengan = naruto_rasengan

    # Testar se o jutsu será lançado com mana 0
    naruto.chakra_pool = 0

    result = naruto.cast_jutsu(rasengan, cria_ninja_luan)

    assert result is False, 'Verifique se seu método cast_jutsu está retornando ' + \
        'um booleano False quando o castador não tem chakra suficiente.'

    assert naruto.chakra_pool == 0, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo chakra do castador quando o jutsu' + \
        'n foi castado.'

    assert cria_ninja_luan.health_pool == 100, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo hp do adversary quando o jutsu ' + \
        'n foi castado.'


def test_cast_jutsu_ninja_failed_unconcious(naruto_rasengan, cria_ninja_luan):
    naruto, rasengan = naruto_rasengan

    # Testar se o jutsu será lançado o adversário inconciente
    cria_ninja_luan.concious = False

    result = naruto.cast_jutsu(rasengan, cria_ninja_luan)

    assert result is False, 'Verifique se seu método cast_jutsu está retornando ' + \
        'um booleano False quando adversary está inconciente.'

    assert naruto.chakra_pool == 100, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo chakra do castador quando o jutsu' + \
        'não foi castado.'

    assert cria_ninja_luan.health_pool == 100, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo hp do adversário quando o jutsu ' + \
        'não foi castado.'


def test_cast_jutsu_ninja_failed_jutsu_not_in_list(
        naruto_rasengan,
        cria_ninja_luan,
        cria_jutsu_chidori):

    naruto, rasengan = naruto_rasengan

    # Testar se o jutsu será lançado sem estar na jutsu_list
    result = naruto.cast_jutsu(cria_jutsu_chidori, cria_ninja_luan)

    assert result is False, 'Verifique se seu método cast_jutsu está retornando ' + \
        'um booleano False quando o jutsu não está na jutsu_list do castador.'

    assert naruto.chakra_pool == 100, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo chakra do castador quando o jutsu' + \
        'não foi castado.'

    assert cria_ninja_luan.health_pool == 100, 'Verifique se seu método ' + \
        'cast_jutsu não está deduzindo hp do adversário quando o jutsu ' + \
        'não foi castado.'
