from django.db import models
from django.utils import timezone

class Data(models.Model):
    """ 解析データクラス """

    def __init__(self):
        self.author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        self.title = models.CharField(max_length=200)
        self.text = models.TextField()
        self.figures_int = models.IntegerField()
        self.figures_float = models.FloatField()
        self.created_date = models.DateTimeField(default=timezone.now)
        self.published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ データ公開 """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

