from flask import Flask, request
import requests, json

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

def post_text_to_slack(user_name, text):
	payload = {"text": "%s said: %s" % (user_name, text)}
	headers = {"content-type": "application/json"}
	r = requests.post(app.config['PING_HOOK'], data=json.dumps(payload), headers=headers)
	return r.status_code

@app.route("/roll", methods=["POST"])
def roll():
	if request.form["token"] == app.config['SLACK_TOKEN'] and request.form["team_id"] == app.config["SLACK_TEAM"]:
				
		# We are going to parse out the text and support one of:
		# d4, d6, d8, d10, d12 and d20
		# Anything else in an error.

		return "Success"
	else
		return 404

@app.route("/ping", methods=["POST"])
def ping():
	
	if request.form["token"] == app.config['SLACK_TOKEN'] and request.form["team_id"] == app.config["SLACK_TEAM"]:
		status = post_text_to_slack(request.form["user_name"], request.form["text"])
		return "Success"
	else:
		# Not part of our group? No soup for you.
		return 404

if __name__ == "__main__":
	app.run(host='0.0.0.0')
