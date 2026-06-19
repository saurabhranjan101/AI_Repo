# Step 1: Collect sentences (LIST - flexible, can grow/shrink)
sentences = [
    "AI is powerful",
    "Python is versatile",
    "Data drives decisions"
]

# Add more dynamically
sentences.append("Models learn patterns")

print("Dataset (list of sentences):")
print(sentences)

# Step 2: Define training samples (TUPLES - fixed input-output pairs)
# Each tuple = (features, label)
training_data = [
    ( [0.2, 0.8, 0.5], "Positive" ),
    ( [0.9, 0.1, 0.4], "Negative" ),
    ( [0.5, 0.5, 0.5], "Neutral" )
]

print("\nTraining samples (list of tuples):")
for sample in training_data:
    print(sample)

# Step 3: Simulate feeding into a model
print("\nFeeding data into model loop:")
for features, label in training_data:
    print(f"Features: {features} --> Label: {label}")