# https://coderun.yandex.ru/problem/median-out-of-three/description?currentPage=1&pageSize=10&rowNumber=1


def get_middle_element(numbers: str):
    numbers_list = list(map(int, numbers.split()))
    return sorted(numbers_list)[1]


if __name__ == '__main__':
    numbers = input()
    print(get_middle_element(numbers))