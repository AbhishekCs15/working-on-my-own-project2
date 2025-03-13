from flask import Flask, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('register')

@app.route('/', methods=['GET', 'POST'])
def register():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect(url_for('s'))
    return render_template("register.html", form=login_form)

@app.route('/h',methods=['GET','POST'])
def s():
    return render_template('index.html')



@app.route('/hi', methods=['GET', 'POST'])
def match():
    return render_template('index1.html')


if __name__ == "__main__":
    app.run(debug=True)


