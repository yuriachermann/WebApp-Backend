from django.db import models


class Tool(models.Model):
    title = models.CharField(max_length=200)
    tool_num = models.CharField(max_length=200)
    raw_image = models.CharField(max_length=200)  # raw image type to store in database
    processed_image = models.CharField(max_length=200, default='')  # raw image type to store in database
    wear_area = models.FloatField(default=0.0)
    wear_length = models.FloatField(default=0.0)
    vb_max = models.FloatField(default=0.0)
    vb_mean = models.FloatField(default=0.0)


class ToolWear(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    wear_area = models.FloatField(default=0.0)
    wear_length = models.FloatField(default=0.0)
    vb_max = models.FloatField(default=0.0)
    vb_mean = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tool.title + " " + str(self.date)


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + str(self.date)
