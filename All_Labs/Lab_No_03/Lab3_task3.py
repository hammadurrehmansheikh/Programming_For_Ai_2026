class Dataset:

    def __init__(self, values):
        self.values = values

    def count_data(self):
        return len(self.values)

    # Method to calculate average
    def calculate_average(self):
        return sum(self.values) / len(self.values)


# Dataset
data_values = [12, 18, 25, 30, 22, 27]


dataset = Dataset(data_values)


print("Data:", dataset.values)
print("Number of data points:", dataset.count_data())
print("Average:", dataset.calculate_average())