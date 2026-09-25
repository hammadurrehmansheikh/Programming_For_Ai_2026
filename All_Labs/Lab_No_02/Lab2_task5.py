speeds = [60, 85, 72, 90, 55, 81, 70, 95]


violations = 0


for speed in speeds:

    if speed > 80:
        print(speed, "km/h - Overspeeding")
        violations += 1
    else:
        print(speed, "km/h - Normal")


total_vehicles = len(speeds)
percentage = (violations / total_vehicles) * 100


print("Total Vehicles:", total_vehicles)
print("Total Violations:", violations)
print("Violation Percentage:", percentage, "%")