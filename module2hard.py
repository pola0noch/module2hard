#Дополнительное практическое задание по модулю: "Основные операторы"
def generate_password(n):
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                pairs.append(f"{i}{j}")

    result = "".join(pairs)
    return result

import random
n = random.randint(3,20)
result = generate_password(n)
print(f"Нужный пароль для числа {n}: {result}")
