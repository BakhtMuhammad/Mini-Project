from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

#APIs Links
programSessions= requests.get("https://cms.mlcs.xyz/api/view/program_sessions/all/")
studentOf= requests.get("https://cms.mlcs.xyz/api/view/students_of/bscs-2016/all/")
teachingStaff= requests.get("https://cms.mlcs.xyz/api/view/teaching_staff/all/")

#Array declaration for Team Members


@app.route ("/index", methods=['GET','POST'])
def index():
	if request.method=="POST":
		DataList = request.json
		if DataList != None:
			global FData
			FData = DataList
			global li
			li = [FData["Teacher"], FData["Leader"],FData["TMembers"], FData["Session"]]
			return redirect(url_for("result"  ))
		else:
			return redirect(url_for("result" ))
	else:
		return render_template("index.html", STD=teachingStaff.json(), sess = programSessions.json(), mds = studentOf.json())

@app.route("/programs")
def programs():
	return render_template("programs.html", data=programSessions.json())

@app.route("/students")
def students():
	return render_template("students.html", data=studentOf.json())


@app.route("/teachingStaff")
def teachingstaff():
	return render_template("teachingstaff.html", data=teachingStaff.json())

@app.route("/result")
def result():
	return render_template("result.html" , res1 = li[0], res2 = li[1], res3 = li[2], res4 = li[3])

if __name__ == "__main__":
	app.run(debug=True)
