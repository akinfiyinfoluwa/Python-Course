total = 0
expenses = []
num_expenses = int(input('Enter the number of expenses: '))
for i in range(num_expenses):
    expenses.append(float(input('Enter how much you blasted: ')))

total = sum(expenses)

print('you spent $', total, sep='')