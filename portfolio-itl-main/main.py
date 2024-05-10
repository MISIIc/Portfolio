# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Esecuzione della pagina dei contenuti
@app.route('/')
def index():
    return render_template('index.html')


# Competenze dinamiche
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_python=button_python, button_discord=button_discord)

@app.route('/', methods=['POST'])
def feedback_form():
    feedback_python = request.form.get('email')
    feedback_python_text = request.form.get('text')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)