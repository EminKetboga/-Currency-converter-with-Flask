from urllib import response
from flask import Flask,render_template,request
import requests
from sympy import sec


api_key = "e245e2aa9bc51891004ecb24fe25bcf1"
url = "http://data.fixer.io/api/latest?access_key="+ api_key

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():

    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")

        response = requests.get(url)

        infos = response.json()
        firstValues = infos["rates"][firstCurrency]
        secondValues = infos["rates"][secondCurrency]

        result = (secondValues / firstValues ) * float(amount)


        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        
        return render_template("index.html",info = currencyInfo)
        
    else:
            
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
