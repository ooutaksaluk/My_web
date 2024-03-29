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
            return redirect(url_for('calculate_water_cost', area='Bangkok'))
        else:
            return redirect(url_for('calculate_water_cost', area='Other'))
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

@app.route('/calculate_water_cost/<area>', methods=['GET', 'POST'])
def calculate_water_cost(area):
    if request.method == 'POST':
        water_usage = float(request.form['water_usage'])
        if area == 'Bangkok':
            rate_per_unit = calculate_rate_bangkok(water_usage)
        else:
            rate_per_unit = calculate_rate_other(water_usage)

        service_charge = 50  
        tax_rate = 0.07  

        water_cost = (water_usage * rate_per_unit) + service_charge
        total_cost = water_cost * (1 + tax_rate)

        return render_template('page8.html', water_cost=water_cost, total_cost=total_cost)

    return render_template('calculate_water_cost.html', area=area)

def calculate_rate_bangkok(water_usage):
    if water_usage <= 30:
        return 8.50
    elif water_usage <= 40:
        return 10.03
    elif water_usage <= 50:
        return 10.35
    elif water_usage <= 60:
        return 10.68
    elif water_usage <= 70:
        return 11.00
    elif water_usage <= 80:
        return 11.33
    elif water_usage <= 90:
        return 12.50
    else:
        return 12.50  
    
def calculate_rate_other(water_usage):
    if water_usage <= 30:
        return 8.50
    elif water_usage <= 40:
        return 10.03
    elif water_usage <= 50:
        return 10.35
    elif water_usage <= 60:
        return 10.68
    elif water_usage <= 70:
        return 11.00
    elif water_usage <= 80:
        return 11.33
    elif water_usage <= 90:
        return 12.50
    else:
        return 12.50

@app.route('/page9', methods=['GET', 'POST'])
def page9():
    if request.method == 'POST':
        return redirect(url_for('thank_you'))
    return render_template('page9.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)