from flask import Flask, render_template
#from app import app
 
app = Flask(__name__)      
 

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
 
if __name__ == '__main__':
  app.run(debug = True)