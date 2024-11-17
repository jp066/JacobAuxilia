from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    attachment = models.FileField(upload_to='feedback_attachments/', blank=True, null=True)  # Campo de anexo

    def __str__(self):
        return f"{self.subject} - {self.name}"


class Video(models.Model):
    url = models.URLField()
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
