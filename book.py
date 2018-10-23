from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('home.html'), 200

@app.route('/Shakespeare/')
def Shakespeare():
  return render_template('introduction.html'), 200

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
       return redirect(url_for('root'))
    else:
       return render_template('login.html'), 200

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

@app.route('/Shakespeare/one/')
def Shakespeare_one():
  return render_template('Shakespeare1.html')

@app.route('/Shakespeare/two/')
def Shakespeare_two():
  return render_template('Shakespeare2.html')

@app.route('/register/')
def register():
  return render_template('register.html'), 200
    
if __name__ == ("__name__"):
    app.run(host='0.0.0.0', debug=True)

