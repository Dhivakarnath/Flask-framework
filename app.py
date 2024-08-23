# ###1st Tutorial
# from flask import  Flask 

# ### WSGI application 

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Vanakkam this is Dhivu"

# if __name__=="__main__":
#     app.run(debug=True)


###### Dynamic URL
 
from flask import  Flask , redirect , url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to results page"

@app.route('/passed/<int:score>')
def passed(score):
    return "You passed in the exam and your mark is " + str(score)

@app.route('/failed/<int:score>')
def failed(score):
    return "You failed in the exam and your mark is " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks > 40 :
        result = "passed"
    else :
        result = "failed"
    return redirect(url_for(result , score = marks))    

if __name__=="__main__":
    app.run(debug=True)

     
