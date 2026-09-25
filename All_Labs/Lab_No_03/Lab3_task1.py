sensor_readings = [45, 78, -12, 90, 105, 66, 88]


# Function to remove invalid readings
def clean_data(data):
    cleaned_data = []

    for value in data:
        if 0 <= value <= 100:
            cleaned_data.append(value)

    return cleaned_data


# Function to calculate average
def calculate_average(data):
    if len(data) == 0:
        return 0

    total = sum(data)
    average = total / len(data)

    return average


# Calling functions
cleaned_data = clean_data(sensor_readings)
average = calculate_average(cleaned_data)

print("Original Data:", sensor_readings)
print("Cleaned Data:", cleaned_data)
print("Average:", average)