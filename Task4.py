cgpas = [3.8 , 3.2 , 3.6 , 3.9 , 3.4]

incomes = [60000 , 50000 , 90000 , 75000 , 40000]

eligible_students = 0

for i in range(len(cgpas)):
    if(cgpas[i] >= 3.5 and incomes[i] <= 80000):
        eligible_students += 1

print("eligible_students : ",eligible_students)
