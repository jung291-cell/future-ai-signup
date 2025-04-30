from flask import Flask, request, redirect, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    if email:
        with open('subscribers.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([email])
    return redirect('/thank-you')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
