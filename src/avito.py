from tracemalloc import start
from typing_extensions import final
import aiohttp
import asyncio


async def __parse_matrix(matrix: str) -> list[int]:
    matrix = [[int(el.replace(' ', '')) for el in line.split('|') if el.replace(' ', '').isnumeric()] for line in matrix.split('\n')[1:len(matrix.split(' ')):2] if line]
    return matrix


async def __get_sidelines(original_matrix: list[int], startPos: int, endPos: int) -> list[int]:
    sidelines = []
    sidelines.extend([original_matrix[el][startPos] for el in range(startPos, endPos)])
    sidelines.extend([original_matrix[endPos][el] for el in range(startPos, endPos)])
    sidelines.extend([original_matrix[el][endPos] for el in range(endPos, startPos, -1)])
    sidelines.extend([original_matrix[startPos][el] for el in range(endPos, startPos, -1)])

    return sidelines


async def __get_center_cube(original_matrix: list[int], startPos: int) -> list[int]:
    central_cube = []
    central_cube.extend([
                        original_matrix[startPos][startPos], 
                        original_matrix[startPos + 1][startPos],
                        original_matrix[startPos + 1][startPos + 1],
                        original_matrix[startPos][startPos + 1]
                        ])
    return central_cube


async def get_matrix(url: str, file_name: str = None) -> list[int]:
    if file_name:
        with open(file_name, encoding='utf-8') as file:
            matrix = file.read()
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                try:
                    matrix = await response.text()
                except aiohttp.ClientConnectorError as error:
                    raise ValueError('Connection error')

    matrix = await __parse_matrix(matrix)
    final_matrix = []

    if len(matrix) % 2 == 0:
        for i in range(0, int((len(matrix) - 2) / 2)):
            final_matrix.extend(await __get_sidelines(matrix, i, len(matrix) - i - 1))

        final_matrix.extend(await __get_center_cube(matrix, int((len(matrix) - 2) / 2)))
    else:
        for i in range(0, int((len(matrix) - 1) / 2)):
            final_matrix.extend(await __get_sidelines(matrix, i, len(matrix) - i - 1))

        final_matrix.append(matrix[int((len(matrix) - 1) / 2)][int((len(matrix) - 1) / 2)])

    return final_matrix

