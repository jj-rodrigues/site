from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import SendForm


@app.route('/')
@app.route('/index')
def index():
        return render_template('index.html', titulo='Home')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = SendForm()
    if form.validate_on_submit():
        mensagem = flash('A mensagem foi enviada!')
        return redirect('/index')
    return render_template('contato.html', form=form, titulo='Contato')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Sobre')
