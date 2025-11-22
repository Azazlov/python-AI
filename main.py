from flask import Flask, request, render_template
from ai import chat_with_model, load_model

app = Flask(__name__)
load_model()

bigInt = 1<<64


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/req', methods=['POST'])
def req():
    req = request.form.get('req')

    result = chat_with_model(prompt=req)
    think = result['thinking']
    content = result['content']

    return render_template('index.html', thinking = think, content=content, req=req)

app.run(debug=True)