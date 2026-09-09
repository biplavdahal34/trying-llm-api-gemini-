from google import genai
from dotenv import load_dotenv
import os
import sys
import logging
logging.getLogger("google_genai").setLevel(logging.ERROR)
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
app.config['SECRET_KEY'] = "DOUUFP98Y98VOUDGV8O78ODIJFGIU"


load_dotenv()




class MainForm(FlaskForm):
    prompt = StringField("You")


@app.route("/", methods=["GET", "POST"])
def form():
    form = MainForm()
    response=None
    if form.validate_on_submit():
        prompt = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=form.prompt.data 
        )
        response = prompt.text
    return render_template("home.html", form = form, response=response)
    






if __name__ == "__main__":
    app.run(debug=True)
