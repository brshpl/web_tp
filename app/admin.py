from django.contrib import admin
from app.models import Post, Question, Tag, Answer, Profile, Mark

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Post)
admin.site.register(Mark)
