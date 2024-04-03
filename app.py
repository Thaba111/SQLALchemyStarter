from flask import Flask

# tag 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/welcome')
def welcome_message():
    return 'Welcome to my app. Need a tour ? '

if __name__ == '__main__':
    app.run()

'''
How flask works under the hood 
1. Routing : defining url routes and associating them with python functions (View Functions)
MVT -> software architecture pattern (Models : data holders, Views : functions to work on the data
 and Templates : views (html) -> React/Vue)
2. Request handling : matching the requested route to the defined route and executing the corresponding function.
3. Templates : Flask will allow generation of HTML elements 
4. Extensions : https://pypi.org/search/?c=Framework+%3A%3A+Flask :: these add additional functionality to your project. 
FLASK SQL ALCHEMY : database integration. 


- To DO list application 
- Blog app
- RestFUL API's 
- E-commerce store. 


'''