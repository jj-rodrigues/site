from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
class SendForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
    submit = SubmitField ('Enviar')
   