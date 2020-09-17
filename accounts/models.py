from django.db import models


class Player(models.Model):
    # プレイヤーのid(ノードの番号と対応)
    pid = models.AutoField(primary_key=True)
    color = models.CharField(max_length=5, null=True)
    use = models.BooleanField(default=False)
    user_name = models.CharField(max_length=100, null=False)
    user_mail = models.CharField(max_length=100, null=False)

    def __int__(self):
        return self.pid  # , self.color
