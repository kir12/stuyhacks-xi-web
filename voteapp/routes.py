from voteapp import app
from flask import render_template

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/vote')
def vote():
	return "Vote"

@app.route('/results')
def results():
	return "results"

@app.route('/info/<int:submission_id>')
def info():
	return "info"
