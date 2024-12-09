from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task # importing the model from models.py

#testing the functionality fo task model
class TaskModelTest(TestCase):
    def setUp(self):
        #creating dummy user 
        self.user = User.objects.create_user(username='testuser', password='password123')
        # creating a default task 
        self.task = Task.objects.create(
            title='Test task',
            body='This is a test task.',
            user=self.user,
            status=Task.STATUS_NOT_STARTED
        )

    def test_task_creation(self):
        # testing title 
        self.assertEqual(self.task.title, 'Test task')
        #testing body section
        self.assertEqual(self.task.body, 'This is a test task.')
        # checking status
        self.assertEqual(self.task.status, Task.STATUS_NOT_STARTED)
        self.assertEqual(self.task.user.username, 'testuser')

    def test_task_str_method(self):
        self.assertIn(self.task.body, str(self.task))
