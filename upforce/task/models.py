from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add other relevant fields



class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
#    other_relavant_details = models.TextField(null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    lid = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    other_relavant_details = models.TextField(null=True)

    def __str__(self):
        return f'{self.user} likes {self.post}'
