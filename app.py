from flask import Flask, render_template, request
import re

app = Flask(__name__)

###############
@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/match", methods = ['POST'])
def test():
    regex_pattern = request.form.get("regex_pattern")
    test_string = request.form.get("test_string")
    matches = re.findall(regex_pattern, test_string)
    print(matches)
    if matches:
        return render_template("results.html", regex_pattern = regex_pattern, test_string=test_string, matches=matches)
    else:
        return render_template("result2.html", regex_pattern = regex_pattern, test_string=test_string)

@app.route("/email", methods = ['GET','POST'])
def email_valid():
    import re
    pattern = r"^[a-z 0-9]+[\._]?[a-z 0-9+[@]\w+[.]\w{2,4}$"
    email=request.form.get("email")
    if re.search(pattern, email):
        return render_template("valid_email.html", email=email)
    else:
        return render_template("invalid_email.html", email=email)



###################


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")