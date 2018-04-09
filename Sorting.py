from flask import Flask,request
from flask_restful import Resource,Api,reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('ListOfNumber')

#wirte in postman
#ListOfNumber = 5,15,1,25,2,0,40,4,22,8
#    Name                      Values
#ListOfNumber 		5,15,1,25,2,0,40,4,22,8

def Bubble(ListNum):
	print(ListNum)
	cv = [int(i) for i in ListNum]
	swap = True
	while(swap):
		swap = False
		for i in range(len(cv)-1):
			if(cv[i] > cv[i+1]):
				temp = cv[i]
				cv[i] = cv[i+1]
				cv[i+1] = temp
				swap = True
	return cv

def Quick(ListNum):
	print(ListNum)
	cv = [int(i) for i in ListNum]
	less = []
	equal = []
	greater = []
	if len(cv) > 1:
		pivot = cv[0]
		for x in cv:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return Quick(less)+equal+Quick(greater)
	else:
		return cv

def Merge(ListNum):
	print(ListNum)
	cv = [int(i) for i in ListNum]
	if len(cv) < 2:
		return cv
	half = len(cv) // 2
	left = Merge(cv[:half])
	right = Merge(cv[half:])
	out = []
	li = ri = 0
	while True:
		if li >= len(left):
			out.extend(right[ri:])
			break
		if ri >= len(right):
			out.extend(left[li:])
			break
		if left[li] < right[ri]:
			out.append(left[li])
			li += 1
		else:
			out.append(right[ri])
			ri += 1
	return out

class BubbleSort(Resource):
	def post(self):
		args = parser.parse_args()
		data = args['ListOfNumber']
		print map(int,data.split(','))
		data = map(int,data.split(','))
		result = str(Bubble(data))
		return {"Then_Result_Bubble_Sort":result}

class QuickSort(Resource):
	def post(self):
		args = parser.parse_args()
		data = args['ListOfNumber']
		print map(int,data.split(','))
		data = map(int,data.split(','))
		result = str(Quick(data))
		return {"Then_Result_Quick_Sort":result}

class MergeSort(Resource):
	def post(self):
		args = parser.parse_args()
		data = args['ListOfNumber']
		print map(int,data.split(','))
		data = map(int,data.split(','))
		result = str(Merge(data))
		return {"Then_Result_Merge_Sort":result}

api.add_resource(BubbleSort,'/Bubble')
api.add_resource(QuickSort,'/Quick')
api.add_resource(MergeSort,'/Merge')

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=5000)

