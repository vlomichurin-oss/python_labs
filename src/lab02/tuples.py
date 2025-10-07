def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec

    fio_clean = ' '.join(fio.split()).strip()
    group_clean = group.strip()

    parts = fio_clean.split()
    surname = parts[0].title()

    initials = ''.join(f"{name[0].upper()}." for name in parts[1:])

    gpa_str = f"{gpa:.2f}"
    mass = [surname, initials, gpa_str]
    if len(mass) == 3:
        return f"{surname} {initials}, гр. {group_clean}, GPA {gpa_str}"
    else:
        return TypeError
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999Í)))