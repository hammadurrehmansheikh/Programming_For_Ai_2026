temperatures = [18, 25, 32, 28, 35, 22, 31]


normal_count = 0
high_count = 0


for temperature in temperatures:

    if 15 <= temperature <= 30:
        normal_count += 1

    elif temperature > 30:
        high_count += 1


print("Normal Readings:", normal_count)
print("High Readings:", high_count)