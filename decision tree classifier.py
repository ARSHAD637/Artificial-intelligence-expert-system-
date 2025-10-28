# Import libraries
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create dataset (based on the given figure)
# Features: Outlook, Temperature, Humidity, Windy
# Target: Play (Yes/No)
data = [
    ['Sunny', 85, 85, False, 'No'],
    ['Sunny', 80, 90, True, 'No'],
    ['Overcast', 83, 78, False, 'Yes'],
    ['Rainy', 70, 96, False, 'Yes'],
    ['Rainy', 68, 80, False, 'Yes'],
    ['Rainy', 65, 70, True, 'No'],
    ['Overcast', 64, 65, True, 'Yes'],
    ['Sunny', 72, 95, False, 'No'],
    ['Sunny', 69, 70, False, 'Yes'],
    ['Rainy', 75, 80, False, 'Yes'],
    ['Sunny', 75, 70, True, 'Yes'],
    ['Overcast', 72, 90, True, 'Yes'],
    ['Overcast', 81, 75, False, 'Yes'],
    ['Rainy', 71, 91, True, 'No']
]

# Step 2: Convert to features and labels
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Convert categorical to numeric
from sklearn.preprocessing import LabelEncoder
encoders = [LabelEncoder() for _ in range(len(X[0]))]
for i in range(len(X[0])):
    if isinstance(X[0][i], str) or isinstance(X[0][i], bool):
        col = [row[i] for row in X]
        X_col_encoded = encoders[i].fit_transform(col)
        for j in range(len(X)):
            X[j][i] = X_col_encoded[j]

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)

# Step 5: Display tree
print(export_text(model, feature_names=['Outlook', 'Temp', 'Humidity', 'Windy']))

# Step 6: Predict and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 7: Classify new instance
sample = [['Sunny', 75, 70, False]]
for i in range(len(sample[0])):
    if isinstance(sample[0][i], str) or isinstance(sample[0][i], bool):
        sample[0][i] = encoders[i].transform([sample[0][i]])[0]
print("New prediction:", model.predict([sample[0]])[0])




output
|--- Outlook <= 0.50
|   |--- Windy <= 0.50
|   |   |--- class: No
|   |--- Windy >  0.50
|   |   |--- class: Yes
|--- Outlook >  0.50
|   |--- Temperature <= 1.50
|   |   |--- class: Yes
|   |--- Temperature >  1.50
|   |   |--- class: No

