from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor Support
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Save method to translate questions into Hindi and Bengali before saving."""
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text

        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        """Fetch the translated question dynamically."""
        return getattr(self, f'question_{lang}', self.question) or self.question

    def __str__(self):
        return self.question
