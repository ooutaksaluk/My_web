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
    if request.method == 'POST':
        location = request.form['location']
        if location == 'bangkok':
            return redirect(url_for('page8', area='Bangkok'))
        else:
            return redirect(url_for('page8', area='Other'))
    return render_template('page4.html')

@app.route('/page5', methods=['GET', 'POST'])
def page5():
    if request.method == 'POST':
        size = request.form['size']
        return redirect(url_for('get_month'))
    return render_template('page5.html')

@app.route('/page6', methods=['GET', 'POST'])
def page6():
    if request.method == 'POST':
        year = request.form['year']
        month = request.form['month']
        return redirect(url_for('thank_you'))
    return render_template('page6.html')

@app.route('/page7', methods=['GET', 'POST'])
def page7():
    if request.method == 'POST':
        water_usage = float(request.form['water_usage'])
        return redirect(url_for('calculate_water_cost', water_usage=water_usage))
    return render_template('page7.html')

if __name__ == '__main__':
    app.run(debug=True)