def factorize_all(numbers):
    def factorize(number):
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return (f"{number}={i}*{number // i}")

    result = []
    for number in numbers:
        result.append(factorize(number))

    return result
