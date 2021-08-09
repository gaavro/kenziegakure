def test_start_mission(cria_jounin_kakashi):
    result = cria_jounin_kakashi.start_mission()
    expected = 'O ninja Kakashi Hatake saiu em missão'

    assert cria_jounin_kakashi.is_in_mission is True, \
        'Verifique se seu método start_mission está atualizando' + \
        ' o atributo is_in_mission para True.'

    assert result == expected, 'Verifique se o seu método ' + \
        'start_mission está retornando a string no formato adequado.'


def test_start_mission_failed(cria_jounin_kakashi):
    cria_jounin_kakashi.start_mission()

    result = cria_jounin_kakashi.start_mission()
    expected = 'O ninja Kakashi Hatake já está em uma missão'

    assert result == expected, 'Verifique se o seu método ' + \
        'start_mission está retornando a string no formato adequado' + \
        ' quando o jounin ja estava em uma missão.'
