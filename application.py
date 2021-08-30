from flask import Flask, request, Response
import json
import help
application = app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'

@app.route("/SubBudge/new", methods=["POST"])
def sub_budget():
    # Get item from the POST body
    req_data = request.get_json()
    Spent = req_data['Spent']
    Budget = req_data['Budget']
    res_data = help.Subtraction(Budget,Spent)

    if res_data is None:
        response = Response(
            "operation can't be done either paramaters aren't supplied or paramaters are invalid",
            status=400,
            mimetype="application/json",
        )
        return response

    # Return response
    response = Response(json.dumps(res_data), mimetype="application/json")
    return response

app.run()