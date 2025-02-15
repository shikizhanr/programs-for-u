from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import csv

Base = DeclarativeBase()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    course = Column(String, nullable=False)
    grade = Column(Float, nullable=False)


engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class StudentDB:
    def __init__(self):
        self.session = Session()

    def insert_from_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = Student(
                    last_name=row['Фамилия'],
                    first_name=row['Имя'],
                    faculty=row['Факультет'],
                    course=row['Курс'],
                    grade=float(row['Оценка'])
                )
                self.session.add(student)
            self.session.commit()

    def get_students_by_faculty(self, faculty_name):
        return self.session.query(Student).filter_by(faculty=faculty_name).all()

    def get_unique_courses(self):
        return self.session.query(Student.course).distinct().all()

    def get_average_grade_by_faculty(self, faculty_name):
        avg_grade = self.session.query(func.avg(Student.grade)).filter_by(faculty=faculty_name).scalar()
        return avg_grade if avg_grade else 0

    def get_students_below_grade(self, course_name, threshold=30):
        return self.session.query(Student).filter(Student.course == course_name, Student.grade < threshold).all()

