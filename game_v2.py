import numpy as np


def smart_predict(number: int) -> int:
    """Бинарный поиск загаданного числа."""
    count, low, high = 0, 1, 100

    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid < number:
            low = mid + 1
        elif mid > number:
            high = mid - 1
        else:
            return count


def score_game(predict_func) -> int:
    """Оценивает среднее число попыток угадывания."""
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    return int(np.mean([predict_func(num) for num in random_array]))


if __name__ == "__main__":
    print(f"Среднее число попыток: {score_game(smart_predict)}")