from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        text = request.form['text']
        results = predict(text)
        prediction = ""
        c = 0
        for pred in results[0]['confidences']:
            prediction+=pred['label']
            c+=1
            if c==3: break
            prediction+=", "

        return render_template('ui.html', text=text, prediction=prediction)

    else:
        return render_template("ui.html")

def predict(input_text):
    response = requests.post("https://kamrussamad-multilabel-imdb-movie-genre-clas-253b5da.hf.space/run/predict", json={
    "data": [
        input_text
    ]
    }).json()
    result = response["data"]

    return result

if __name__ == '__main__':
    app.run(debug=True)
