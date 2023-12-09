import json
import math
'''
from flask import Flask,Response

# ex-1
# returns True/False whether the given argument is prime

def primality_test(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True

# print(primality_test(int(input("Give a number?:"))))

app= Flask(__name__)


@app.route('/prime_number/<numberstring>')
def prime(numberstring):
    try:
        number = int(numberstring)
        response = {
            "Number": number,
            "isPrime": primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

@app.route('/prime_number')
def error_stub():
    try:
        number = 666
        response = {
            "Message": "Prime beast!",
            "Number": number,
            "isPrime": primality_test(number)
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as parameter",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=404, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response={
        "message":"Invalid endpoint",
        "status":404
    }
    json_response=json.dumps(response)
    http_response=Response(response=json_response,status=404,mimetype="application/json")
    return http_response



if __name__ == '__main__':
     app.run(use_reloader=True, host='127.0.0.1', port=5000)

'''
# ex-2

from flask import Flask, jsonify

app = Flask(__name__)

airport_database = {
    "OTHH": {"Name": "Hamad International Airport", "Location": "Doha"},
    "OOMS": {"Name": "Muscat International Airport", "Location": "Muscat"},
    "VNKT": {"Name": "Tribhuwan International Airport", "Location": "Kathmandu"},
    "OMDB": {"Name": "Dubai International Airport", "Location": "Dubai"},
    "VTBS": {"Name": "Suvarnabhumi Airport", "Location": "Bangkok"},
    "WADD": {"Name": "Ngurah Rai International Airport", "Location": "Bali"}


}

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport = airport_database.get(icao_code)
    if airport is not None:
        return jsonify({"ICAO": icao_code, **airport})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

