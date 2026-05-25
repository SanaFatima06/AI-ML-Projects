from flask import Flask, render_template, request
import joblib   # ✅ change from pickle to joblib

app = Flask(__name__)

# load model + vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]

    data = vectorizer.transform([message])
    prediction = model.predict(data)[0]

    result = "SPAM 🚨" if prediction == 1 else "NOT SPAM ✅"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)