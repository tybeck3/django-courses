from django.db import models

class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 3:
            errors['title'] = "Name must be at least 3 characters"
        if len(postData["description"]) == 0:
            errors['description'] = "Please enter a description"
        return(errors)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager

    def __repr__(self):
        return f"{self.id} {self.title} {self.description} {self.created_at}"