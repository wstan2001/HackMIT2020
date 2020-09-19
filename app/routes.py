from app import app
from flask import render_template

@app.route('/')
def poggers():
    return render_template('index.html', title = 'COVID')

@app.route('/about')
def poggers2():
    return render_template('about.html', title = 'COVID')

@app.route('/donkey')
def donkey():
    return '''
    <html>
    <body>
    <iframe width="1680" height="666" src="https://www.youtube.com/embed/fL-gKdENuMs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>
    </html>
    
    '''

@app.route('/<word>')
def lol(word):
    return render_template('index.html', title=word.upper())
