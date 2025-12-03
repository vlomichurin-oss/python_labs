# Лабораторная работа №8
## `models.py`
```from datetime import datetime, date 
from dataclasses import dataclass 

@dataclass 
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self): 
        if self.gpa > 5 or self.gpa < 0:
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")
        try:
            self.birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d") 
        except ValueError:
            raise ValueError("Неправильный формат даты рождения, ожидается:ГГГГ-ММ-ДД")
        

    def age(self) -> int:
        b = self.birthdate 
        today = date.today()
        if today.month > b.month:
            return today.year - b.year
        if today.month < b.month:
            return today.year - b.year - 1
        if today.day >= b.day:
            return today.year - b.year
        return today.year - b.year - 1

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate.strftime("%Y/%m/%d"),
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod 
    def from_dict(cls, d: dict):
        fio = d["fio"]
        birthdate = d["birthdate"]
        group = d["group"]
        gpa = d["gpa"]
        return cls(fio, birthdate, group, gpa)

    def __str__(self):
        return f"Student:{self.fio}, {self.age()} years old, group {self.group}, rating {self.gpa}"
```
## `serialize.py`
```import json
from models import Student

def students_to_json(students, path):
    data = [s.to_dict() for s in students] 
    with open(path, "w", encoding="utf-8") as fw:
        fw.write(json.dumps(data, ensure_ascii=False, indent=2))

def students_from_json(path):
    with open(path, "r", encoding="utf-8") as fr:
        data =json.load(fr)
    return [Student.from_dict(d) for d in data]
```
## `test_lab08`
```from serialize import students_from_json, students_to_json
from models import Student

def main():
    s1 = Student("Max Verstappen","1997-09-30", "БИВТ-25-33", 5.0)
    s2 = Student("Fernando Alonso","1981-07-29", "БИВТ-25-14", 4.4)
    s3 = Student("Nikita Mazepin","1999-03-02", "БИВТ-25-1", 1.4)
    students_to_json([s1,s2,s3], "/Users/edna/Desktop/python_labs/data/lab08/students_output.json")
    for s in students_from_json("/Users/edna/Desktop/python_labs/data/lab08/students_input.json"):
        print(s)

if __name__ == '__main__':
    main()
```
## Вывод программы


<img width="663" height="92" alt="lab08exB01" src="https://github.com/user-attachments/assets/381c5b58-2384-4648-ae37-a22491c388b8" />

<img width="358" height="393" alt="lab08exB02" src="https://github.com/user-attachments/assets/2f638771-24c7-4e58-9e6f-bc90637b5388" />
