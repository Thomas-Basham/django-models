from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

# I used JB's Tests and changed the names to match the project 
class ThingsTests(TestCase):
    def setUp(self):
        purchaser = get_user_model().objects.create(username="tester",password="tester")
        Snack.objects.create(name="doritos", purchaser=purchaser)

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_list_page_context(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        snacks = response.context['object_list']
        self.assertEqual(len(snacks), 1)
        self.assertEqual(snacks[0].name, "doritos")
        self.assertEqual(snacks[0].description, '')
        self.assertEqual(snacks[0].purchaser.username, "tester")

    def test_detail_page_status_code(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_detail_page_context(self):
        url = reverse('snack_detail', args=(1,))
        response = self.client.get(url)
        thing = response.context['snack']
        self.assertEqual(thing.name, "doritos")
        self.assertEqual(thing.description, '')
        self.assertEqual(thing.purchaser.username, "tester")
