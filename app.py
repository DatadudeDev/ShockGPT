from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from flask_bcrypt import Bcrypt
import openai
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                    InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                    InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

class RecoveryForm(FlaskForm):
    username = StringField('Username', validators = [InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    submit = SubmitField('Recover Password')


@app.route('/', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('chat'))
    return render_template('login.html', form=form)

@app.route('/chat/', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html')


@app.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@ app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/recovery/', methods=['GET', 'POST'])
def recovery():
    form = RecoveryForm()
    return render_template('recovery.html', form=form)

# Define the route to handle the chat requests
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["userInput"]
    conversation_history = request.json["conversationHistory"]  # Get the conversation history from the request
    response = generate_response(user_input, conversation_history)
    conversation_history.append(user_input)  # Add the user input to the conversation history
    conversation_history.append(response)  # Add the response to the conversation history
    return jsonify({"response": response, "conversationHistory": conversation_history})  # Return the response and updated conversation history


# Set the OpenAI API key
openai.api_key = os.getenv('API-KEY','YOUR-API-KEY-HERE')

# Define the function to generate the OpenAI API response
def generate_response(prompt, conversation_history):
    model_engine = "text-davinci-002"
    prompt_with_history = '\n'.join(conversation_history + [prompt])  # Concatenate conversation history and prompt
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_with_history,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port='5002')
