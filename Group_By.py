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


def GroupByFunc(list):
    output_list = {}
    for item in list:
        if output_list.keys().__contains__(item["Location"]):
            output_list[item["Location"]].append(item)
        else:
            output_list[item["Location"]] = []
            output_list[item["Location"]].append(item)
    return output_list


final_result = GroupByFunc(Persons)
print(final_result)
