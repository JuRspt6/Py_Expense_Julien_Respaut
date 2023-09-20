from PyInquirer import prompt
import csv
from os.path import exists

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
]

def change_balance(*args):
    amount = args[0]
    spender = args[1]
    involved = args[2]

    involved_amount = amount / (len(involved) + 1)
    new_balance = {
        spender: involved_amount
    }
    for person in involved:
        new_balance[person] = -involved_amount
    print(new_balance)
    return new_balance

def update_status(*args):
    amount = float(args[0])
    spender = args[1]
    involved = args[2]

    new_balance = change_balance(amount, spender, involved)

    csv_writer = csv.writer(open("status.csv","a"))

    csv_writer.writerow(new_balance.keys())
    csv_writer.writerow(new_balance.values())
    return

def new_expense(*args):
    infos = prompt(expense_questions)

    spender = infos['spender']

    involved = get_spenders()
    involved.remove({'name': spender})

    question_involved = [{
        "type":"checkbox",
        "name":"involved_persons",
        "message":"New Expense - Involved persons: ",
        "choices": involved,
    }]

    infos.update(prompt(question_involved))
    update_status(infos['amount'], spender, infos['involved_persons'])

    infos['involved_persons'].append(spender)
    csv_writer = csv.writer(open("expense_report.csv","a"))
    csv_writer.writerow([infos['amount'], infos['label'], infos['spender'], infos['involved_persons']])

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    print("Expense Added !")
    return True