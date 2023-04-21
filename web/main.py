from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        num1 = request.form['num1'].upper()
        num2 = request.form['num2'].upper()
        numr = float(num1) + float(num2)
        print(numr)


    else:
        num1 = ''
        num2 = ''
        numr = ''

    return render_template("homepage.html", resultado=numr)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
