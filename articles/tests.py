from django.test import TestCase
from django.utils.text import slugify

from articles.utils import slugify_instance_title

from .models import Article


class ArticleTestCase(TestCase):
    """
    A test case for the Article model.
    """

    def setUp(self):
        """
        Set up the test case by creating 500 articles with the same title and content.
        """
        self.number_of_articles = 500
        for i in range(0, self.number_of_articles):
            Article.objects.create(title="Hello world", content="something else")

    def test_queryset_exists(self):
        """
        Test that the Article queryset exists.
        """
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        """
        Test that the Article queryset count is equal to the number of articles created in the setup.
        """
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

    def test_hello_world_slug(self):
        """
        Test that the slug of the first Article object is equal to the slugified title.
        """
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)

    def test_hello_world_unique_slug(self):
        """
        Test that the slug of each Article object is not equal to the slugified title.
        """
        qs = Article.objects.exclude(slug__iexact="hello-world")
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugified_title = slugify(title)
            self.assertNotEqual(slug, slugified_title)

    def test_slugify_instance_title(self):
        """
        Test that the slug of an Article object is unique when slugify_instance_title is called multiple times.
        """
        obj = Article.objects.all().last()
        new_slugs = []
        for i in range(0, 25):
            instance = slugify_instance_title(obj, save=False)
            new_slugs.append(instance.slug)
        unique_slugs = list(set(new_slugs))
        self.assertEqual(len(new_slugs), len(unique_slugs))

    def test_slugify_instance_title_redux(self):
        """
        Test that the slug of each Article object is unique.
        """
        slug_list = Article.objects.all().values_list("slug", flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))

    def test_article_search_manager(self):
        qs = Article.objects.search(query="hello world")
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query="hello")
        self.assertEqual(qs.count(), self.number_of_articles)
        qs = Article.objects.search(query="something else")
        self.assertEqual(qs.count(), self.number_of_articles)
