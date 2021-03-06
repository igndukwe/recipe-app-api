from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch
from core import models


def sample_user(email='test@gmail.com', password='abcd1234'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful
        """

        email = "anyi1ta1@gmail.com"
        password = "1234abcd"

        # create a user
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        # check username is correct
        self.assertEqual(user.email, email)
        # check password is correct
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized
        """
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(
            email, 'test123'
        )

        # make all emails lowercase
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalied_email(self):
        """Test_creating user with no email raises error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, 'test123'
            )

    def test_create_new_superuser(self):
        """Test creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # Just to test that the Tag model exists
    # and that we can create and modify a Tag model
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            # this creates a user with email and password
            # for Tag with name 'Vegan'
            user=sample_user(),
            name='Vegan'
        )

        # when we convert our tag into a string str(tag)
        # it gives us the name
        self.assertEqual(str(tag), tag.name)

    # Just to test that the Ingredient model exists
    # and that we can create and modify an Ingredient model
    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    # This would test that we can create new recipie objects
    # and that we can successfully retrieve them as a string
    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid

        # myimage.jpg, the myimage part will be replaced
        # with the generated uuid
        # both the file path will be retained
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        # f'' means you can insert varibles in strings by using {}
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
