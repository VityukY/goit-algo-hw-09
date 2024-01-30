import timeit
from find_coins_greedy import find_coins_greedy
from find_coins_min import find_coins_min


def test_calc_algorithm(algorithm, amout):
    def calc_amout():
        return algorithm(amout)

    return timeit.timeit(calc_amout, number=1000)


greeedy_result = find_coins_greedy(1234)
min_result = find_coins_min(1234)

time_greedy = test_calc_algorithm(find_coins_greedy, 1234)
time_min = test_calc_algorithm(find_coins_min, 1234)

with open("readme.md", "w", encoding="utf-8") as fp:
    fp.writelines(
        f"Розрахунок зроблений для видачі здачі для 1234 монет. Для збільшення даних, алгоритми прогнані 1000 разів\n"
    )
    fp.writelines(
        f"Результати прорахнку за жадібним алгоритмом {time_greedy} з результатом {greeedy_result}\n"
    )
    fp.writelines(
        f"Результати прорахнку за динамічним алгоритмом {time_min} з результатом {min_result}\n"
    )
    fp.writelines(
        f"Продуктивнысть на одноразовому прикладі на стороні жадіброго алгоритму. Хоча у випадку безпереровності процесу з запамятовуванняям проміжних результітв, алгоритм динамічного програмування, може дати більш конкурентні результати "
    )
