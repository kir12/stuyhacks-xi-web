from voteapp import db
class Submission(db.Model):
	project_title = db.Column(db.String(64),unique=True)
	description=db.Column(db.String(64))
	github_url=db.Column(db.String(64),unique=True)
	votes=db.Column(db.Integer)
	project_id=db.Column(db.Integer,primary_key=True)
	authors = db.relationship('Contributor',backref="submission",lazy='dynamic')
	def __repr__(self):
		return self.project_title  
class Contributor(db.Model):
	first_name=db.Column(db.String(64))
	last_name=db.Column(db.String(64))
	project = db.Column(db.Integer,db.ForeignKey('submission.project_id'))
	contributor_id=db.Column(db.Integer,primary_key=True)
	def __repr__(self):
		return first_name+" "+last_name
