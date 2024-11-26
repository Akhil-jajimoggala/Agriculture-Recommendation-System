from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import vertexai
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel, Part

app = Flask(__name__)

PROJECT_ID = "gcp-build-and-blog"
credentials = service_account.Credentials.from_service_account_file(
    'vertex-ai-user.json'
)

vertexai.init(
    project=PROJECT_ID,
    location="asia-south1",
    credentials=credentials
)

# Load your trained model (update the path to your actual model file)


@app.route("/")
def home():
    """
    Render the frontend HTML.
    """
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    """
    Handle prediction requests from the frontend.
    """
    model = GenerativeModel("projects/797037723886/locations/asia-south1/endpoints/2276169389403275264")
    try:
        # Parse incoming JSON payload
        data = request.json
        print(type(str(data)))
        soil_quality = data.get("Soil_Quality")
        seed_variety = data.get("Seed_Variety")
        fertilizer = data.get("Fertilizer_Amount_kg_per_hectare")
        sunny_days = data.get("Sunny_Days")
        rainfall = data.get("Rainfall_mm")
        irrigation = data.get("Irrigation_Schedule")

        # Ensure all required fields are provided
        if None in [soil_quality, seed_variety, fertilizer, sunny_days, rainfall, irrigation]:
            return jsonify({"error": "Missing one or more required fields"}), 400
        
        text_input = str(data)

        # Make prediction
        prediction = model.generate_content(text_input)

        prediction_dict = prediction.to_dict()
        final_text = prediction_dict['candidates'][0]['content']['parts'][0]['text'].replace('"','')
        print(final_text,type(final_text))

        # Return the prediction as a JSON response
        return jsonify({"prediction": str(final_text).replace('"','')})

    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
