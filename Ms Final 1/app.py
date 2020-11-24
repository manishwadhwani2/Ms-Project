from flask import Flask, request, render_template
from flask_cors import cross_origin
import pandas as pd

app = Flask(__name__)



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        ph_level = int(request.form["ph_Level(0-14)"])
        x = ph_level
        if(8.5>=x>=7):
            score_ph = 100

        elif (8.6>=x>=8.5):
            score_ph= 80
             

        elif (6.9>=x>=6.8):
            score_ph = 80
            
        elif (8.8>=x>=8.6):
            score_ph = 60
        elif (6.8>=x>=6.7):
            score_ph = 60
        elif (9>=x>=8.8):
            score_ph = 40
        elif (6.7>=x>=6.5):
            score_ph = 40
            
        else:
            score_ph = 0

        # Dissolved Oxygen
        Dissolved_Oxygen = int(request.form["Dissolved_oxygen(mg/l)"])
        y = Dissolved_Oxygen

        if(y>=6):
            score_Do = 100

        elif (6>=y>=5):
            score_Do= 80
             

        elif (5>=y>=4):
            score_Do = 60
            
        elif (4>=y>=3):
            score_Do = 40
            
            
        else:
            score_Do = 0
        Ni = int(request.form['Nitrate(mg/L)'])
        if(20>=Ni>=0):
            score_Ni = 100

        elif (50>=Ni>=20):
            score_Ni= 80
             

        elif (100>=Ni>=50):
            score_ec = 60
            
        elif (200>=Ni>=100):
            score_Ni = 40
            
            
        else:
            score_Ni = 0
        ec=int(request.form['electrical_conductivity(s/m)'])
        if(75>=ec>=0):
            score_ec = 100

        elif (150>=ec>=75):
            score_ec = 80
             

        elif (225>=ec>=150):
            score_ec = 60
            
        elif (300>=ec>=225):
            score_ec = 40
            
            
        else:
            score_ec = 0
        
        Biological_Dissolved_oxygen = int(request.form["Biological_Dissolved_oxygen(mg/l)"])
        bdo =  Biological_Dissolved_oxygen
        if(3>=bdo>=0):
            score_bdo = 100

        elif (6>=bdo>=3):
            score_bdo = 80
             

        elif (80>=bdo>=6):
            score_bdo = 60
            
        elif (125>=bdo>=80):
            score_bdo = 40
            
            
        else:
            score_bdo = 0
        tc = int(request.form['Total_coliform(cfu/ml)'])
        if(5>=tc>=0):
            score_tc = 100

        elif (50>=tc>=5):
            score_tc = 80
             

        elif (500>=tc>=50):
            score_tc = 60
            
        elif (10000>=tc>=500):
            score_tc = 40
            
            
        else:
            score_tc = 0
            
        

        
        water_quality_index = 0.16*score_ph+0.281*score_Do+0.281*score_tc+0.234*score_bdo+0.009*score_ec+0.028*score_Ni
        if(water_quality_index>=50):
            output="Water Sample is fit for drinking"
        else:
            output = "Water Sample is unift for drinking"
        return render_template('home.html',prediction_text=output)


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
