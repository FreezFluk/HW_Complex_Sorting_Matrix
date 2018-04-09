from flask import Flask,request
from flask_restful import Resource,Api,reqparse
import numpy as np
from numpy import linalg as LA

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('A0')
parser.add_argument('A1')
parser.add_argument('A2')
parser.add_argument('B0')
parser.add_argument('B1')
parser.add_argument('B2')

def addSub(a1,a2,a3,b1,b2,b3):
	a = [a1,a2,a3]
	b = [b1,b2,b3]
	for dim1 in range(3):
		for dim2 in range(3):
			b[dim1][dim2] = b[dim1][dim2] * 2
	result = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i][j] = a[i][j] + b[i][j]
	result = map(str,result)
	return result

def multiply(a1,a2,a3,b1,b2,b3):
	a = [a1,a2,a3]
	b = [b1,b2,b3]
	result = np.dot(a,b)
	result = str(result)
	result = map(str,result.split('\n'))
	return result

def hardcore(a1,a2,a3,b1,b2,b3):
	a = [a1,a2,a3]
	a1 = LA.matrix_power(a,2)
	a2 = inverseMatrix(a)
	b = [b1,b2,b3]
	b1 = inverseMatrix(b)
	result1 = np.dot(a1,b1)
	result2 = np.dot(a2,b)
	result3 = np.dot(a,b)
	result = np.add(np.add(result1,result2),result3)
	result = str(result)
	result = map(str,result.split('\n'))
	return result

def inverseMatrix(a):
	a = np.linalg.inv(a)
	return a

class AddSub(Resource):
	def post(self):
		args = parser.parse_args()
		A0 = args['A0']
		A1 = args['A1']
		A2 = args['A2']
		B0 = args['B0']
		B1 = args['B1']
		B2 = args['B2']
		A0 = map(int,A0.split(','))
		A1 = map(int,A1.split(','))
		A2 = map(int,A2.split(','))
		B0 = map(int,B0.split(','))
		B1 = map(int,B1.split(','))
		B2 = map(int,B2.split(','))
		result = addSub(A0,A1,A2,B0,B1,B2)
		return {"Then_Result_AddSub":result}

class Multiply(Resource):
	def post(self):
		args = parser.parse_args()
		A0 = args['A0']
		A1 = args['A1']
		A2 = args['A2']
		B0 = args['B0']
		B1 = args['B1']
		B2 = args['B2']
		A0 = map(int,A0.split(','))
		A1 = map(int,A1.split(','))
		A2 = map(int,A2.split(','))
		B0 = map(int,B0.split(','))
		B1 = map(int,B1.split(','))
		B2 = map(int,B2.split(','))
		result = multiply(A0,A1,A2,B0,B1,B2)
		return {"Then_Result_Multiply":result}

class Hardcore(Resource):
	def post(self):
		args = parser.parse_args()
		A0 = args['A0']
		A1 = args['A1']
		A2 = args['A2']
		B0 = args['B0']
		B1 = args['B1']
		B2 = args['B2']
		A0 = map(int,A0.split(','))
		A1 = map(int,A1.split(','))
		A2 = map(int,A2.split(','))
		B0 = map(int,B0.split(','))
		B1 = map(int,B1.split(','))
		B2 = map(int,B2.split(','))
		result = hardcore(A0,A1,A2,B0,B1,B2)
		return {"Then_Result_Hardcore":result}

api.add_resource(AddSub,'/AddSub')
api.add_resource(Multiply,'/Multiply')
api.add_resource(Hardcore,'/Hardcore')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
