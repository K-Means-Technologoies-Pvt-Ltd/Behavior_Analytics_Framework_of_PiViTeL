import pandas as pd

DATA_PATH = "data/processed/pivitel_merged_dataset.csv"


def load_dataset(path):
    """Load the merged dataset"""
    try:
        df = pd.read_csv(path)
        print("Dataset loaded successfully.\n")
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None

def inspect_dataset(df):
    """Inspect dataset structure"""

    print("----- DATASET STRUCTURE -----")

    print("\nDataset Dimensions:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nDataset Columns:")
    print(df.columns)

    print("\nColumn Data Types:")
    print(df.dtypes)


def check_missing_values(df):
    """Check missing values"""

    print("\n----- MISSING VALUES -----")
    print(df.isnull().sum())


def basic_statistics(df):
    """Generate descriptive statistics"""

    print("\n----- BASIC STATISTICS -----")
    print(df.describe())


def main():

    df = load_dataset(DATA_PATH)
    if df is None:
        print("Failed to load dataset. Aborting analysis.")
        return

    inspect_dataset(df)

    check_missing_values(df)

    basic_statistics(df)


if __name__ == "__main__":
    main()