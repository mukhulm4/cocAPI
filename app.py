##   main.py   ##
from flask import Flask, render_template, request 
import requests

app = Flask(__name__)

def getData(url):
    
    key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM3MThmNGNlLTI5NTEtNDZhOC1iOThjLWRhNTZhNzAxODZmMiIsImlhdCI6MTYyMTc0NjI0Niwic3ViIjoiZGV2ZWxvcGVyL2M2ZmMwNTgzLWIyZDktYWRmNy1hOThhLTY5NGE0MTI1Y2NjYyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExNy4yMjcuMjMuMjIxIiwiMTE3LjIyNy4xMDYuMTQ4Il0sInR5cGUiOiJjbGllbnQifV19.UEFkhIPxUrBnMHeH1hGytfL7UVqJniT2_gFHrjlKMzRLkXnzmRxZmCodptHn_0EUi96bP5leCubtBYf5JkyOpA"
    headers = {
        "Accept" : "application/json", 
        "authorization": f"Bearer {key}"
    }
    response = requests.get(url, headers = headers)
    return response.json()
    

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/SResult", methods = ["GET", "POST"])
def searchRessult():
    cname = request.form["cname"]
    url = f"https://api.clashofclans.com/v1/clans?name={cname}"
    
    jsonData = getData(url)
    
    return render_template("SResult.html", jsonData = jsonData)
    #return jsonData

@app.route("/clan", methods=["GET", "POST"])
def clan():
    tag = request.args.get("name")
    
    url = f"https://api.clashofclans.com/v1/clans/{tag}"
    jsonData = getData(url)
    
    return render_template("clan.html", jsonData = jsonData)
    

if __name__ == "__main__": 
    app.run(debug = True)