from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    csv_writer = csv.writer(open("users.csv","a"))
    csv_writer.writerow([infos['name']])

    return