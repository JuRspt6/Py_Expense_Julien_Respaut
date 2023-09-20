from PyInquirer import prompt
import csv

def get_spenders(*args):
    spenders = []
    with open('users.csv', 'r') as users_file:
        reader = csv.reader(users_file)
        for row in reader:
            spenders.append({"name": row[0]})
    return spenders

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_spenders,
    },
    {
        "type":"checkbox",
        "name":"involved_persons",
        "message":"New Expense - Involved persons: ",
        "choices": get_spenders,
    },

]

def new_expense(*args):
    infos = prompt(expense_questions)
    csv_writer = csv.writer(open("expense_report.csv","a"))
    csv_writer.writerow([infos['amount'], infos['label'], infos['spender'], infos['involved_persons']])

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True