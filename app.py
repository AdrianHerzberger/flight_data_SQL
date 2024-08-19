from flask import Flask, request, jsonify
import data

app = Flask(__name__)
data_manager = data.FlightData('sqlite:///data/flights.sqlite3')

@app.route('/api/flight/<int:flight_id>', methods=['GET'])
def get_flight_by_id(flight_id):
    results = data_manager.get_flight_by_id(flight_id)
    if results:
        return jsonify(results[0]), 200
    else:
        return jsonify({"error": "Flight not found"}), 404

@app.route('/flights', methods=['GET'])
def get_flights_by_date():
    day = request.args.get('day')
    month = request.args.get('month')
    year = request.args.get('year')
    if not day and month and year:
        return jsonify({"error": "Missing date parameters"}), 400    
    if day and month and year:
        results = data_manager.get_flights_by_date(int(day), int(month), int(year))
        return jsonify(results)

@app.route('/delayed_flights/airline', methods=['GET'])
def get_delayed_flights_by_airline():
    airline = request.args.get('airline')
    if not airline:
        return jsonify({"error": "Missing airline parameter"}), 400
    if airline:
        results = data_manager.get_delayed_flights_by_airline(airline)
        return jsonify(results)

@app.route('/api/flights/delayed/airport', methods=['GET'])
def get_delayed_flights_by_airport():
    airport = request.args.get('airport')
    if not airport:
        return jsonify({"error": "Please provide an airport IATA code"}), 400
    if airport:
        results = data_manager.get_delayed_flights_by_airport(airport)
        return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)