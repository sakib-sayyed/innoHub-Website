from django.db import models

class Services(models.Model):
    service_title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.get_padded_id()} - {self.service_title}'
    
    def get_padded_id(self):
        return str(self.id).zfill(2)