def format_record(s):
    if len(s) != 3:
        return 'ValueError'
    else:
        fio = s[0].split()
        group = s[1]
        gpa = s[2]
        if type(s[2]) != float:
            return 'TypeError'
        else:
            if len(fio) == 2:
                return f'"{fio[0]} {fio[1][0]}., гр. {group}, GPA {gpa:.2f}"'
            elif fio[0] != fio[0].title() and len(fio) == 2:
                return f'"{fio[0].title()} {fio[1][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            elif fio[0] != fio[0].title() and len(fio) == 3:
                return f'"{fio[0].title()} {fio[1][0].title()}.{fio[2][0].title()}., гр. {group}, GPA {gpa:.2f}"'
            else:
                return f'"{fio[0]} {fio[1][0]}.{fio[2][0]}., гр. {group}, GPA {gpa:.2f}"'


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))