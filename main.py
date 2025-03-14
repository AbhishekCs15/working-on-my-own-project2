from flask import Flask, render_template, redirect,url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer,String,VARCHAR

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_registration.db'


db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email:Mapped[str] = mapped_column(VARCHAR,unique=True)
    password:Mapped[str] = mapped_column(VARCHAR)
    name:Mapped[str] = mapped_column(String)
    phone:Mapped[str] = mapped_column(Integer, unique=True)

with app.app_context():
    db.create_all()


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
        user = User(
            email=login_form.email.data,
            name=login_form.name.data,
            password=login_form.password.data,
            phone=login_form.phone.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=login_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data
        phone = login_form.phone.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if user.password == password and user.phone == phone and user.email == email:
            return redirect(url_for('s'))
    return render_template('login.html', form=login_form)

@app.route('/h',methods=['GET','POST'])
def s():
    return render_template('index.html')



@app.route('/hi', methods=['GET', 'POST'])
def match():
    return render_template('index1.html')


if __name__ == "__main__":
    app.run(debug=True)


