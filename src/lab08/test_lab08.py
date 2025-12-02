from serialize import students_from_json, students_to_json
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
