from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="program_images/", blank=True, null=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="applications")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program.title}"
