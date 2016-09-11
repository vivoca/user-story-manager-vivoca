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

    @classmethod
    def get_userstory_list(cls):
        list1, userstory_list = [], []
        r = list(cls.select(cls))
        for element in r:
            list1 = [element.id, element.story_title, element.user_story, element.acceptance_criteria,
                     element.business_value, element.estimation, element.story_status]
            userstory_list.append(list1)
        return userstory_list

    @classmethod
    def get_userstory(cls, story_id):
        list1 = []
        r = cls.select().where(cls.id == story_id)
        for element in r:
            list1 = [element.id, element.story_title, element.user_story, element.acceptance_criteria,
                     element.business_value, element.estimation, element.story_status]
        return list1
