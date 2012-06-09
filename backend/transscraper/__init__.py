from flask import Flask
import json
import jsonpickle
from flask import request


from transscraper.structure import Response,Parsed_Request

app = Flask(__name__)

@app.route("/api", methods=['GET','POST'])
def get_data():
    parsed_request = Parsed_Request()
    
    if request.method == 'POST':
        parsed_request.start_address = request.form['start_address']
        parsed_request.destination_address = request.form['destination_address']
        parsed_request.number_people = request.form['number_people']
        parsed_request.car_make = request.form['car_make']
        parsed_request.car_model = request.form['car_model']
    elif request.method == 'GET':
        parsed_request.start_address = request.args.get('start_address', '')
        parsed_request.destination_address = request.args.get('destination_address', '')
        parsed_request.number_people = request.args.get('number_people', '')
        parsed_request.car_make = request.args.get('car_make', '')
        parsed_request.car_model = request.args.get('car_model', '')

    response = Response()
    response.start_address = parsed_request.start_address;
    response.destination_address = parsed_request.destination_address;

    return jsonpickle.encode(response)


@app.route("/get_request_sample", methods=['GET','POST'])
def get_request_type():
    parsed_request = Parsed_Request()
    return jsonpickle.encode(parsed_request)


if __name__ == "__main__":
    app.run(debug=True)