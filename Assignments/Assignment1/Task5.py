readings = [15, 25, 90, 50, 10, 80, 85, 40]

total_alerts = 0

for read in readings:
    if(read < 20 or read > 80):
        total_alerts += 1
Percentage = total_alerts/len(readings) * 100

print("total_alerts : ",total_alerts)

print("Percentage : ",Percentage)