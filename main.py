# Imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

# Create Form fields
class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='log in')


comp_email = 'admin@email.com'
comp_password = '12345678'

# Create app
app = Flask(__name__)
Bootstrap(app)

# Validation
app.config['SECRET_KEY'] = 'Litle_kami75'

# Routes
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    form = MyForm()
    emailu = form.email.data
    passwordu = form.password.data
    if form.validate_on_submit():
        print(f'{emailu}\n{passwordu}')
        if comp_email == emailu and comp_password == passwordu:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


@app.route('/cafes', methods=['POST', 'GET'])
def cafes():
    form = MyForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
