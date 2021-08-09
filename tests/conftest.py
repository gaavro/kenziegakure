from pytest import fixture
from src.models.ninja_model import Ninja
from src.models.jutsu_model import Jutsu
from src.models.jounin_model import Jounin
from .helpers import naruto, luan, chidori, rasengan, kakashi


@fixture()
def cria_ninja_naruto():
    return Ninja(**naruto)


@fixture()
def cria_ninja_luan():
    return Ninja(**luan)


@fixture()
def naruto_rasengan(cria_ninja_naruto, cria_jutsu_rasengan):
    cria_ninja_naruto.learn_jutsu(cria_jutsu_rasengan)

    return (cria_ninja_naruto, cria_jutsu_rasengan,)


@fixture()
def cria_jounin_kakashi():
    return Jounin(**kakashi)


@fixture()
def cria_jutsu_rasengan():
    return Jutsu(**rasengan)


@fixture()
def cria_jutsu_chidori():
    return Jutsu(**chidori)
