from flask import Flask, request, render_template, jsonify
import datetime
import json

app = Flask(__name__)

# Sample flight data (this could come from your JSON file)


flights_data = [
    {"flight_no": "6e338", "from": "CBE", "to": "Chennai", "price": "3605", "time": "06:35"},
    {"flight_no": "6e6011", "from": "CBE", "to": "Chennai", "price": "3605", "time": "14:10"},
    {"flight_no": "6e981", "from": "CBE", "to": "Chennai", "price": "3912", "time": "08:00"},
    {"flight_no": "6e6918", "from": "CBE", "to": "Chennai", "price": "3920", "time": "10:00"},
    {"flight_no": "6e6797", "from": "CBE", "to": "Chennai", "price": "3920", "time": "11:35"},
    {"flight_no": "6e692", "from": "CBE", "to": "Chennai", "price": "3920", "time": "19:50"},
    {"flight_no": "ai539", "from": "CBE", "to": "Chennai", "price": "4209", "time": "15:10"},
    {"flight_no": "6e848", "from": "CBE", "to": "Chennai", "price": "4235", "time": "16:00"},
    {"flight_no": "6e6315", "from": "CBE", "to": "Chennai", "price": "4235", "time": "22:40"},
    {"flight_no": "ai577", "from": "CBE", "to": "Chennai", "price": "8796", "time": "14:20"}
]

# Route to display the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to get flights based on the user input
@app.route('/get_flights', methods=['GET'])
def get_flights():
    query_time = request.args.get('time')
    
    if not query_time:
        return jsonify({"error": "No time parameter provided. Please include 'time' in the query."}), 400
    
    try:
        query_time = datetime.datetime.strptime(query_time, "%H:%M")
    except ValueError:
        return jsonify({"error": "Invalid time format. Please use HH:MM."}), 400

    # Find flights within a 1-hour range
    result = []
    for flight in flights_data:
        flight_time = datetime.datetime.strptime(flight["time"], "%H:%M")
        time_difference = abs((flight_time - query_time).total_seconds()) / 3600
        if time_difference <= 1:
            result.append(flight)

    return render_template('index.html', flights=result, query_time=query_time)

if __name__ == "__main__":
    app.run(debug=True)
