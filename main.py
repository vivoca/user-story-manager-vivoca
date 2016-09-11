from model import *
from flask import *


app = Flask(__name__)


@app.route('/home')
def home():
    return render_template("home.html")


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
@app.route('/story/<story_id>', methods=['GET', 'POST'])
def story_edit(story_id):
    if request.method == 'GET':
        status_list = Status.get_status_list()
        data_list = UserStory.get_userstory(story_id)
        return render_template("edit.html", data_list=data_list, status_list=status_list)
    elif request.method == 'POST':
        columns = ["title", "story", "criteria", "value", "estimation", "status"]
        a = [request.form[element] for element in columns]
        q = UserStory.update(story_title=a[0], user_story=a[1], acceptance_criteria=a[2], business_value=a[3],
                             estimation=a[4], story_status=a[5]).where(UserStory.id == story_id)
        q.execute()
        return redirect(url_for('story_list'))


# Listing the already added data
@app.route('/list')
@app.route('/')
def story_list():
    userstory_list = UserStory.select()
    return render_template("list.html", userstory_list=userstory_list)


@app.route('/story/delete/<story_id>')
def delete_story(story_id):
    q = UserStory.delete().where(UserStory.id == story_id)
    q.execute()
    return redirect(url_for('story_list'))


if __name__ == '__main__':
    app.run(debug=True)
