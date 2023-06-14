from flask import Flask, request, make_response,jsonify
import json
import dbhelper
import apiHelper
import dbcreds
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.post('/api/painting')
def post_new_painting ():
        error=apiHelper.check_endpoint_info(request.json,["artist","date_painted","name","image_url"]) 
        if (error !=None):
         return make_response(jsonify(error), 400)
        results = dbhelper.run_procedure('CAll add_new_artist(?,?,?,?)',[request.json.get("artist"),request.json.get("date_painted"),request.json.get("name"),request.json.get("image_url")])
        if(type(results)==list):
             return make_response(jsonify(results), 200)
        else:
            return make_response(jsonify(results), 500)
        
@app.get('/api/painting') 
def get_all_artist():
    # error=apiHelper.check_endpoint_info(request.args,["artist"]) 
    # if (error !=None):
        #  return make_response(jsonify(error), 400)
    # results = dbhelper.run_procedure('CAll get_all_artist(?)',[request.args.get("artist")])
    results = dbhelper.run_procedure('CAll get_all_artist()',[])
    if(type(results)==list):
            return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 500) 
    
        

if (dbcreds.production_mode == True):
    print("Running in Production Mode")
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing/Development Mode!")
app.run(debug=True)
