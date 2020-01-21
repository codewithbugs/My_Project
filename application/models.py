from application import db, login_manager
from flask_login import UserMixin

class Emp(db.Model, UserMixin):
	empid = db.Column(db.Integer,primary_key=True)
	empname = db.Column(db.String(20),nullable=False)
	emppost = db.Column(db.String(20),nullable=False)
	emppass = db.Column(db.String(20),nullable=False)
 
	def get_id(self):
           return (self.empid)
	
	def ___repr__(self):
		return f"Emp('{self.empname}','{self.emppost}')"

	
