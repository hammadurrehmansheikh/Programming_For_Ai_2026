class RuleClassifier:

    # Constructor
    def __init__(self, threshold):
        self.threshold = threshold

    # Method to classify one value
    def classify(self, value):
        return value >= self.threshold

    # Method to classify a list of values
    def classify_list(self, values):
        results = []

        for value in values:
            results.append(self.classify(value))

        return results


# Sample data
threshold = 60
values = [45, 72, 88, 30, 65]

# Create object
classifier = RuleClassifier(threshold)

# Classify values
results = classifier.classify_list(values)

# Display results
print("Threshold:", classifier.threshold)
print("Values:", values)
print("Classification:", results)