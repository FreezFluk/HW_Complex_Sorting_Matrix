from flask import Flask,request
from flask_restful import Resource,Api,reqparse
import cmath

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('number_1')
parser.add_argument('number_2')

def ConvertStringToComplexNumber(num1 , num2, want):
	num1 = complex(num1)
	num2 = complex(num2)
	if(want == 'Add'):
		return num1 + num2
	elif(want == 'Sub'):
		return num1 - num2
	elif(want == 'Multiply'):
		return  num1 * num2
	else:
		return 'Error'

class AddComplexNumber(Resource):
	def post(self):
		args = parser.parse_args()
		num1 = args['number_1']
		num2 = args['number_2']
		result = str(ConvertStringToComplexNumber(num1 , num2 , 'Add'))
		return {"complex_number_result":result}

class SubComplexNumber(Resource):
	def post(self):
		args = parser.parse_args()
		num1 = args['number_1']
		num2 = args['number_2']
		result = str(ConvertStringToComplexNumber(num1 , num2 , 'Sub'))
		return {"complex_number_result":result}

class MultiplyComplexNumber(Resource):
	def post(self):
		args = parser.parse_args()
		num1 = args['number_1']
		num2 = args['number_2']
		result = str(ConvertStringToComplexNumber(num1 , num2 , 'Multiply'))
		return  {"complex_number_result":result}

api.add_resource(AddComplexNumber,'/Add')
api.add_resource(SubComplexNumber,'/Sub')
api.add_resource(MultiplyComplexNumber,'/Multiply')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
