import csv
from pathlib import Path
from datetime import datetime, date
from typing import List, Optional, Dict, Any

try:
    from src.lab08.models import Student
except ImportError:
    class Student:
        def __init__(self, fio: str, birthdate: date, group: str, gpa: float):
            self.fio = fio
            self.birthdate = birthdate
            self.group = group
            self.gpa = float(gpa)
        
        def __repr__(self):
            return f"Student(fio='{self.fio}', birthdate={self.birthdate}, group='{self.group}', gpa={self.gpa})"
        
        def to_dict(self) -> dict:
            return {
                'fio': self.fio,
                'birthdate': self.birthdate.isoformat(),
                'group': self.group,
                'gpa': str(self.gpa)
            }


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()
    
    def _read_all(self) -> List[Dict[str, str]]:
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    
    def _write_all(self, rows: List[Dict[str, str]]) -> None:
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def _dict_to_student(self, row: Dict[str, str]) -> Student:
        try:
            # Парсим дату из строки
            birthdate = datetime.strptime(row['birthdate'], '%Y-%m-%d').date()
            # Преобразуем GPA в float
            gpa = float(row['gpa'])
            return Student(
                fio=row['fio'],
                birthdate=birthdate,
                group=row['group'],
                gpa=gpa
            )
        except (ValueError, KeyError) as e:
            raise ValueError(f"Ошибка при преобразовании данных: {e}")
    
    def list(self) -> List[Student]:
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = self._dict_to_student(row)
                students.append(student)
            except ValueError as e:
                print(f"Предупреждение: {e}")
        return students
    
    def add(self, student: Student) -> None:
        rows = self._read_all()
        
        for row in rows:
            if row['fio'] == student.fio:
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        rows.append(student.to_dict())
        
        self._write_all(rows)
    
    def find(self, substr: str) -> List[Student]:
        all_students = self.list()
        found_students = []
        
        for student in all_students:
            if substr.lower() in student.fio.lower():
                found_students.append(student)
        
        return found_students
    
    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        original_count = len(rows)
        
        # Фильтруем строки, удаляя те, где ФИО совпадает
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) < original_count:
            # Если количество изменилось, записываем обратно
            self._write_all(rows)
            return True
        
        return False
    
    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                # Обновляем указанные поля
                for field, value in fields.items():
                    if field in ['group', 'gpa', 'birthdate']:
                        if field == 'birthdate' and isinstance(value, date):
                            # Преобразуем дату в строку
                            row[field] = value.isoformat()
                        elif field == 'gpa':
                            # Преобразуем GPA в строку
                            row[field] = str(float(value))
                        else:
                            row[field] = str(value)
                    else:
                        raise ValueError(f"Поле '{field}' не поддерживается для обновления")
                updated = True
                break
        
        if updated:
            self._write_all(rows)
        
        return updated
    
    def stats(self) -> Dict[str, Any]:
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        gpa_values = [student.gpa for student in students]
        
        groups_stats = {}
        for student in students:
            group = student.group
            groups_stats[group] = groups_stats.get(group, 0) + 1
        
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [
            {"fio": s.fio, "gpa": s.gpa}
            for s in sorted_students[:5]
        ]
        
        return {
            "count": len(students),
            "min_gpa": min(gpa_values),
            "max_gpa": max(gpa_values),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups_stats,
            "top_5_students": top_5
        }
    
    def clear(self) -> None:
        """Очистить все записи (оставить только заголовок)"""
        self._write_all([])

