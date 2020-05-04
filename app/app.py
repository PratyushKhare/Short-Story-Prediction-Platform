from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pkk import genre_classifier

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(90000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    action = db.Column(db.Integer, default=0)
    adv = db.Column(db.Integer, default=0)
    comedy = db.Column(db.Integer, default=0)
    crime = db.Column(db.Integer, default=0)
    doc = db.Column(db.Integer, default=0)
    drama = db.Column(db.Integer, default=0)
    fam = db.Column(db.Integer, default=0)
    fantasy = db.Column(db.Integer, default=0)
    history = db.Column(db.Integer, default=0)
    horror = db.Column(db.Integer, default=0)
    mystery = db.Column(db.Integer, default=0)
    romance = db.Column(db.Integer, default=0)
    scifi = db.Column(db.Integer, default=0)
    thriller = db.Column(db.Integer, default=0)
    war = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return '<Task %r>' % self.id



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write', methods=['POST','GET'])
def write():
    if request.method == 'POST':
        story_content = request.form['message']
        story_title = request.form['name']
        genres = genre_classifier(story_content)
        drama1=0
        comedy1=0
        adv1=0
        history1=0
        war1=0
        thriller1=0
        crime1=0
        fantasy1=0
        horror1=0
        fam1=0
        doc1=0
        mystery1=0
        romance1=0
        scifi1=0
        action1=0
        for i in genres:
            if (i=='Drama'):
                drama1=1
            elif (i=='Comedy'):
                comedy1=1
            elif (i=='Adventure'):
                adv1=1
            elif (i=='History'):
                history1=1
            elif (i=='War'):
                war1=1
            elif (i=='Thriller'):
                thriller1=1
            elif (i=='Crime'):
                crime1=1
            elif (i=='Fantasy'):
                fantasy1=1
            elif (i=='Horror'):
                horror1=1
            elif (i=='Family'):
                fam1=1
            elif (i=='Documentary'):
                doc1=1
            elif (i=='Mystery'):
                mystery1=1
            elif (i=='Romance'):
                romance1=1
            elif (i=='ScienceFiction'):
                scifi1=1
            elif (i=='Action'):
                action1=1
        new_story = story(content=story_content, title=story_title, action=action1, adv=adv1, comedy=comedy1, crime=crime1, doc=doc1, drama=drama1, fam=fam1, fantasy=fantasy1, history=history1, horror=horror1, mystery=mystery1, romance=romance1, scifi=scifi1, thriller=thriller1, war=war1)
        #try:
        db.session.add(new_story)
        db.session.commit()
        return render_template('write.html',genres=genres)
        #except:
            #return 'There was an issue adding your story.'
    else:
        
        return render_template('write.html')

@app.route('/read')
def read():
    stories = story.query.order_by(story.date_created).all()
    return render_template('read.html', stories=stories)

@app.route('/delete/<int:id>')
def delete(id):
    story_to_delete = story.query.get_or_404(id)

    try:
        db.session.delete(story_to_delete)
        db.session.commit()
        return redirect('/read')
    except:
        return 'There was a problem deleting that story.'

if __name__ =="__main__":
    app.run(debug=True)

