from flask import Flask, render_template, request
import pandas as pd
import os
import glob
from customer_churn.utils.main_utils import load_object
from customer_churn.constants import *

app = Flask(__name__)

# --- Purana logic jo prediction mein best tha ---
def get_latest_model_path():
    """
    Automatically detects the model path inside the artifact folder.
    """
    base_path = "artifact/model_trainer/trained_model"
    model_path = os.path.join(base_path, "model.pkl")
    
    if not os.path.exists(model_path):
        # Agar static path nahi mila, tabhi glob use karein
        list_of_folders = glob.glob("artifact/*")
        if not list_of_folders:
            raise FileNotFoundError("No artifact folders found!")
        latest_folder = max(list_of_folders, key=os.path.getctime)
        model_path = os.path.join(latest_folder, "model_trainer", "trained_model", "model.pkl")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")
        
    return model_path

# Load the model
try:
    model_path = get_latest_model_path()
    print(f"Loading model from: {model_path}")
    model = load_object(model_path)
except Exception as e:
    print(f"CRITICAL ERROR: Could not load model. {e}")
    model = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# GET aur POST dono allow kiye taaki browser se prediction route chale
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if model is None:
        return "Model not loaded. Please check the logs."
    
    if request.method == 'GET':
        return render_template('index.html')
    
    try:
        # Purana data dictionary format jo aapke liye best kaam kar raha tha
        data = {
            'Tenure Months': [float(request.form['tenure'])],
            'Monthly Charges': [float(request.form['monthly_charges'])],
            'Contract': [request.form['contract']],
            'Partner': [request.form.get('partner', 'No')], 
            'Internet Service': [request.form.get('internet_service', 'DSL')],
            'Tech Support': [request.form.get('tech_support', 'No')]
        }
        df = pd.DataFrame(data)
        
        # Prediction
        prediction = model.predict(df)
        result = "Churn" if prediction[0] == 1 else "No Churn"
        
        return render_template('index.html', prediction=result)
    except Exception as e:
        return f"Prediction Error: {e}"

if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)




# from flask import Flask, render_template, request
# import pandas as pd
# import os
# import glob
# from customer_churn.utils.main_utils import load_object
# from customer_churn.constants import *

# app = Flask(__name__)

# # Function to get the latest model path automatically
# def get_latest_model_path():
#     """
#     Automatically detects the latest artifact folder and returns the model path.
#     """
#     base_path = "artifact"
#     # Sabse naye folder ka path dhoondhein
#     list_of_folders = glob.glob(os.path.join(base_path, '*'))
#     if not list_of_folders:
#         raise FileNotFoundError("No artifact folders found!")
    
#     latest_folder = max(list_of_folders, key=os.path.getctime)
    
#     # Model file ka path construct karein
#     model_path = os.path.join(latest_folder, "model_trainer", "trained_model", "model.pkl")
    
#     if not os.path.exists(model_path):
#         raise FileNotFoundError(f"Model file not found at: {model_path}")
        
#     return model_path

# # Load the model object with error handling
# try:
#     model_path = get_latest_model_path()
#     print(f"Loading model from: {model_path}")
#     model = load_object(model_path)
# except Exception as e:
#     print(f"CRITICAL ERROR: Could not load model. {e}")
#     model = None

# @app.route('/', methods=['GET'])
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return "Model not loaded. Please check the logs."
    
#     try:
#         data = {
#             'Tenure Months': [float(request.form['tenure'])],
#             'Monthly Charges': [float(request.form['monthly_charges'])],
#             'Contract': [request.form['contract']],
#             'Partner': ['No'], 
#             'Internet Service': ['DSL'],
#             'Tech Support': ['No']
#         }
#         df = pd.DataFrame(data)
#         prediction = model.predict(df)
#         result = "Churn" if prediction[0] == 1 else "No Churn"
#         return render_template('index.html', prediction=result)
#     except Exception as e:
#         return f"Prediction Error: {e}"

# if __name__ == "__main__":
#     app.run(host=APP_HOST, port=APP_PORT)