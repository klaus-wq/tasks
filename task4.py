#1
first_post = Post.objects.filter(creator=User.objects.get(email="bob1@blogs.org")).order_by('created_at').first()

#2
posts = Post.objects.filter(creator=User.objects.get(email="bob1@blogs.org")).order_by('created_at')[:3]

#3
from datetime import datetime

try:
    user = User.objects.get(email="bob1@blogs.org")
except User.DoesNotExist:
    print("Пользователь не найден")
    user = None

if user:
    first_post = Post.objects.filter(creator=user).order_by('created_at').first()
    if first_post:
        today = datetime.now()
        delta = (today - first_post.created_at.replace(tzinfo=None)).days
        print(f"Пользователь ведёт блог уже {delta} дней")
