minutes = int(input("Минуты: "))
hours = minutes // 60
rem_minutes = minutes % 60
print(f"{hours}:{rem_minutes:02d}")