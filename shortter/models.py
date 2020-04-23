from django.db import models


# Create your models here.
class Links(models.Model):
    lnk_id = models.SmallIntegerField(primary_key=True, db_column='lnk_id')
    lnk_short_name = models.CharField(max_length=16, db_column='lnk_short_name')
    lnk_full_name = models.CharField(max_length=255, db_column='lnk_full_name')

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        sh_link = self.lnk_short_name
        fl_link = self.lnk_full_name[:30]
        return "{sh_link} - [{fl_link}...]".format(sh_link=sh_link, fl_link=fl_link)
