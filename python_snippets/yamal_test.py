import yaml

data = [{'name': 'ABCD', 'age': '45', 'cName': 'infosys', 'salary': '75000', 'designation': 'productowner'}, {'name': 'CHANDU', 'age': '22', 'cName': 'IBM', 'salary': '50000', 'designation': 'manager'}, {'name': 'Ashok', 'age': '26', 'cName': 'infosys', 'salary': '40000', 'designation': 'productowner'}, {'name': 'Yuvraj', 'age': '30', 'cName': 'Google', 'salary': '100000', 'designation': 'Developer'}, {'name': 'Swapnali', 'age': '28', 'cName': 'Amazon', 'salary': '75000', 'designation': 'manager'}]

yaml.dump(data, open("test1.yaml", 'w'))