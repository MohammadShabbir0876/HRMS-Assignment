from sqlalchemy.orm import Session
from . import models, schemas

def create_employee(db: Session, emp: schemas.EmployeeCreate):
    employee = models.Employee(**emp.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employees(db: Session):
    return db.query(models.Employee).all()


def delete_employee(db: Session, emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
    return emp


def mark_attendance(db: Session, att: schemas.AttendanceCreate):
    attendance = models.Attendance(**att.dict())
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance


def get_attendance_by_employee(db: Session, emp_id: int):
    return db.query(models.Attendance).filter(models.Attendance.employee_id == emp_id).all()
