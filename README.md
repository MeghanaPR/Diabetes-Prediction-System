🩺 Diabetes Prediction System

A Machine Learning–powered Diabetes Prediction Web Application developed using Python, Random Forest Classifier, Flask, MySQL, and Tableau for visualization. This system helps predict the likelihood of diabetes in patients based on medical input parameters and logs all predictions to a MySQL database for further analytics and insights.

🛠 Tech Stack:

   - Python

   - Flask (Web framework)

   - Random Forest Classifier (Machine Learning model)

   - MySQL (Database for prediction history)

   - Tableau (Visualization dashboard)

   - HTML/CSS (Frontend templates)

🎯 Features:

   🔍 Prediction - Predicts whether a patient is diabetic based on input features:

      - Pregnancies

      - Glucose

      - Blood Pressure

      - Skin Thickness

      - Insulin

      - BMI

      - Diabetes Pedigree Function (DPF)

      - Age

   🗃 Database Logging - Every prediction made through the web app is logged into a MySQL database for record-keeping and analysis.

   📊 Visualization - Includes a /visualize route (template placeholder) to embed or link to Tableau dashboards using historical data stored in MySQL.

🧠 Model Training:

   - Dataset: PIMA Indians Diabetes Dataset

   - Missing values in key medical fields are handled using mean/median imputation.

   - Trained using Random Forest Classifier (n_estimators=20)

   - Saved as diabetes-prediction-rfc-model.pkl for deployment.

📊 Tableau Integration:

    - Data stored in the MySQL Predictions table can be connected to Tableau for interactive dashboards.

    - You can embed the Tableau dashboard in visualize.html using an <iframe> or redirect to an external Tableau public/private link.
