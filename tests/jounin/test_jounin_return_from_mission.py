def test_return_from_mission(cria_jounin_kakashi):
    cria_jounin_kakashi.start_mission()

    result = cria_jounin_kakashi.return_from_mission()
    expected = 'O ninja Kakashi Hatake retornou em segurança da missão'

    assert cria_jounin_kakashi.is_in_mission is False, \
        'Verifique se seu método return_from_mission está atualizando' + \
        ' o atributo is_in_mission para False.'

    assert result == expected, 'Verifique se o seu método ' + \
        'return_from_mission está retornando a string no formato adequado.'


def test_return_from_mission_failed(cria_jounin_kakashi):
    result = cria_jounin_kakashi.return_from_mission()
    expected = 'O ninja Kakashi Hatake não está em nenhuma missão no momento'

    assert result == expected, 'Verifique se o seu método ' + \
        'start_mission está retornando a string no formato adequado' + \
        ' quando o jounin não estava em uma missão.'
