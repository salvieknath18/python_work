from django.db import models
from django.contrib.auth.models import User


class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)



class Tag(ObjectTracking):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = []

class QuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="active")

    def all_objects(self):
        return super().get_queryset()

    def inactive(self):
        return self.all_objects().filter(status='inactive')



class Question(ObjectTracking):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    objects = QuestionManager()


    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text