🧠 Anxiety Level Prediction based on Digital Activity
This project provides a simple desktop application built with Tkinter that predicts a user's anxiety level (Low, Moderate, High) based on various digital activity metrics. It utilizes machine learning models trained on a mentalhealth.csv dataset to make these predictions.

✨ Features
User-friendly Interface: A minimalist Tkinter GUI for inputting digital activity data.

Anxiety Prediction: Predicts anxiety levels (Low, Moderate, High) using a trained machine learning model.

Machine Learning Backend: Trains and utilizes Ridge Classifier, RandomForest Classifier, and XGBoost Classifier to determine the best performing model.

Data Preprocessing: Handles missing values and scales input features for optimal model performance.

🚀 Getting Started
Follow these instructions to set up and run the project on your local machine.

Prerequisites
You need Python 3.x installed on your system.
You will also need the following Python libraries:

pandas

scikit-learn

xgboost

tkinter (usually comes with Python)

You can install the required libraries using pip:

pip install pandas scikit-learn xgboost

Project Structure
Make sure your project directory is organized as follows:

MENTAL WELLBEING BASED ON DIGITAL ACTIVITY/
├── frontend.py
├── project.py
└── mentalhealth.csv

frontend.py: Contains the Tkinter GUI for user interaction.

project.py: Contains the machine learning model training and prediction logic.

mentalhealth.csv: The dataset used for training the anxiety prediction model.

Installation
Clone the repository (or download the files):
If you have a Git repository, clone it:

git clone <your-repository-url>
cd MENTAL WELLBEING BASED ON DIGITAL ACTIVITY

Otherwise, ensure you have frontend.py, project.py, and mentalhealth.csv in the same directory.

Install dependencies:

pip install pandas scikit-learn xgboost

Running the Application
To start the anxiety prediction application, simply run the frontend.py script:

python frontend.py

A desktop window will appear where you can enter your digital activity data and get an anxiety level prediction.

💻 How it Works
Data Loading & Preprocessing:

The project.py script loads the mentalhealth.csv dataset.

It fills any missing numerical values with the mean of their respective columns.

Features are scaled using StandardScaler to normalize their ranges.

The anxiety_level target variable is binned into "Low", "Moderate", and "High" categories for classification.

Model Training:

The data is split into training and testing sets.

Three classification models are trained: Ridge Classifier, RandomForest Classifier, and XGBoost Classifier.

The model with the highest accuracy on the test set is selected as the best_model.

Prediction:

The frontend.py GUI collects user input for digital activity metrics.

This input data is then scaled using the same scaler used during training.

The best_model predicts the anxiety level based on the scaled input.

The prediction (0, 1, or 2) is mapped to "Low Anxiety", "Moderate Anxiety", or "High Anxiety" and displayed to the user.

🛠️ Technologies Used
Python 3.x

Tkinter: For the graphical user interface.

Pandas: For data manipulation and analysis.

Scikit-learn: For machine learning model training, preprocessing, and evaluation.

XGBoost: For the XGBoost Classifier model.

📈 Future Improvements
More Robust UI: Implement more advanced Tkinter widgets or consider a web-based framework (e.g., Flask, Django) for a richer user experience.

Model Persistence: Save the trained model and scaler to a file (e.g., using joblib or pickle) so they don't need to be retrained every time the application starts.

Error Handling: More specific input validation and user feedback.

Dataset Expansion: Use a larger and more diverse dataset for training to improve model accuracy and generalization.

Feature Engineering: Explore creating new features from existing ones to potentially improve model performance.

User Authentication and Data Storage: For a production application, implement user accounts and securely store user data and predictions.
