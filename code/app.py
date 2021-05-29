from flask import Flask, jsonify, request
import flask
import json
#from SpeechToText import SpeechConverter
from invalidInputException import InvalidInputException
from pylib.SpeechToText import SpeechConverter

app = Flask(__name__)

# API call
@app.route('/convert', methods=['POST'])
def convert():
    # Get request data
    request_data = json.loads(request.data)
    try:
        # Collect the input text
        input_text = request_data['input']
    except:
        # raise exception
        raise InvalidInputException('\'data\' keyword is missing.')
    
    # Get output text and return   
    converter = SpeechConverter()
    output_text = converter.getText(input_text)
    return app.response_class(response=json.dumps({'output': output_text}),
                                  status=200,
                                  mimetype='application/json')
 
# Exception handler 
@app.errorhandler(Exception)          
def basic_error(e):
    # Set status code
    if isinstance(e,InvalidInputException):
        status_code = 400
    else:
        status_code = 500
    
    # Return error and status code    
    return app.response_class(response=json.dumps({'Error': str(e)}),
                                  status=status_code,
                                  mimetype='application/json')     
	

if __name__ == '__main__':
    app.run()                                  