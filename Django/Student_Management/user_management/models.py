from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    #def_group = Group.objects.get(id=4)
    #DEFAULT_PROFILE = 4
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, null=True, blank=True)
    lastname = models.CharField(max_length=25, null=True, blank=True)
    rollnumber = models.IntegerField(null=True, blank=True)
    profileimage = models.ImageField(upload_to='Profile_images', null=True, blank=True)
    profilerole = models.ForeignKey(Group, on_delete='CASCADE', default=1 )

    class Meta:
        ordering = ('rollnumber',)

    def __str__(self):
        return "{0} {1}".format(self.firstname, self.lastname)


@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()


class Attendance(models.Model):
    completeDateTime = models.DateTimeField()
    studentList = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('completeDateTime',)
