from flask import Flask, render_template, request
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = 0
    if request.method == 'POST':
        model = pickle.load(open('model.pkl', 'rb'))
        user_input = request.form.get('attenuation')
        prediction = model.predict([[user_input]])
        print(prediction)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)