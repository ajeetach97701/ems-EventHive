import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle, json
import Recomender

# with open('recomend.pickle', 'rb') as f:
#     model = pickle.load(f)
    
# Create flask app
flask_app = Flask(__name__)

@flask_app.route("/response", methods = ["GET","POST"])
def response():
    data = request.json
    EventType = data['EventType']
    City = data['City']
    return jsonify({'message': 'Data received'})
   
   
@flask_app.route("/", methods = ["GET","POST","PUT"])
def predict():
    receivedData = request.json
    EventType = receivedData['EventType']
    City = receivedData['City']
    # print("Data from flutter is: EventType = {} and city = {}".format(EventType, City))
    data = Recomender.recomend(EventType, City)
    if not data:
        return jsonify({'error': 'No recommendations found for the input'})
    response_data = {
        'data': '{}'.format(data),
        'message': 'Data received and processed successfully',
            # 'data': data,
            # 'data': '{}'.format(data),
        }
    return jsonify(response_data)

if __name__ == "__main__":
    flask_app.run(debug=True)



# print(Recomender.recomend("Marriage", "Sarajevo"))