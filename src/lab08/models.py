from datetime import datetime, date 
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
    