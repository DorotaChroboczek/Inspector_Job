from django.db.models import *

from accounts.models import Profile


class ActionType(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class ActionStatus(Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class ActionEffect(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


# in next step add field - proposed remuneration & negotiated salary value
# change type, status, effect on_delete=SET_NULL

class Action(Model):
    searcher = ForeignKey(Profile, on_delete=CASCADE)
    company = CharField(max_length=100, null=False, blank=False)
    position = CharField(max_length=150, null=True, blank=True)
    type = ForeignKey(ActionType, on_delete=CASCADE)
    date = DateField()
    response_time = DateField()
    status = ForeignKey(ActionStatus, on_delete=CASCADE)
    effect = ForeignKey(ActionEffect, on_delete=CASCADE)
    comment = CharField(max_length=255, null=True, blank=True)
    conclusions = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company

