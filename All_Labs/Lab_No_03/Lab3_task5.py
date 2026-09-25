def clean_data(data):
    cleaned_data = []

    for value in data:
        if 0 <= value <= 100:
            cleaned_data.append(value)

    return cleaned_data

class DataAnalysis:

    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def average(self):
        return sum(self.data) / len(self.data)

    def minimum(self):
        return min(self.data)

    def maximum(self):
        return max(self.data)

raw_data = [10, 55, -3, 78, 120, 66, 92]

cleaned_data = clean_data(raw_data)

analysis = DataAnalysis(cleaned_data)

print("Raw Data:", raw_data)
print("Cleaned Data:", cleaned_data)
print("Number of Data Points:", analysis.count())
print("Average:", analysis.average())
print("Minimum:", analysis.minimum())
print("Maximum:", analysis.maximum())