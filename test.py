 
# test.py
from main import StudentsInMLOps

def test_enrollStudents():
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(5)
    assert mlops_class.getTotalStrength() == 5

def test_dropStudents():
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(10)
    mlops_class.dropStudents(3)
    assert mlops_class.getTotalStrength() == 7

def test_getClassName():
    mlops_class = StudentsInMLOps()
    assert mlops_class.getClassName() == "MLOps"
