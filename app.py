from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('Employee_Attrition.pkl', 'rb'))

label_maps = {
    'BusinessTravel': ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'],
    'Department': ['Sales', 'Research & Development', 'Human Resources'],
    'EducationField': ['Life Sciences', 'Other', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources'],
    'Gender': ['Female', 'Male'],
    'JobRole': ['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manufacturing Director',
                'Healthcare Representative', 'Manager', 'Sales Representative', 'Research Director', 'Human Resources'],
    'MaritalStatus': ['Single', 'Married', 'Divorced'],
    'OverTime': ['Yes', 'No']
}

def encode_input(value, category):
    return label_maps[category].index(value)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form

        features = [
            int(data['age']),
            int(data['distance']),
            int(data['income']),
            int(data['hike']),
            int(data['years_total']),
            int(data['years_company']),
            int(data['years_role']),
            int(data['years_promo']),
            int(data['years_manager']),
            encode_input(data['business_travel'], 'BusinessTravel'),
            encode_input(data['department'], 'Department'),
            encode_input(data['education_field'], 'EducationField'),
            encode_input(data['gender'], 'Gender'),
            encode_input(data['job_role'], 'JobRole'),
            encode_input(data['marital_status'], 'MaritalStatus'),
            encode_input(data['overtime'], 'OverTime')
        ]

        prediction = model.predict([features])[0]
        result = "Yes" if prediction == 'Yes' else "No"

        return render_template('index.html', prediction_text=f"Employee Attrition: {result}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
