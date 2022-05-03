import pytest_example.SamplePyforTestCase as st
import pytest
import sys

'''
Test File should always start with test_ prifix and
test case function start with test_ prifix

if we write 'python -m pytest' commad in cmd
then it goes inside the folder subfolders run test files
started with prefix test_ and run test function started with test_ prefix
or just use 'py.test' in the same directory
>>>py.test -v (with details) or pytest -v
>>>pytest -v -rxs (with skipped tests msgs) or py.test -v -rxs
>>>pytest -k calc (run all the test wich have calc in their function name
                    can use '-v' or '-v -rxs' for futher details)
>>>pytest -v --capture=no (to get print statements)
'''

@pytest.mark.skip("Skip this test")
def test_calc_add():
    total = st.calc_add(5,6)
    assert total == 11

@pytest.mark.skipif(sys.version_info > (3.5), reason="Skip this test for python version higher than 3.5")
def test_calc_add2():
    total = st.calc_add(2,0)
    assert total == 2

def test_calc_mul():
    print("Tis is multiplication test")
    total = st.calc_mul(5,6)
    assert total == 30


'''
mark category of testcases to run perticular test at a time eg. OS oriented
use command >>>pytest -m Windows -v (windows is a mark category wich we set)
run testcases not marked with windows >>pytest -m "not Windows" -v
'''
@pytest.mark.Windows
def test_windows_1():
    assert True

@pytest.mark.Windows
def test_windows_2():
    assert True

@pytest.mark.Linux
def test_linux_():
    assert True

@pytest.mark.Linux
def test_linux_2():
    assert True

'''
Multiple testcases for one function
'''
@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = st.calc_square(test_input)
    assert result == expected_output
    
'''
Problem: Suppose we need database connection or any initialization for 
         every test case function
         writing connection for db in each function not expected
Solution: Setup and Teardown Models are writen, Setup for connection & initialisation 
          teardown to close the connection
But Pytest provides Fixture for above problem does same as setup and teardown module

It is also called as Dependency Injection

Fixture is explained as follow

import pytest

@pytest.fixture(scope="module") #scope writen to create connection only once
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    db_conn = conn.cursor()
    yield db_conn
    curs.close()
    conn.close()
    print("closing DB")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
'''
