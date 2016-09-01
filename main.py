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


@app.route('/list')
def story_list():
    adding_table_to_html()
    return render_template("list.html")


def print_table():
    l = UserStory.get_userstory_list()
    html = """
    <!doctype html>

    <html>

    <head>
    <title>User Story Manager</title>
    </head>

    <body>
        <h1>User Story Manager</h1>
    <table border='1'>
        <thead>
        <tr><th colspan="7">User Story Manager</th></tr>
        <tr><th>Story ID</th><th>Story Title</th>
            <th>User Story</th><th>Acceptance Criteria</th>
            <th>Business Value</th><th>Estimation</th>
            <th>Status</th>
        </tr>
        </thead>

        <tbody>
    """
    for i in l:
        html += ('<tr>\n')
        for j in range(7):
            html += (('<td>') + str(i[j]) + ('</td>'))
        html += ('</tr>\n')
    html += """</tbody>

    </table>
    </body>
    </html>
    """
    return html


def adding_table_to_html():
    html = print_table()
    html_file = open("templates/list.html", "w")
    html_file.write(html)
    html_file.close


if __name__ == '__main__':
    app.run(debug=True)
