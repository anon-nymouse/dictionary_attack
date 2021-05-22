import random
from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usr = form.username.data
        psw = form.password.data
        if form.username.data == 'admin@admin.com' and form.password.data == 'admin':
            return redirect(url_for("success"))
        else:
            return redirect(url_for("login"))
    return render_template('test.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=True)
