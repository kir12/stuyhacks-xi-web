from voteapp import app
from flask import render_template, request
from voteapp.models import *
from sqlalchemy import desc #sort by descending

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/vote',methods=['GET','POST'])
def vote():
	#first time submissions
	if(request.method != "POST"):
		submissions = Submission.query.all()
		return render_template("vote.html",context=submissions)
	#people who've submitted a form
	else:
		#attempt to get project object
		selection = int(request.form['submission'])
		obj = Submission.query.filter_by(project_id=selection).first()
		#increment vote if successfull
		if obj is not None:
			obj.votes+=1
			db.session.commit()
			return render_template("vote.html",result={"result":"Thank you for submitting!"})
		#report error if not successfull
		else:
			return render_template("vote.html",result={"result":"Something went wrong..."})
@app.route('/results')
def results():
	submissions = Submission.query.order_by(desc(Submission.votes)).all()
	return render_template("results.html",context=submissions)
@app.route('/info/<int:submission_id>')
def info():
	return "info"
