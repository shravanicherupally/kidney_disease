import pandas as pd
import numpy as np
import os

# --- Configuration ---
num_ckd_rows = 1500
num_notckd_rows = 1500
output_file_path = r"C:\Users\shiva\kidney_disease\Data\important_6_features_dataset.csv"

# --- Main Script ---
def generate_ckd_dataset_6_features(n_ckd, n_notckd, filename):
    """Generate synthetic CKD dataset with 6 important features."""

    # Ensure directory exists
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # --- CKD Class ---
    ckd_data = {
        'age': np.random.normal(loc=62, scale=13, size=n_ckd).astype(int),
        'sc': np.random.lognormal(mean=1.2, sigma=0.6, size=n_ckd).round(1),
        'hemo': np.random.normal(loc=10.5, scale=1.8, size=n_ckd).round(1),
        'al': np.random.choice([1, 2, 3, 4], size=n_ckd, p=[0.3, 0.4, 0.2, 0.1]),
        'bp': np.random.normal(loc=90, scale=15, size=n_ckd).astype(int),
        'sg': np.random.choice([1.005, 1.010, 1.015], size=n_ckd, p=[0.4, 0.5, 0.1]),
        'classification': 'ckd'
    }
    df_ckd = pd.DataFrame(ckd_data)

    # --- Not CKD Class ---
    notckd_data = {
        'age': np.random.normal(loc=45, scale=15, size=n_notckd).astype(int),
        'sc': np.random.normal(loc=0.9, scale=0.2, size=n_notckd).round(1),
        'hemo': np.random.normal(loc=15.5, scale=1.0, size=n_notckd).round(1),
        'al': 0,
        'bp': np.random.normal(loc=75, scale=8, size=n_notckd).astype(int),
        'sg': np.random.choice([1.020, 1.025, 1.030], size=n_notckd, p=[0.6, 0.3, 0.1]),
        'classification': 'notckd'
    }
    df_notckd = pd.DataFrame(notckd_data)

    # Combine, shuffle, clip
    df = pd.concat([df_ckd, df_notckd], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    df['age'] = df['age'].clip(1, 90)
    df['bp'] = df['bp'].clip(50, 180)
    df['sc'] = df['sc'].clip(0.4, 15.0)
    df['hemo'] = df['hemo'].clip(5, 18)

    # Save
    try:
        df.to_csv(filename, index=False)
        print("\n✅ File created at:", filename)
        print(f"📊 Total rows: {len(df)}")
        print("🔢 Class counts:")
        print(df['classification'].value_counts())
    except Exception as e:
        print("❌ Error saving file:", e)

# --- Run It ---
if __name__ == "__main__":
    generate_ckd_dataset_6_features(
        n_ckd=num_ckd_rows,
        n_notckd=num_notckd_rows,
        filename=output_file_path
    )
