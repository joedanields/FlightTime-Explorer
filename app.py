from flask import Flask, request, jsonify
import datetime
import json

app = Flask(__name__)

# Sample Flight Data (normally, you would fetch this from a database or file)
flights_data = [
    {"sno": "1", "flight_no": "6e339", "from": "cbe", "to": "chennai", "price": "3605", "discound": "0", "time": "6:35"},
    {"sno": "2", "flight_no": "6e6011", "from": "cbe", "to": "chennai", "price": "3605", "discound": "0", "time": "14:10"},
    {"sno": "3", "flight_no": "6e981", "from": "cbe", "to": "chennai", "price": "3912", "discound": "0", "time": "8:00"},
    {"sno": "4", "flight_no": "6e6918", "from": "cbe", "to": "chennai", "price": "3920", "discound": "0", "time": "10:00"},
    {"sno": "5", "flight_no": "6e6797", "from": "cbe", "to": "chennai", "price": "3920", "discound": "0", "time": "11:35"},
    {"sno": "6", "flight_no": "6e692", "from": "cbe", "to": "chennai", "price": "3920", "discound": "0", "time": "19:50"},
    {"sno": "7", "flight_no": "ai539", "from": "cbe", "to": "chennai", "price": "4209", "discound": "0", "time": "15:10"},
    {"sno": "8", "flight_no": "6e848", "from": "cbe", "to": "chennai", "price": "4235", "discound": "0", "time": "16:00"},
    {"sno": "9", "flight_no": "6e6315", "from": "cbe", "to": "chennai", "price": "4235", "discound": "0", "time": "22:40"},
    {"sno": "10", "flight_no": "ai577", "from": "cbe", "to": "chennai", "price": "8796", "discound": "0", "time": "14:20"}
]

@app.route('/get_flights', methods=['GET'])
def get_flights():
    # Get the query time from the request
    query_time = request.args.get('time')
    
    # Validate and parse time
    try:
        query_time = datetime.datetime.strptime(query_time, "%H:%M")
    except ValueError:
        return jsonify({"error": "Invalid time format. Please use HH:MM."}), 400

    # Find flights within 1 hour range
    result = []
    for flight in flights_data:
        flight_time = datetime.datetime.strptime(flight["time"], "%H:%M")
        time_difference = abs((flight_time - query_time).total_seconds()) / 3600  # Difference in hours
        if time_difference <= 1:
            result.append(flight)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)