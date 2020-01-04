from voteapp import app

@app.route('/')
def main_page():
	return "Main Page"

@app.route('/vote')
def vote():
	return "Vote"

@app.route('/results')
def results():
	return "results"

@app.route('/info/<int:submission_id>')
def info():
	return "info"
