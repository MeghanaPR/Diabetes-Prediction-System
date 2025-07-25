from flask import Flask, render_template, request
import pickle
import numpy as np
import mysql.connector  # Import MySQL connector for database interaction

# Load the trained model
try:
    with open('diabetes-prediction-rfc-model.pkl', 'rb') as file:
        classifier = pickle.load(file)
except EOFError:
    print("Error: The pickle file is empty or corrupted.")
except FileNotFoundError:
    print("Error: The pickle file was not found.")

# Initialize Flask app
app = Flask(__name__)

# Step 1: Establish MySQL database connection
db = mysql.connector.connect(
    host="localhost",      
    user="root",      
    password="pinki", 
    database="DiabetesPrediction"  
)
cursor = db.cursor()

# Step 2: Define the routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        print("Form data received:", request.form)  # Debugging log
        try:
            pregnancies = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            blood_pressure = int(request.form['blood_pressure'])
            skin_thickness = int(request.form['skin_thickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            DPF = float(request.form['DPF'])
            age = int(request.form['age'])
        except KeyError as e:
            return f"Missing form field: {e}", 400  # Return HTTP 400 error if form field is missing

        # Prepare the data for prediction
        data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DPF, age]])
        my_prediction = classifier.predict(data)[0]  # 0 = Negative, 1 = Positive
        prediction = int(my_prediction)

        # Step 3: Insert the data into the MySQL table
        query = """
            INSERT INTO Predictions (
                pregnancies, glucose, BloodPressure, SkinThickness, insulin, bmi, DPF, age, outcome
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DPF, age, prediction)
        cursor.execute(query, values)
        db.commit()  # Save the changes to the database

        # Render the result page with the prediction
        return render_template('result.html', prediction=prediction)
    
@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

# Step 4: Run the application
if __name__ == '__main__':
    app.run(debug=True)
