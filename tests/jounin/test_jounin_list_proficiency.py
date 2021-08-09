def test_list_best_proficiency(cria_jounin_kakashi):
    expected = 'Kakashi demonstra maior proficiência em ninjutsu'
    result = cria_jounin_kakashi.list_best_proficiency()

    assert expected == result, 'Verifique se seu método ' + \
        'list_best_proficiency está retornando a string ' + \
        'no formato correto.'
