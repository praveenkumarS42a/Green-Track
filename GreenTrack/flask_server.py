from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/schedule')
def schedule():
    return redirect(url_for('static', filename='schedule.html'))

if __name__ == '__main__':
    app.run(port=8000)