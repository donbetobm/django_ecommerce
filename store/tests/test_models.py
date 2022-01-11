from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    # is a good practice using a name that describes what the test is for
    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_entry(self):
        """
        Test category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')