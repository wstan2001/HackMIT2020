from app import app, db
from flask import render_template, request, jsonify
from app.models import Polls

@app.route('/')
def poggers():
    database = Polls.query.all()
    data = {poll.name: {'latest': poll.latest, 'timestamp': poll.timestamp} for poll in database}
    return render_template('index.html', data = data)





@app.route('/dbpost', methods=['POST'])
def dbpost():
    if request.method == 'POST':
        data = request.get_json()
        update = Polls.query.filter_by(name=data['location']).first()
        if update is None:
            new = Polls(data['location'], data['waittime'], data['timestamp'])
            db.session.add(new)
            db.session.commit()
        else:
            update.latest = data['waittime']
            update.timestamp = data['timestamp']
            db.session.commit()
    return 'success'
    


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
