from app import app, db
from flask import render_template, request, jsonify
from app.models import Polls

@app.route('/')
def poggers():
    database = Polls.query.all()
    dict = {poll.name: {'latest': poll.latest, 'timestamp': poll.timestamp} for poll in database}
    return render_template('index.html', title = 'COVID')

@app.route('/about')
def poggers2():
    return render_template('about.html')

@app.route('/contact')
def poggers3():
    return render_template('contact.html')


@app.route("/<any(plain, jquery, fetch):js>")
def index(js):
    return render_template("{0}.html".format(js), js=js)



@app.route('/dbpost', methods=['POST'])
def dbpost():
    if request.method == 'POST':
        data = request.get_json()
        update = Polls.query.filter_by(name=data['location']).first()
        if update is None:
            new = Polls(data['location'], data['waittime'], data['timestamp'])
            print(new)
            db.session.add(new)
            db.session.commit()
    return data
    


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
