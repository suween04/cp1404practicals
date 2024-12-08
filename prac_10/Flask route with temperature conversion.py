@app.route("/convert/<float:celsius>")
def convert_temperature(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return f"<h1>{celsius}°C is {fahrenheit}°F</h1>"
