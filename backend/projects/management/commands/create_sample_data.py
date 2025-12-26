from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from projects.models import Project
from tasks.models import Task
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Creates sample data for testing'

    def handle(self, *args, **options):
        # Create users
        user1, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@pms.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user1.set_password('admin123')
            user1.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user1.username}'))

        user2, created = User.objects.get_or_create(
            username='john',
            defaults={
                'email': 'john@pms.com',
                'first_name': 'John',
                'last_name': 'Doe',
            }
        )
        if created:
            user2.set_password('john123')
            user2.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user2.username}'))

        user3, created = User.objects.get_or_create(
            username='jane',
            defaults={
                'email': 'jane@pms.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
            }
        )
        if created:
            user3.set_password('jane123')
            user3.save()
            self.stdout.write(self.style.SUCCESS(f'Created user: {user3.username}'))

        # Create projects
        project1, created = Project.objects.get_or_create(
            name='Website Redesign',
            defaults={
                'description': 'Redesign the company website with modern UI/UX',
                'status': 'in_progress',
                'owner': user1,
                'start_date': date.today() - timedelta(days=30),
                'end_date': date.today() + timedelta(days=30),
            }
        )
        if created:
            project1.members.add(user2, user3)
            self.stdout.write(self.style.SUCCESS(f'Created project: {project1.name}'))

        project2, created = Project.objects.get_or_create(
            name='Mobile App Development',
            defaults={
                'description': 'Develop a cross-platform mobile application',
                'status': 'planning',
                'owner': user1,
                'start_date': date.today() + timedelta(days=7),
                'end_date': date.today() + timedelta(days=90),
            }
        )
        if created:
            project2.members.add(user2)
            self.stdout.write(self.style.SUCCESS(f'Created project: {project2.name}'))

        project3, created = Project.objects.get_or_create(
            name='API Integration',
            defaults={
                'description': 'Integrate third-party APIs into the system',
                'status': 'completed',
                'owner': user2,
                'start_date': date.today() - timedelta(days=60),
                'end_date': date.today() - timedelta(days=10),
            }
        )
        if created:
            project3.members.add(user3)
            self.stdout.write(self.style.SUCCESS(f'Created project: {project3.name}'))

        # Create tasks for project1
        tasks_data = [
            {
                'title': 'Create wireframes',
                'description': 'Design wireframes for all main pages',
                'project': project1,
                'assignee': user2,
                'priority': 'high',
                'status': 'done',
                'due_date': date.today() - timedelta(days=5),
            },
            {
                'title': 'Implement homepage',
                'description': 'Develop the new homepage design',
                'project': project1,
                'assignee': user2,
                'priority': 'high',
                'status': 'in_progress',
                'due_date': date.today() + timedelta(days=7),
            },
            {
                'title': 'Setup contact form',
                'description': 'Create and integrate contact form with email',
                'project': project1,
                'assignee': user3,
                'priority': 'medium',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=14),
            },
            {
                'title': 'Test responsive design',
                'description': 'Test website on various devices and browsers',
                'project': project1,
                'assignee': user3,
                'priority': 'high',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=21),
            },
        ]

        for task_data in tasks_data:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                project=task_data['project'],
                defaults=task_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created task: {task.title}'))

        # Create tasks for project2
        tasks_data2 = [
            {
                'title': 'Design app UI',
                'description': 'Create UI mockups for mobile app',
                'project': project2,
                'assignee': user2,
                'priority': 'urgent',
                'status': 'in_progress',
                'due_date': date.today() + timedelta(days=10),
            },
            {
                'title': 'Setup development environment',
                'description': 'Configure React Native development environment',
                'project': project2,
                'assignee': user2,
                'priority': 'high',
                'status': 'todo',
                'due_date': date.today() + timedelta(days=5),
            },
        ]

        for task_data in tasks_data2:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                project=task_data['project'],
                defaults=task_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created task: {task.title}'))

        # Create tasks for project3
        tasks_data3 = [
            {
                'title': 'Payment gateway integration',
                'description': 'Integrate Stripe payment gateway',
                'project': project3,
                'assignee': user3,
                'priority': 'high',
                'status': 'done',
                'due_date': date.today() - timedelta(days=20),
            },
            {
                'title': 'Social media API integration',
                'description': 'Connect to Facebook and Twitter APIs',
                'project': project3,
                'assignee': user3,
                'priority': 'medium',
                'status': 'done',
                'due_date': date.today() - timedelta(days=15),
            },
        ]

        for task_data in tasks_data3:
            task, created = Task.objects.get_or_create(
                title=task_data['title'],
                project=task_data['project'],
                defaults=task_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created task: {task.title}'))

        self.stdout.write(self.style.SUCCESS('\nSample data created successfully!'))
        self.stdout.write(self.style.SUCCESS('\nUsers created:'))
        self.stdout.write(self.style.SUCCESS('  - admin (password: admin123)'))
        self.stdout.write(self.style.SUCCESS('  - john (password: john123)'))
        self.stdout.write(self.style.SUCCESS('  - jane (password: jane123)'))
