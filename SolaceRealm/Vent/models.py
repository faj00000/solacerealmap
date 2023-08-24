from django.db import models

class venttable(models.Model):
    id = models.AutoField(primary_key =True,editable=False)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return str(self.datetime)+"-"+self.title


