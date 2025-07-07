# Chronic Kidney Disease (CKD) Prediction Project

This project is a complete pipeline for predicting Chronic Kidney Disease using machine learning. It includes data preprocessing, model training, evaluation, and a Flask web application for user-friendly predictions.

## Project Structure

```
kidney_disease/
│
├── App/
│   ├── app.py                # Flask backend for prediction web app
│   ├── model/
│   │   ├── model.pkl         # Trained ML model (joblib)
│   │   └── scaler.pkl        # Scaler for input features
│   ├── routes/
│   │   └── __init__.py       # (Optional) Modular routing
│   ├── static/
│   │   ├── css/style.css     # App styling
│   │   └── js/script.js      # Client-side validation
│   └── templates/
│       └── index.html        # Main web page
│
├── Data/
│   ├── cleaned_ckd_data.csv  # Cleaned, processed dataset
│   ├── imp_6_features.csv    # 6-feature dataset for training
│   ├── your_dataset.csv      # Raw dataset
│   ├── your_dataset.xlsx     # Raw dataset (Excel)
│   ├── your_dataset.json     # Raw dataset (JSON)
│   └── raw.py                # Script to generate synthetic data
│
├── Evaluation/
│   ├── best_model_saving.ipynb        # Notebook for saving best model
│   └── evaluation_and_tuning.ipynb    # Model evaluation and hyperparameter tuning
│
├── Training/
│   ├── preprocess_data.ipynb          # Data cleaning and preprocessing
│   └── training_notebook.ipynb        # Model training and saving
│
├── dir.py                  # Script to generate project structure
├── requirements.txt        # Python dependencies
├── python_version.txt      # Python version used
├── README.md               # Project documentation
└── setup.exe               # (Placeholder)
```

## Key Components

### 1. Data Preparation
- **Data/raw.py**: Generates synthetic CKD datasets with 6 important features.
- **Training/preprocess_data.ipynb**: Cleans, encodes, and scales the raw dataset, saving the processed data and scaler.

### 2. Model Training & Evaluation
- **Training/training_notebook.ipynb**: Trains a Logistic Regression model on the 6-feature dataset, evaluates, and saves the model and scaler.
- **Evaluation/evaluation_and_tuning.ipynb**: Compares multiple models (Logistic Regression, SVM, Random Forest, AdaBoost, Gradient Boosting) using GridSearchCV, evaluates metrics, and saves the best model.
- **Evaluation/best_model_saving.ipynb**: Example notebook for saving the best model.

### 3. Web Application
- **App/app.py**: Flask app for user input and prediction. Loads the trained model and scaler, processes user input, and displays prediction results.
- **App/templates/index.html**: User interface for entering features and viewing results.
- **App/static/css/style.css**: Styles the web app.
- **App/static/js/script.js**: Validates user input on the client side.

## Usage

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
2. **Preprocess data**
   - Run `Training/preprocess_data.ipynb` to clean and scale the data.
3. **Train and evaluate models**
   - Use `Training/training_notebook.ipynb` and `Evaluation/evaluation_and_tuning.ipynb` to train and select the best model.
4. **Run the web app**
   ```
   cd App
   python app.py
   ```
   - Open your browser at `http://127.0.0.1:5000/`.

## Input Features for Prediction
- **age**: Age of the patient
- **sc**: Serum Creatinine
- **hemo**: Hemoglobin
- **al**: Albumin
- **bp**: Blood Pressure
- **sg**: Specific Gravity

## Output
- Predicts if a person is likely to have Chronic Kidney Disease (CKD) or not.

## Requirements
- Python 3.11.9
- See `requirements.txt` for all dependencies.

## Notes
- All data and models are for educational/demo purposes.
- For any issues, check the code in the respective notebooks and scripts.
