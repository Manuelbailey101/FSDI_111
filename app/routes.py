from flask import Flask         # from the flask module import the flask
                                # class .

app = Flask(__name__)           # create an instance of the Flask class
                                # into the app variable (now an object).


@app.get("/")                   # Flask decorator that creates routes.
def index():                    # Flask calls these "views functions".
    me = {                      # Python dictionary with key/value pairs.
        "first_name": "Manny",
        "last_name": "Bailey",
        "hobbies": "MMA",
        "is_active": True
    }
    return me                   # when a view function return a dict
                                # Flask automatically converts it to
                                #JSON.


