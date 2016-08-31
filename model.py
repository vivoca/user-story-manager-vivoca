from peewee import *

database = PostgresqlDatabase('vivoca', user='vivoca')


class BaseModel(Model):
    class Meta:
        database = database


class Status(BaseModel):
    status_name = CharField()

    @classmethod
    def get_status_list(cls):
        status_list = []
        r = cls.select(cls)
        for element in r:
            status_list.append(element.status_name)
        return status_list


class UserStory(BaseModel):
    story_title = CharField(null=True)
    user_story = TextField(null=True)
    acceptance_criteria = TextField(null=True)
    business_value = IntegerField()
    estimation = FloatField()
    story_status = CharField()
