from flask import Flask
from flask import render_template
from flask import request
import master
import json

#Creating app object.
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])

def index():

    #On click of the 'play' button the POST method is activated.
    if request.method == 'POST':

        #Retrieving user form input.
        category = request.form.get('category')
        players = request.form.get('players')

        #Retrieving and processing the API data and result of hand
        active_cards, active_attribute, result  = master.run(category,players)

        return render_template('index.html',
                                api_response = json.dumps(active_cards),
                                attribute = active_attribute,
                                result = result)

    #Return valueless page.                          
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
