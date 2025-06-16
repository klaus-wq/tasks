from django.db import models

class Clip(models.Model):
    title = models.CharField(max_length=200)

    def like(self):
        ClipLike.objects.create(clip=self)

    def dislike(self):
        ClipDislike.objects.create(clip=self)


    @classmethod
    def rates_for(cls, *args):
        annotate = cls.objects.filter(
            title__in=args,
        ).annotate(
            likes=models.Count('cliplike', distinct=True),
            dislikes=models.Count('clipdislike', distinct=True),
        ).order_by('title')
        return list(annotate.values_list('likes', 'dislikes'))

class ClipLike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
  

class ClipDislike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
