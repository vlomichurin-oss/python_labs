a = input().replace(",", ".")
b = input().replace(",", ".")
num1 = float(a)
num2 = float(b)
summ = num1 + num2
avg = (num1 + num2) / 2
rounded_sum = round(summ, 2)
rounded_avg = round(avg, 2)
print(rounded_sum,rounded_avg)