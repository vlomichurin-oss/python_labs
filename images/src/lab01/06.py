n = int(input())
ochno = 0
zaochno = 0
for i in range(n):
    mas = input()
    if mas.endswith("True"):
        ochno += 1
    if mas.endswith("False"):
        zaochno += 1
print(f"Очно: {ochno}")
print(f"Заочно: {zaochno}")
