from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Project)
def project_created(sender, instance, created, **kwargs):

    if created:
        print("Project Created")