from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    class Meta:
        db_table = "employees"
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
