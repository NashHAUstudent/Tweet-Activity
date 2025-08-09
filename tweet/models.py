from django.db import models
from django.core.exceptions import ValidationError

class Tweet(models.Model):
    """
    This model stores tweet data, including text, an image, and a timestamp.
    """
    # The main text content of the tweet.
    text = models.TextField()

    # The date and time the tweet was created, set automatically.
    created_at = models.DateTimeField(auto_now_add=True)

    # An optional image field. Images will be uploaded to a directory named 'images/'.
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the tweet, which is the text content.
        """
        return self.text

    def clean(self):
        """
        A method to perform model-level validation.
        This checks the tweet for forbidden words before it is saved.
        """
        forbidden_words = ['shit', 'fuck', 'bobo']
        if any(word in self.text.lower() for word in forbidden_words):
            raise ValidationError("This tweet contains a forbidden word.")

    def save(self, *args, **kwargs):
        """
        Overrides the save method to run the clean method before saving.
        """
        self.full_clean()
        super().save(*args, **kwargs)

