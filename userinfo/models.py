from django.db import models
from django.utils import timezone
# Create your models here.
class User_id_table(models.Model):
    
    class Meta:
        db_table = 'User_id_table'
        
    
    title = models.CharField('タイトル',max_length=30)    
    name = models.CharField('名前',max_length=255)
    created_at = models.DateField('入社日',default=timezone.now)
    
    def __str__(self):
        return self.title