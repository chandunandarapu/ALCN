from django.db import models
class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_url = models.URLField()
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title