from app import app
from flask import render_template
from app.models import Polls

@app.route('/')
def poggers():
    db = Polls.query.all()
    dict = {poll.name: {'latest': poll.latest, 'timestamp': poll.timestamp} for poll in db}
    print(dict)
    return render_template('index.html', title = 'COVID')

@app.route('/submit')
def donkey():
    return '''
    <html>
    <body>
    <iframe width="1680" height="666" src="https://www.youtube.com/embed/fL-gKdENuMs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <h1 style=font-size:100px;"> DONKEH </h1>
    </body>
    </html>
    
    '''

@app.route('/<word>')
def lol(word):
    return render_template('index.html', title=word.upper())
