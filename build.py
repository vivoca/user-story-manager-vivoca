from model import *

database.connect()
database.drop_tables([Status, UserStory])
database.create_tables([Status, UserStory])

Status.create(status_name="Planning")
Status.create(status_name="ToDo")
Status.create(status_name="InProgress")
Status.create(status_name="Review")
Status.create(status_name="Done")
