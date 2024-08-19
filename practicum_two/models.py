from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    files = models.ManyToManyField('ProjectFile', related_name='projects', null=True, blank=True)

    class Meta:
        ordering = ['-title']
        verbose_name = "Project"
        verbose_name_plural = 'Projects'
        unique_together = (('title', 'created_at'),)

    def __str__(self):
        return f"Project: {self.title}"


class Task(models.Model):
    STATUSES_CHOICES = [
        ('New', 'New'),
        ('In_progress', 'In_progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Very High', 'Very High'),
    ]
    title = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(10)])
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=STATUSES_CHOICES, default='New', max_length=15)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=15)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', null=True, blank=True, related_name='tasks')
    due_date = models.DateTimeField()
    assignee = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks')

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-due_date', 'assignee']
        unique_together = (('title', 'project'),)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to='project_files/',)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


back_tag = Tag.objects.get(title='Backend')
devops_tag = Tag.objects.get(title='DevOPS')
designer_tag = Tag.objects.get(title='Design')
front_tag = Tag.objects.get(title='Frontend')
qa_tag = Tag.objects.get(title='Q&A')
