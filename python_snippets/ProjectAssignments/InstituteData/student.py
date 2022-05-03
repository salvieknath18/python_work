import openpyxl

class Student:

    def __init__(self):
        pass

    def student_info_from_xl(self):
        book = openpyxl.Workbook()
        sheet = book.get_sheet_by_name("student_details")
        for row in range(1,8):
            for col in range(1,8):
                pass