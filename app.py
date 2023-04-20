from flask import Flask, render_template, request

app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html")

# this collects the name in a form and submit it to the game.html
#if there is an error it returns the page, that is why i used try and except
@app.route("/game",methods=["POST"])
def login():
    try:
        name = request.form['name']
    
    except:
        return render_template("index.html")
    
    return render_template("game.html", name=name)


# this collects the answers in a form and submit it to the result.html for grading but it determines that here in app.py
#if there is an error like not filling the form completly it returns the page, that is why i used try and except
@app.route("/result", methods=["POST"])
def result():
    
    try:
        Abuja = request.form['Abuja']
        Nairobi = request.form['Nairobi']
        Algiers = request.form['Algiers']
        Cairo = request.form['Cairo']
        Yaoundé = request.form['Yaoundé']
        Accra = request.form['Accra']
        Tunis = request.form['Tunis']
        Pretoria = request.form['Pretoria']

        count = 0
    

        if Abuja == 'Abuja':
            count +=1
            abuja =f"1: You Got it!. the Capital of Nigeria is Abuja"
        else:
            abuja =f"1: You Failed it!. the Capital of Nigeria is Abuja"

        if Nairobi == 'Nairobi':
            count +=1
            nairobi =f"2: You Got it!. the Capital of Kenya is Nairobi"
        else:
            nairobi =f"2: You Failed it!. the Capital of Kenya is Nairobi"
        
        if Algiers == 'Algiers':
            count +=1
            algiers =f"8: You Got it!. the Capital of Algeria is Algiers"
        else:
            algiers =f"8: You Failed it!. the Capital of Algeria is Algiers" 

        if Cairo == 'Cairo':
            count +=1
            cairo =f"6: You Got it!. the Capital of Eygpt is Cairo"
        else:
            cairo =f"6: You Failed it!. the Capital of Eygpt is Cairo"

        if Yaoundé == 'Yaoundé':
            count +=1
            yaoundé =f"5: You Got it!. the Capital of Camerron is Yaoundé"
        else:
            yaoundé =f"5: You Failed it!. the Capital of Camerron is Yaoundé"

        if Accra == 'Accra':
            count +=1
            accra =f"3: You Got it!. the Capital of Ghana is Accra"
        else:
            accra =f"3: You Failed it!. the Capital of Ghana is Accra"

        if Tunis == 'Tunis':
            count +=1
            tunis =f"7: You Got it!. the Capital of Tunisa is Tunis"
        else:
            tunis =f"7: You Failed it!. the Capital of Tunisa is Tunis"

        if Pretoria == 'Pretoria':
            count +=1
            pretoria =f"4: You Got it!. the Capital of South Africa is Pretoria"
        else:
            pretoria =f"4: You Failed it!. the Capital of South Africa is Pretoria"

        

        

    except:
        print("you have to choose all options")
        return render_template('game.html')

    

    return render_template("result.html", won = count, yaoundé=yaoundé, accra=accra, algiers=algiers, abuja=abuja, nairobi=nairobi, cairo=cairo, tunis=tunis, pretoria=pretoria,)


    # , Abuja=Abuja, Nairobi=Nairobi, Algiers=Algiers, Cairo=Cairo, Yaoundé=Yaoundé, Accra=Accra, Tunis=Tunis, Pretoria=Pretoria