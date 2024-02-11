from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('page3'))
    return render_template('page2.html')

@app.route('/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'POST':
        surname = request.form['surname']
        return redirect(url_for('ask_bangkok'))
    return render_template('page3.html')

@app.route('/page4', methods=['GET', 'POST'])
def page4():

if __name__ == '__main__':
    app.run(debug=True)