#pip install flask
from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)
car=pd.read_csv("car data.csv")

@app.route('/')
def index():
    Car_Name = sorted(car['name'].unique())
    Year = sorted(car[Year].unique(), reverse=True)
    Kms_Driven = car['Kms_Driven'].unique()
    Fuel_Type = car['Fuel_Type'].unique()
    return render_template('index.html', Car_Name=Car_Name, Year=Year, ms_Driven=ms_Driven, Fuel_Type=Fuel_Type)

if __name__=="__main__":
    app.run(debug=True)    