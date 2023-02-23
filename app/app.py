from flask import Flask, request, Response 
import jsonpickle
import pickle
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(_name_)

# Load the pickled data and store it in a global variable
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
   


@app.route('/api/test', methods=['GET'])
def test():
    # Model code
    response = {'message': 'API hit iimv'}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")





@app.route('/api/testmodel', methods=['POST'])
def process_form():
    input1 = float(request.form['input1'])
    input2 = float(request.form['input2'])
    input3 = float(request.form['input3'])
    input4 = float(request.form['input4'])
    input5 = float(request.form['input5'])
    input6 = float(request.form['input6'])
    input7 = float(request.form['input7'])
    input8 = float(request.form['input8'])
    input9 = float(request.form['input9'])
    input10 = float(request.form['input10'])
    input11 = float(request.form['input11'])
    input12 = float(request.form['input12'])
    input13 = float(request.form['input13']) 

   testdata = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13]
   testdata = np.array(testdata)
   testdata = testdata.reshape(-1,1)
   testdata = np.transpose(testdata)
                    
                    
    data = model.predict([testdata])  
    data_str = ", ".join(str(x) for x in data)
    return data_str


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
