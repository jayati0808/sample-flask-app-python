import os

from flask import Flask
from flask import render_template, redirect,flash, url_for
from flask import request
from database import db_session, init_db
from models import ActiveData
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy

database_username = 'iatiwari'
database_password = 'iatiwari1'
database_ip       = '127.0.0.1'
database_name     = 'v_sent_poc'

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_entries')
def show_entries():
    activeDatas = ActiveData.query.all()
    return render_template('show_entries.html', activeDatas=activeDatas)


@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/delete/<id>')
def delete_page(id):
    activeData = ActiveData.query.filter(ActiveData.id == id).first()
    db_session.delete(activeData)
    db_session.commit()
    flash('Thanks for registering')
    return redirect(url_for('show_entries'))

@app.route('/edit/<id>',  methods=['GET', 'POST'])
def edit_page(id):
    activeData = ActiveData.query.filter(ActiveData.id == id).first()
    form = UserForm(request.form)
    if request.method == 'POST':
        #activeData = ActiveData(form.username.data, form.sentiment.data)
        activeData.username = form.username.data
        activeData.sentiment = form.sentiment.data
       # activeData.update(dict(name=form.username.data, email=form.sentiment.data))
        db_session.commit()
        flash('Thanks for registering')
        return redirect(url_for('show_entries'))
    form = UserForm(request.form, username=activeData.username, sentiment=activeData.sentiment)
   # activeData = ActiveData(form.username.data=activeData.username, form.sentiment.data=activeData.sentiment)
    return render_template('edit_page.html', form=form, id=activeData.id)

@app.route('/positive/<id>',  methods=['GET', 'POST'])
def positive_page(id):
    db_session.query(ActiveData).filter(ActiveData.id == id).update({ActiveData.sentiment: 'positive'})
    db_session.commit()   
    return redirect(url_for('show_entries'))

@app.route('/negative/<id>',  methods=['GET', 'POST'])
def negative_page(id):
    db_session.query(ActiveData).filter(ActiveData.id == id).update({ActiveData.sentiment: 'negative'})
    db_session.commit()   
    return redirect(url_for('show_entries'))


@app.route('/neutral/<id>',  methods=['GET', 'POST'])
def neutral_page(id):
    db_session.query(ActiveData).filter(ActiveData.id == id).update({ActiveData.sentiment: 'neutral'})
    db_session.commit()   
    return redirect(url_for('show_entries'))

  
if __name__ == "__main__":
    app.run(debug=True)
