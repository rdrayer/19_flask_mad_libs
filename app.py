from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
debug = DebugToolbarExtension(app)

@app.route('/')
def home_route():
    '''Madlibs root page that displays example story'''
    ex_story = story.template
    prompts = story.prompts
    return render_template('home.html', ex_story=ex_story, prompts=prompts)

@app.route('/story')
def get_story():
    '''Story page that displays story from form inputs'''
    text = story.generate(request.args)
    return render_template('story.html', text = text)