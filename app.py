from flask import Flask, render_template, request, abort
import requests
import easygui

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        city = request.form['city_name']
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a1e5cc4655f9711d4b948c10de85550c'
        res = requests.get(url.format(city)).json()
        
        try:
            temp = res['main']['temp']
            weather = res['weather'][0]['description']
            humidity = res['main']['humidity']
            temp_min = res['main']['temp_min']
            temp_max = res['main']['temp_max']
            icon = res['weather'][0]['icon']

            return render_template('index.html', temp=temp, weather=weather, humidity=humidity, min=temp_min, max= temp_max, city_name=city, icon=icon)
        except:
            easygui.msgbox("Invalid City Name!", title="simple gui")

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

