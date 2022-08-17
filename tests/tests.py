import asyncio
from avito import get_matrix


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]
TRAVERSAL2 = [
    10, 50, 90, 130,
    140, 150, 160, 170,
    180, 200, 210, 220,
    230, 240, 250, 260,
    270, 280, 290, 300,
    320, 330, 340, 350, 360
]


def test_get_matrix_from_server():
    '''
    Четная матрица с сервера
    '''
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL, 'Test 1 fatal'


def test_get_matrix_from_dir():
    '''
    Нечетная матрица из локалки
    '''
    assert asyncio.run(get_matrix(SOURCE_URL, file_name='custom.txt')) == TRAVERSAL2, 'Test 2 fatal'

