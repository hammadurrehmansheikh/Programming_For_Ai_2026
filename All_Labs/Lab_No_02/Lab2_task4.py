incomes = [55000, 70000, 80000, 45000, 65000]


employment_status = ["Employed", "Employed", "Unemployed", "Employed", "Employed"]

# Counter
eligible_count = 0


for i in range(len(incomes)):

    if incomes[i] >= 60000 and employment_status[i] == "Employed":
        eligible_count += 1
        print("Applicant", i + 1, ": Eligible")

    else:
        print("Applicant", i + 1, ": Not Eligible")


print("Total Eligible Applicants:", eligible_count)