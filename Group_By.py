from functools import reduce
from collections import defaultdict
Persons = [
    {"Name": "Ali", "FatherName": "Khan", "Age": 30, "Location": "Gulberg"},
    {"Name": "Sara", "FatherName": "Ahmed", "Age": 27, "Location": "Defence"},
    {"Name": "Usman", "FatherName": "Arshad", "Age": 32, "Location": "Shahdra"},
    {"Name": "Amina", "FatherName": "Hussain", "Age": 22, "Location": "Model Town"},
    {"Name": "Ahmed", "FatherName": "Rasheed", "Age": 28, "Location": "Gulberg"},
    {"Name": "Zara", "FatherName": "Siddique", "Age": 31, "Location": "Defence"},
    {"Name": "Hassan", "FatherName": "Malik", "Age": 26, "Location": "Gulberg"},
    {"Name": "Fatima", "FatherName": "Rizvi", "Age": 29, "Location": "Shahdra"},
    {"Name": "Bilal", "FatherName": "Azam", "Age": 24, "Location": "Model Town"},
    {"Name": "Hina", "FatherName": "Ali", "Age": 33, "Location": "Defence"}
]


def GroupByFunc(list,key):
    output_list = {}
    for item in list:
        if output_list.keys().__contains__(item[key]):
            output_list[item[key]].append(item)
        else:
            output_list[item[key]] = []
            output_list[item[key]].append(item)
    return output_list


key = input("Enter the key to group the records: ")
final_result = GroupByFunc(Persons, key)
final_result2 = reduce(lambda output_list, record: output_list[record["Location"]].append(record) or output_list if record["Location"] in output_list else output_list.update({record['Location']: [record]}) or output_list, Persons, defaultdict(list))
print(final_result2)
