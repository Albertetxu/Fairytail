from flask import Flask, render_template, request
from langchain_google_vertexai import VertexAI
import vertexai

app = Flask(__name__)

# Replace with your actual project ID and region
PROJECT_ID="albert-project-414914"
REGION="europe-west3"

#PROJECT_ID = "your-project-id"  
#REGION = "your-region"

vertexai.init(project=PROJECT_ID, location=REGION)
model = VertexAI(model_name="gemini-pro")

@app.route("/", methods=["GET", "POST"])
def index():
    fairy_tale = ""
    if request.method == "POST":
        language = request.form.get("language")
        age_range = request.form.get("age_range")
        subject = request.form.get("subject")

        prompt = f"""Create a fairy tale in {language} for the age range {age_range} about {subject}.
        """
        
        fairy_tale = model.invoke(prompt)

    return render_template("index.html", fairy_tale=fairy_tale)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
