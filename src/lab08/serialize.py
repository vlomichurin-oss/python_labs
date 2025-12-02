import json
from models import Student

def students_to_json(students, path):
    data = [s.to_dict() for s in students] 
    with open(path, "w", encoding="utf-8") as fw:
        fw.write(json.dumps(data, ensure_ascii=False, indent=2))

def students_from_json(path):
    with open(path, "r", encoding="utf-8") as fr:
        data =json.load(fr)
    return [Student.from_dict(d) for d in data]