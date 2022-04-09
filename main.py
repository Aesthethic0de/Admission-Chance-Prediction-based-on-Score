
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
from sklearn.preprocessing import StandardScaler as scaler

app = Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route('/predict', methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #reading the inputs given by user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            if(is_research=='yes'):
                research=1
            else:
                research=0
            filename = 'finalized_model_linear_regression_nonscaled.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))#loading the model
            prediction = loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print(f"prediction is {prediction}")

            return render_template('result.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print("the exception message is ", e)
            return 'something is wrong'
    else:
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)