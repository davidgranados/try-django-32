from django.test import TestCase
from django.utils import timezone

from .models import Article


class ArticleModelTestCase(TestCase):
    """
    A test case for the Article model.

    This test case includes tests for creating and updating an Article instance.
    """

    def setUp(self):
        """
        Set up the Article instance for testing.

        This method creates an Article instance with test data.
        """
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article.",
            publish=timezone.now().date(),
        )

    def test_article_creation(self):
        """
        Test creating an Article instance.

        This method tests that the Article instance is created correctly and has the expected attributes.
        """
        article = self.article
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(article.__str__(), article.title)
        self.assertIsNotNone(article.slug)
        self.assertEqual(article.get_absolute_url(), f"/articles/{article.slug}/")

    def test_article_update(self):
        """
        Test updating an Article instance.

        This method tests that the Article instance can be updated and has the expected attributes after the update.
        """
        article = self.article
        article.title = "Updated Test Article"
        article.save()
        self.assertEqual(article.__str__(), article.title)
        self.assertIsNotNone(article.slug)
        self.assertEqual(article.get_absolute_url(), f"/articles/{article.slug}/")
