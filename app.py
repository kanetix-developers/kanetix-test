from flask import Flask, jsonify, render_template
import requests

from services.rating import RatingService

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'


@app.route('/rates')
def rates():
    return render_template('rates.html')


@app.route('/api/rates')
def api_rates():
    rating = RatingService()
    rates = rating.get_rates()

    return jsonify(rates)


@app.route('/api/company/<id>')
def api_company(id):

    company_details = {
        '1': {'name': 'Allstate', 'phone': '1-888-333-3121'},
        '2': {'name': 'TD Insurance', 'phone': '1-888-558-5832'},
        '3': {'name': 'Belairdirect', 'phone': '1-888-784-1256'},
        '4': {'name': 'Sonnet', 'phone': '1-905-578-3121'},
        '5': {'name': 'RBC Insurance', 'phone': '1-416-225-8778'},
    }

    return jsonify(company_details[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
