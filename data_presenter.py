# problem 2 
data = open('./CupcakeInvoices.csv')

# problem 3
for row in data:
    print(row)

# problem 4
for row in data:
    values = row.split(',')
    print(values[2])

# problem 5
for row in data:
    values = row.split(',')
    total = int(values[3]) * float(values[4])
    print(total)

# Problem 6
total = 0
for row in data:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))
print(total)

# Problem 7

data.close()

