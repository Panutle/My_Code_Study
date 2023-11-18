from flask import Flask, render_template, request
import joblib
import numpy as np

loaded_model = joblib.load('App/MM.h5')

happy = {1:'คุณมีความสุขอยู่ในระดับน้อยที่สุด',2:'คุณมีความสุขอยู่ในระดับน้อย',3:'คุณมีความสุขอยู่ในระดับปานกลาง',4:'คุณมีความสุขอยู่ในระดับมาก',5:'คุณมีความสุขอยู่ในระดับมากที่สุด'}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/respon', methods=['POST'])
def resp():
    try:
        aa = []
        for i in range(29):
            num = int(request.form[f'{i+1}'])
            aa.append(num)

        data = np.array([aa])

        res = loaded_model.predict(data)

        return render_template('index.html', result=happy[int(res)])

    except ValueError:
        return render_template('index.html', result='Not Respon')

if __name__ == '__main__':
    app.run(debug=True)



