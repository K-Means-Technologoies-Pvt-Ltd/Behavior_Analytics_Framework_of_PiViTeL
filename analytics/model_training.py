import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_model_dataset.csv"
df = pd.read_csv(DATA_PATH)

print("\nDataset Loaded:", df.shape)

os.makedirs("outputs/model", exist_ok=True)

# ---------------------------------------------------
# SPLIT FEATURES & TARGET
# ---------------------------------------------------

X = df.drop(columns=["high_risk_event"])
y = df["high_risk_event"]

# ---------------------------------------------------
# TRAIN TEST SPLIT
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)

# ---------------------------------------------------
# MODELS
# ---------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = []

# ---------------------------------------------------
# TRAIN & EVALUATE
# ---------------------------------------------------

for name, model in models.items():

    print(f"\n==============================")
    print(f"MODEL: {name}")
    print(f"==============================")

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1 Score:", f1)

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Save confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title(f"{name} - Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.savefig(f"outputs/model/{name.replace(' ', '_')}_confusion_matrix.png")
    plt.close()

    results.append([name, acc, prec, rec, f1])

# ---------------------------------------------------
# SAVE MODEL RESULTS
# ---------------------------------------------------

results_df = pd.DataFrame(
    results,
    columns=["Model", "Accuracy", "Precision", "Recall", "F1 Score"]
)

print("\nFinal Model Comparison:\n")
print(results_df)

results_df.to_csv("outputs/model/model_results.csv", index=False)

# ---------------------------------------------------
# FEATURE IMPORTANCE (RANDOM FOREST)
# ---------------------------------------------------

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

importance = pd.Series(rf.feature_importances_, index=X.columns)
importance = importance.sort_values(ascending=False)

print("\nFeature Importance:\n")
print(importance)

importance.to_csv("outputs/model/feature_importance.csv")

# Plot feature importance
plt.figure()
importance.plot(kind='bar')
plt.title("Feature Importance")
plt.ylabel("Importance Score")

plt.savefig("outputs/model/feature_importance.png")
plt.close()

print("\nAll outputs saved successfully!")