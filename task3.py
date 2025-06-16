from django.db import models

class Vote(models.Model):
    subject = models.CharField(max_length=200)
    positive = models.BooleanField(default=True)

    @classmethod
    def in_favour(cls, subject):
        return cls.objects.create(subject=subject)

    @classmethod
    def against(cls, subject):
        return cls.objects.create(subject=subject, positive=False)

    @classmethod
    def results_for(cls, subject):
        return {
            "in favour": cls.objects.filter(subject=subject, positive=True).count(),
            "against": cls.objects.filter(subject=subject, positive=False).count()
        }
