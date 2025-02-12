from flask import Flask, render_template
from firebase_config import ref

app = Flask(__name__)

@app.route("/")
def index():
    students = ref.get()
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
