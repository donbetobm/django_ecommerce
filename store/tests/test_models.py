from django.test import TestCase

from store.models import Category, Product, User


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

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        # Django makes reference to the user who created the category by its id, 'created_by_id'
        self.data1 = Product.objects.create(category_id=1, tittle='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
    
    
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')