from django.test import TestCase
from django.urls import reverse
from .models import Todolist
from .forms import Todolisform
from .views import addTodoitem, completedTodo, deletecompleted, deleteAll

class TodoviewsTestCase(TestCase):
    def setUp(self):
        # Create initial data for testing
        self.task1 = Todolist.objects.create(text = "Task 1", completed = False)
        self.task2 = Todolist.objects.create(text = "Task 2", completed = False)
        self.task3 = Todolist.objects.create(text = "Task 3", completed = True)

    def test_index_view(self):
        # Test the index view render the correct context and template
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)