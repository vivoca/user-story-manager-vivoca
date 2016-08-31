from model import *

database.connect()
database.drop_tables([Status, UserStory])
database.create_tables([Status, UserStory])

Status.create(status_name="Planning")
Status.create(status_name="To Do")
Status.create(status_name="In Progress")
Status.create(status_name="Review")
Status.create(status_name="Done")
