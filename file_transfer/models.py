from django.db import models


class File(models.Model):

    name = models.CharField('file name', max_length=40, default="new file")
    transfer_file = models.FileField('file', upload_to="files/")
