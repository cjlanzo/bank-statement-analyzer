import csv
import spending

def analyze(filename):
    expenses = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row['Debit'] != '':
                date = row['Date']
                description = row['Description']
                amount = row['Debit']
                category = spending.get_category_from_description(description)

                expense = {}
                expense['date'] = date
                expense['description'] = description
                expense['amount'] = amount
                expense['category'] = category
                expenses.append(expense)

    with open('C:/Users/Chris/workspace/statement-analyzer/temp/citi.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'description', 'amount', 'category'])
        writer.writeheader()
        writer.writerows(expenses)