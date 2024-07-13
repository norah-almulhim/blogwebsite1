from django.core.management.base import BaseCommand
from blog.models import User, Post, Comment, Category
from django.utils import timezone


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **kwargs):
        # Create users
        users_data = [
            {"username": "johnsmith", "email": "johnsmith@example.com",
                "password": "password123"},
            {"username": "emilyjones", "email": "emilyjones@example.com",
                "password": "password123"},
            {"username": "davidwilson", "email": "davidwilson@example.com",
                "password": "password123"},
            {"username": "sarahbrown", "email": "sarahbrown@example.com",
                "password": "password123"},
            {"username": "michaelscott", "email": "michaelscott@example.com",
                "password": "password123"},
            {"username": "lisajohnson", "email": "lisajohnson@example.com",
                "password": "password123"},
            {"username": "alexturner", "email": "alexturner@example.com",
                "password": "password123"},
            {"username": "jessicabaker", "email": "jessicabaker@example.com",
                "password": "password123"},
            {"username": "matthewwright",
                "email": "matthewwright@example.com", "password": "password123"},
            {"username": "oliviawalker", "email": "oliviawalker@example.com",
                "password": "password123"},
        ]

        users = {}
        for user_data in users_data:
            user, created = User.objects.get_or_create(username=user_data['username'], defaults={
                "email": user_data['email'],
                "password": user_data['password']
            })
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'User "{user.username}" created'))
            users[user.username] = user

        # Create categories
        categories_data = [
            "Programming", "Productivity", "Travel", "Art", "Technology",
            "Health", "Books", "Design", "Wellness", "Self-Improvement"
        ]

        categories = {}
        for category_name in categories_data:
            category, created = Category.objects.get_or_create(
                name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Category "{category.name}" created'))
            categories[category_name] = category

        # Create posts
        posts_data = [
            {"title": "Introduction to Django", "content": "Lorem ipsum dolor sit amet",
                "category": "Programming", "date_published": timezone.now()},
            {"title": "Tips for Effective Time Management", "content": "Lorem ipsum dolor sit amet",
                "category": "Productivity", "date_published": timezone.now()},
            {"title": "Exploring the Wonders of Nature", "content": "Lorem ipsum dolor sit amet",
                "category": "Travel", "date_published": timezone.now()},
            {"title": "The Art of Photography", "content": "Lorem ipsum dolor sit amet",
                "category": "Art", "date_published": timezone.now()},
            {"title": "Understanding Machine Learning Algorithms", "content": "Lorem ipsum dolor sit amet",
                "category": "Technology", "date_published": timezone.now()},
            {"title": "Healthy Eating Habits for a Balanced Lifestyle",
                "content": "Lorem ipsum dolor sit amet", "category": "Health", "date_published": timezone.now()},
            {"title": "Exploring the World of Literature", "content": "Lorem ipsum dolor sit amet",
                "category": "Books", "date_published": timezone.now()},
            {"title": "Mastering the Basics of Graphic Design", "content": "Lorem ipsum dolor sit amet",
                "category": "Design", "date_published": timezone.now()},
            {"title": "The Benefits of Yoga and Meditation", "content": "Lorem ipsum dolor sit amet",
                "category": "Wellness", "date_published": timezone.now()},
            {"title": "The Power of Positive Thinking", "content": "Lorem ipsum dolor sit amet",
                "category": "Self-Improvement", "date_published": timezone.now()}
        ]

        posts = []
        for post_data in posts_data:
            category = categories[post_data['category']]
            post, created = Post.objects.get_or_create(title=post_data['title'], defaults={
                "content": post_data['content'],
                "category": category,
                "date_published": post_data['date_published']
            })
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Post "{post.title}" created'))
            posts.append(post)

        # Create comments
        comments_data = [
            {"post": posts[0], "user": users["emilyjones"],
                "content": "Great introduction to Django!"},
            {"post": posts[0], "user": users["michaelscott"],
                "content": "Very informative article."},
            {"post": posts[1], "user": users["davidwilson"],
                "content": "These tips are really helpful."},
            {"post": posts[2], "user": users["alexturner"],
                "content": "I love traveling and exploring nature!"},
            {"post": posts[3], "user": users["sarahbrown"],
                "content": "Beautifully written article about photography."},
            {"post": posts[5], "user": users["jessicabaker"],
                "content": "Healthy eating is so important for overall well-being."},
            {"post": posts[6], "user": users["matthewwright"],
                "content": "I enjoy reading different genres of books."},
            {"post": posts[7], "user": users["oliviawalker"],
                "content": "Graphic design is such a creative field."},
            {"post": posts[8], "user": users["lisajohnson"],
                "content": "Yoga and meditation have changed my life."},
            {"post": posts[9], "user": users["johnsmith"],
                "content": "Positive thinking can make a huge difference in one's life."}
        ]

        for comment_data in comments_data:
            comment, created = Comment.objects.get_or_create(post=comment_data['post'], user=comment_data['user'], defaults={
                "content": comment_data['content'],
                "date_posted": timezone.now()
            })
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Comment on "{comment.post.title}" by "{comment.user.username}" created'))
