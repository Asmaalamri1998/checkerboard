
from flask import Flask, render_template 

app = Flask(__name__)   
@app.route('/')
def parameter():
    return render_template('checkerboard.html',_num1=8, _num2=8)

 
@app.route('/<num>')
def parameter_one(num):
    return render_template('checkerboard.html',_num1=int(num), _num2=8 )

@app.route('/<number1>/<number2>')
def parameter_two(number1,number2):
    return render_template('checkerboard.html',_num1=int(number1), _num2=int(number2))
    




    
    


if __name__=="__main__":   
 app.run(debug=True)    

