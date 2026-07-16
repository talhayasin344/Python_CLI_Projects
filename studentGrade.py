student_data=[
    {
        "name":"Ali",
        "subjects-marks":{
            "English":85,
            "Urdu":70,
            "Math":89,
            "Biology":95,
            "Chemistry":92,
        },
        "total_marks": "",
        "percentage": 0,
        "grade": ""
    }
]

subject=[
    {
        "name":"English",
        "marks": 0,
    },{
        "name":"Urdu",
        "marks": 0
    },{
        "name":"Math",
        "marks": 0
    },{
        "name":"Biology",
        "marks": 0
    },{
        "name":"Chemistry",
        "marks": 0
    }
]

grade_number=[
    {
        "minimum": 90,
        "maximum": 100,
        "grade": "A"
    },{
        "minimum": 80,
        "maximum": 89,
        "grade": "B"
    },{
        "minimum": 70,
        "maximum": 79,
        "grade": "C"
    },{
        "minimum": 60,
        "maximum": 69,
        "grade": "D"
    },{
        "minimum": 0,
        "maximum": 59,
        "grade": "F"
    }
]
store_marks=0
total_marks=500
store_grade=""

while True:
    getName=input("What is the name of the student? ").lower().capitalize().strip()
    for i in range(len(subject)):
        subject[i]["marks"]=int(input(f"How many marks does Student get in {subject[i]["name"]}. "))
        store_marks += subject[i]["marks"]
    def storeStudentdata():
        calculate_percent=(store_marks / total_marks) * 100
        for grade in range(len(grade_number)):
            if calculate_percent >= grade_number[grade]["minimum"] and calculate_percent <= grade_number[grade]["maximum"]:
                store_grade=grade_number[grade]["grade"]
                student_data.append({
                    "name": getName,
                    "subjects-marks": {
                        "English": subject[0]["marks"],
                        "Urdu": subject[1]["marks"],
                        "Math": subject[2]["marks"],
                        "Biology": subject[3]["marks"],
                        "Chemistry": subject[4]["marks"]
                    },
                    "total_marks": store_marks,
                    "percentage": calculate_percent,
                    "grade": store_grade
                })

    storeStudentdata()
    store_marks=0
    store_grade=""

    value_confirm=input("Do you want to add another student? (yes/no). ")
    if value_confirm=="no":
        break
    elif value_confirm=="yes":
        continue
    else:
        print("Invalid input")
        break


for i in range(1,len(student_data)):
    print("Student name is", student_data[i]["name"])
    print("Student total marks are", student_data[i]["total_marks"],"/",total_marks)
    print("Student's percentage is ", round(student_data[i]["percentage"], 0),"%", sep="")
    print("Student's grade is", student_data[i]["grade"])