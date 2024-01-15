from django.db import models

# Create your models here.
PROFECINCYLEVEL = [
    ('➊',1),
    ('➊ ➋',2),
    ('➊ ➋ ➌',3),
    ('➊ ➋ ➌ ➍',4),
    ('➊ ➋ ➌ ➍ ➎',5),
]
class SkillsModel(models.Model):
    name = models.CharField(max_length=50)
    image_skill = models.ImageField(upload_to='Skills/media/images')
    Prficiency_levels = models.CharField(choices = PROFECINCYLEVEL ,max_length=50)

    def __str__(self) -> str:
        return self.name


class Resume(models.Model):
    resume_pdf = models.FileField(upload_to='Skills/resumes/')

    def __str__(self):
        return f"Resume {self.id}"

    def save(self, *args, **kwargs):
        try:
            old_instance = Resume.objects.get(pk=self.pk)
            if old_instance.resume_pdf:
                old_instance.resume_pdf.delete(save=False)
        except Resume.DoesNotExist:
            pass
        super().save(*args, **kwargs)


