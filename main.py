from model import *
from flask import *


app = Flask(__name__)


# Adding new story
@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'GET':
        status_list = Status.get_status_list()
        return render_template("form.html", status_list=status_list)
    elif request.method == 'POST':
        columns = ["title", "story", "criteria", "value", "estimation", "status"]
        a = [request.form[element] for element in columns]
        userstory = UserStory(story_title=a[0], user_story=a[1], acceptance_criteria=a[2], business_value=a[3],
                              estimation=a[4], story_status=a[5])
        userstory.save()
        return redirect(url_for('story'))


# Editing an existing story
@app.route('/story/<story_id>')
def story_edit():
    pass


if __name__ == '__main__':
    app.run(debug=True)
