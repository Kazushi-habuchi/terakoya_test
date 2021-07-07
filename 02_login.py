from flask import Flask, render_template, request, make_response, redirect
app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'user1' and password == 'pass1':
            response = make_response(redirect('/dashboard'))
            response.set_cookie('login-session-id', 'SrF3hDXZtebMrOEO')
            return response
        return render_template("02_login_form.html")

    else:
        session_id = request.cookies.get('login-session-id')
        if session_id == 'SrF3hDXZtebMrOEO':
            return redirect('/dashboard')
        return render_template("02_login_form.html")


@app.route('/dashboard')
def dashboard():
    session_id = request.cookies.get('login-session-id')
    if session_id == 'SrF3hDXZtebMrOEO':
        response = make_response(render_template("02_dashboard.html"))
        return response
    return redirect('/login')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
