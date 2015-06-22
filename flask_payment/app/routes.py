from flask import Flask, render_template
 
app = Flask(__name__)      
 

 #opens home when endpoint met
@app.route('/my_twilio_endpoint')
def home():
  return render_template('webformattest.html')
  #return render_template('home.html')


#opens about page when /about endpoint met
@app.route('/about')
def about():
  return render_template('about.html')  
 
if __name__ == '__main__':
  app.run(debug = True, port=80, host = '0.0.0.0')