from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load('svm_model.pkl')


FEATURE_NAMES = ['Age', 'Sex', 'TSH', 'T4', 'T3', 'USG', 'Fibroscan', 'Hb', 'TLC', 
                 'Plat', 'BUN', 'Creat', 'Hba1c', 'Chol', 'TG', 'LDL', 'HDL', 'ALT', 
                 'ALP', 'AST', 'TB', 'FIB-4', 'APRI', 'Height', 'Weight', 'BMI']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            
            features = []
            for feature in FEATURE_NAMES:
                value = request.form.get(feature)
                features.append(float(value))  
           
            prediction = model.predict([features])[0]
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', features=FEATURE_NAMES, prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)
