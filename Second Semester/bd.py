import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlite3 as dbms
import sys

conn = dbms.connect("students.sqlite3")  # Как оригинально!
cursor = conn.cursor()

with open("11.drop_ddl.sql", 'r', encoding='utf-8') as f:
    drop_ddl = f.read()
with open("11.create_ddl.sql", 'r', encoding='utf-8') as f:
    create_ddl = f.read()
with open("11.insert_dml.sql", 'r', encoding='utf-8') as f:
    insert_dml = f.read()

if True:
    cursor.executescript(drop_ddl)
    conn.commit()

if True:
    cursor.executescript(create_ddl)
    conn.commit()


DeclBase = declarative_base()

engine = sqlalchemy.create_engine('sqlite:///students.sqlite3', echo=False)  # echo=True для логгинга
Session = sessionmaker(bind=engine)
session = Session()


class Program(DeclBase):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", backref="program")
    programs_courses = relationship("Program_course", backref="program")

    def __init__(self, name):
        self.name = name


class Student(DeclBase):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    card = Column(String)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)

    program_id = Column(Integer, ForeignKey('programs.id'))
    marks = relationship("Mark", backref="student")

    def __init__(self, card, surname, name, patronymic, program):
        self.card = card
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.program = program


class Course(DeclBase):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    programs_courses = relationship("Program_course", backref="course")
    marks = relationship("Mark", backref="course")

    def __init__(self, name):
        self.name = name
class Mark(DeclBase):
    __tablename__ = 'marks'
    mark = Column(Integer)

    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)

    def __init__(self, mark, student, course):
        self.mark = mark
        self.student = student
        self.course = course

class Program_course(DeclBase):
    __tablename__ = 'programs_courses'
    semester_number = Column(Integer, primary_key=True)

    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    program_id = Column(Integer, ForeignKey('programs.id'), primary_key=True)

    def __init__(self, semester_number, course, program):
        self.semester_number = semester_number
        self.course = course
        self.program = program








se = Program("Программная инженерия")
kb = Program("Киберспортивная наука")
ul = Program("Удмуртский язык")
c1 = Course("Филология")
c2 = Course("Физика")
c3 = Course("Программирование")
st1 = Student("002002", "Иванов", "Пётр", "Сидорович",  se)
st2 = Student("002003", "Махнева", "Катя", "Алексеевна",  kb)
st3 = Student( '002004', 'Попов', 'Владимир', 'Алексеевич', ul)
st4 = Student('002014', 'Умников', 'Малыш', 'Эдуардович', kb)
m1 = Mark(4, st4, c1)
m2 = Mark(2, st3, c2)
m3 = Mark(5, st2, c2)
session.add_all([c1, c2, c3, kb, ul, st4, st2, st3, st1])
session.commit()
session.add_all([m1, m2, m3])
session.commit()

print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name, s.surname, s.patronymic, s.card)
    for pc in p.programs_courses:
        print("   - ", pc.program.name, pc.course.name, pc.semester_number)
session.commit()

print("Оценки студентов: ")
for p in session.query(Student):
    print("Студент: ", p.name, p.surname, p.patronymic )
    for g in p.marks:
        print("- ", g.mark)

