from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<name>")
def hello(name):
    return f"Hello {name}"

@app.route("/add", methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        res = num1 + num2
        return render_template("results.html", result=res)
    return render_template("index.html")  # Render form for GET request

if __name__ == "__main__":
    app.run(debug=True)
