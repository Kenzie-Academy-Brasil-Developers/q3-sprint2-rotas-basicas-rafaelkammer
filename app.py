from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.get('/')
def home():
    return {"data":"Hello Flask!"}, 200

@app.get('/current_datetime')
def current_datetime():
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")

    if (int(datetime.now().strftime("%H")) < 12):
        message = "Bom dia!"
    if ((int(datetime.now().strftime("%H")) > 12) and (int(datetime.now().strftime("%H")) < 18)):
        message = "Boa tarde!"
    if (int(datetime.now().strftime("%H")) >= 18):
        message = "Boa noite!"    
    
    return {"current_datetime": date, "message": message}, 200

