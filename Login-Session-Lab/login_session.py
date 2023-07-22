from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


login_session = {}

@app.route('/', methods=['GET', 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			quote = request.form['quote']
			author = request.form['author']
			age = request.form['age']
			login_session['quote'] = quote
			login_session['author'] = author
			login_session['age'] = age

			return redirect('/thanks')
		except Exception as e:
			print(f"Error: {e}")
			return redirect('/error')

	return render_template('home.html')

	



@app.route('/error')
def error():


	return render_template('error.html')






@app.route('/display')
def display():
	if 'quote' in login_session and 'author' in login_session and 'age' in login_session:
		return render_template('display.html', login_session=login_session)
	else:
		return redirect('/home')
	

@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)

