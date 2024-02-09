from flask import Flask
app = Flask(__name__)

@app.route('nope')
def hello_world():

   return 'ABC’

if __name__ == '__main__':
   app.run()