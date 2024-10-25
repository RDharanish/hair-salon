from django.db import models

# Define available categories for the 'category' field
CATEGORY_CHOICES = [
    ('Beauty & spa', 'Beauty & spa'),
    ('Body massage', 'Body massage'),
    ('Shaving & Facial', 'Shaving & Facial'),
    ('Hair Color', 'Hair Color'),
]
USERNAME_FIELD = 'email'

class Appointment(models.Model):
    # Model fields corresponding to form fields
    name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Beauty & spa')
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category} on {self.date}"
