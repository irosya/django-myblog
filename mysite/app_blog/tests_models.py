from django.test import TestCase
from django.urls import reverse
from .models import Category, Article, ArticleImage
from django.utils import timezone


class CategoryModelTest(TestCase):
    def test_category_model_str_method(self):
        category = Category(category="Test Category")
        self.assertEqual(str(category), "Test Category")


class ArticleModelTest(TestCase):
    def test_article_model_str_method(self):
        article = Article(title="Test Article")
        self.assertEqual(str(article), "Test Article")

    def test_article_model_get_absolute_url(self):
        pub_date = timezone.now()
        article = Article(title="Test Article", slug="test-article", pub_date=pub_date)
        url = article.get_absolute_url()
        expected_url = reverse(
            "news-detail",
            kwargs={"year": pub_date.strftime("%Y"), "month": pub_date.strftime("%m"), "day": pub_date.strftime("%d"), "slug": "test-article"},
        )
        self.assertEqual(url, expected_url)


class ArticleImageModelTest(TestCase):
    def test_article_image_model_str_method(self):
        article = Article(title="Test Article")
        image = ArticleImage(article=article, title="Test Image", image="test.jpg")
        self.assertEqual(str(image), "Test Image")

    def test_article_image_model_filename_property(self):
        article = Article(title="Test Article")
        image = ArticleImage(article=article, title="Test Image", image="photos/test.jpg")
        self.assertEqual(image.filename, "test.jpg")
