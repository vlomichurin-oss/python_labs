<h1>Лабораторная работа №1</h1>
<h2>Задание №1</h2>
<img width="946" height="552" alt="Снимок экрана 2025-09-14 в 17 17 47" src="https://github.com/user-attachments/assets/6413112e-6acb-40b2-afd3-1f5bcaabb19c" />
<h2>Задание №2</h2>
<img width="928" height="510" alt="Снимок экрана 2025-09-14 в 17 18 33" src="https://github.com/user-attachments/assets/af09d389-195e-410f-9308-793c486eff09" />
<h2>Задание №3</h2>
<img width="925" height="580" alt="Снимок экрана 2025-09-14 в 17 19 26" src="https://github.com/user-attachments/assets/9dd98c10-d5bc-4687-9211-8c47d6945cf6" />
<h2>Задание №4</h2>
<img width="947" height="498" alt="Снимок экрана 2025-09-14 в 17 19 51" src="https://github.com/user-attachments/assets/e24c3fad-3611-4957-a75b-3bc4e905931c" />
<h2>Задание №5</h2>
<img width="945" height="567" alt="Снимок экрана 2025-09-14 в 17 20 24" src="https://github.com/user-attachments/assets/b6e00178-90a3-49ac-8d31-f5a2411f6071" />
<h2>Задание №6</h2>
<img width="982" height="618" alt="Снимок экрана 2025-09-14 в 17 22 08" src="https://github.com/user-attachments/assets/111eb0dc-8f7d-4c07-9255-ec8be6649889" />

<h1>Лабораторная работа №2</h1>
<h2>arrays</h2>
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("список пуст")
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError()
        result.extend(row)
    return result

print("min_max:")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))```

<img width="1423" height="777" alt="lab02ex1 1" src="https://github.com/user-attachments/assets/7df2bcf4-3c35-4050-829b-053a25d212fb" />
<img width="656" height="311" alt="lab02ex1 2" src="https://github.com/user-attachments/assets/07ece2af-4876-40c2-b6e2-6462ab1fda1b" />
<h2>matrix</h2>
<img width="1432" height="630" alt="lab02ex2 1" src="https://github.com/user-attachments/assets/f0bd835c-2181-4213-be29-08a002bf2d9f" />
<img width="529" height="290" alt="lab02ex2 2" src="https://github.com/user-attachments/assets/220576ab-f127-47b7-b6b8-3cb8062f1086" />
<h2>tuples</h2>
<img width="1432" height="512" alt="lab02ex3 1" src="https://github.com/user-attachments/assets/aed626f6-8175-4590-8a27-0114bcf432a3" />
<img width="551" height="144" alt="lab02ex3 2" src="https://github.com/user-attachments/assets/19a1132d-117f-4ddc-81a0-f9f424ef50fe" />


