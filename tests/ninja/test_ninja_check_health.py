from src.models.ninja_model import Ninja
from pytest import fail


def test_check_health_static_method(cria_ninja_naruto):
    # Não verifica se o metodo é estático
    # assert hasattr(Ninja, 'check_health')
    try:
        result = Ninja.check_health(cria_ninja_naruto)
    except AttributeError:
        fail('Sua classe Ninja não contém o método ESTÁTICO check_health')

    assert result, 'Verifique se sua classe check_health está ' + \
        'retornando o atributo concious corretamente'


def test_check_health_static_method_failed(cria_ninja_naruto):
    cria_ninja_naruto.health_pool = - 100

    try:
        result = Ninja.check_health(cria_ninja_naruto)
    except AttributeError:
        fail('Sua classe Ninja não contém o método ESTÁTICO check_health')

    assert result is False, 'Verifique se sua classe check_health está ' + \
        'retornando o atributo concious corretamente'
