from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    rating = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    text = models.TextField(max_length=5000)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Question(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.post.text

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class Mark(models.Model):
    is_liked = models.BooleanField(default=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.is_liked

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'
