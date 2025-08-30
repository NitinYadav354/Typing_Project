from django.db import models

# Create your models here.

class Text(models.Model):
    content = models.TextField()
    category_choices = [
        ("random_words", "Random Words"),
        ("general", "General"),
        ("quotes", "Quotes"),
        ("dialogue", "Dialogue"),
        ("custom", "Custom")

    ]

    Difficulty_choices = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard")
    ]

    Length_choices = [
        ("short", "Short"),
        ("medium", "Medium"),
        ("long", "Long")
    ]

    category = models.CharField(max_length = 20, choices = category_choices)
    difficulty = models.CharField(max_length = 20, choices = Difficulty_choices)
    length = models.CharField(max_length = 20, choices = Length_choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]