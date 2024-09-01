from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/market-updates')
def market_updates():
    return render_template('market_updates.html')

@app.route('/pests-prediction')
def pests_prediction():
    return render_template('pests_prediction.html')

@app.route('/disease-prediction')
def disease_prediction():
    return render_template('disease_prediction.html')

@app.route('/weather-insights')
def weather_insights():
    return render_template('weather_insights.html')

@app.route('/virtual-farmer-assistant')
def virtual_farmer_assistant():
    return render_template('virtual_farmer_assistant.html')

@app.route('/government-schemes')
def government_schemes():
    return render_template('government_schemes.html')

@app.route('/knowledge-sharing-forum')
def knowledge_sharing_forum():
    return render_template('knowledge_sharing_forum.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
