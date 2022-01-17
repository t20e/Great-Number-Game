from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = "15dsv65w4TEG5V$G5Bfg5RSVs"


@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    if 'guess' not in session:
        session['guess'] = None
    if 'num' not in session:
        session['num'] = random.randint(1,1000)
    print(str(session['num']) + '*')
    return render_template('main_page.html')

@app.route('/guessed', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    session['high_or_low'] = 'guess'

    session['count'] = session['count'] + 1

    if int(session['guess']) == session['num']:
        session['high_or_low'] = '.rightNUm'
    elif int(session['guess']) - session['num'] >= 500:
        session['high_or_low'] = '.fivehunOver'
    elif int(session['guess']) - session['num'] >= 100:
        session['high_or_low'] = '.hunOver'
    elif int(session['guess']) - session['num'] >= 50:
        session['high_or_low'] = '.fifthOver'
    elif int(session['guess']) - session['num'] >= 20:
        session['high_or_low'] = '.twotiOVer'
    elif int(session['guess']) - session['num'] >= 10:
        session['high_or_low'] = '.tenOVer'
    # below 
    elif int(session['guess']) - session['num'] <= -500:
        session['high_or_low'] = '.fivehunUnder'
    elif int(session['guess']) - session['num'] <= -100:
        session['high_or_low'] = '.hunUnder'
    elif int(session['guess']) - session['num'] <= -50:
        session['high_or_low'] = '.fifthUnder'
    elif int(session['guess']) - session['num'] <= -20:
        session['high_or_low'] = '.twotiUnder'
    elif int(session['guess']) - session['num'] <= -0:
        session['high_or_low'] = '.tenUnder'

    print(session['count'])
    print(session['guess'])
    return redirect('/')

@app.route('/delete_data', methods=['GET'])
def delete_data():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)