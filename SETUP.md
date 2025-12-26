# Setup Instructions

## Backend Setup (Django REST Framework)

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create sample data (optional but recommended)
```bash
python manage.py create_sample_data
```

This will create:
- 3 sample users (admin, john, jane)
- 3 sample projects
- 8 sample tasks

User credentials:
- admin / admin123 (superuser)
- john / john123
- jane / jane123

### 6. Start the development server
```bash
python manage.py runserver
```

Backend API will be available at: http://localhost:8000

### 7. Access Django Admin (optional)
Visit: http://localhost:8000/admin
Login with admin/admin123

## Frontend Setup (Nuxt 3 + Nuxt UI)

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Start the development server
```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## Testing the Backend API

### List Projects
```bash
curl http://localhost:8000/api/projects/
```

### List Tasks
```bash
curl http://localhost:8000/api/tasks/
```

### List Users
```bash
curl http://localhost:8000/api/users/
```

### Filter Tasks by Project
```bash
curl "http://localhost:8000/api/tasks/?project=1"
```

### Filter Tasks by Status
```bash
curl "http://localhost:8000/api/tasks/?status=in_progress"
```

## Docker Setup (Alternative)

### Build and start all services
```bash
docker-compose up --build
```

### Access services
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Django Admin: http://localhost:8000/admin

### Stop services
```bash
docker-compose down
```

## Troubleshooting

### Backend Issues

**Issue: ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Issue: Database errors**
```bash
# Delete database and recreate
rm db.sqlite3
python manage.py migrate
python manage.py create_sample_data
```

### Frontend Issues

**Issue: Composable not found errors**
```bash
# Clear .nuxt cache and restart
rm -rf .nuxt
npm run dev
```

**Issue: Port already in use**
```bash
# Kill process on port 3000
lsof -ti:3000 | xargs kill -9

# Or specify different port
PORT=3001 npm run dev
```

**Issue: Module not found**
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

## Development Workflow

### 1. Start Backend
```bash
cd backend
source venv/bin/activate
python manage.py runserver
```

### 2. Start Frontend (in another terminal)
```bash
cd frontend
npm run dev
```

### 3. Make Changes
- Backend changes are auto-reloaded
- Frontend changes trigger hot-reload

### 4. Create New Models (Backend)
```bash
# After modifying models.py
python manage.py makemigrations
python manage.py migrate
```

### 5. Add New Pages (Frontend)
- Create files in `app/pages/` directory
- Nuxt will automatically create routes

## API Endpoints Reference

### Projects
- GET /api/projects/ - List all projects
- POST /api/projects/ - Create project
- GET /api/projects/{id}/ - Get project details
- PUT /api/projects/{id}/ - Update project
- DELETE /api/projects/{id}/ - Delete project
- POST /api/projects/{id}/add_member/ - Add member to project
- POST /api/projects/{id}/remove_member/ - Remove member from project

### Tasks
- GET /api/tasks/ - List all tasks
- POST /api/tasks/ - Create task
- GET /api/tasks/{id}/ - Get task details
- PUT /api/tasks/{id}/ - Update task
- DELETE /api/tasks/{id}/ - Delete task

Query parameters for tasks:
- project: Filter by project ID
- status: Filter by status (todo, in_progress, review, done)
- priority: Filter by priority (low, medium, high, urgent)
- assignee: Filter by assignee ID
- search: Search in title and description

### Users
- GET /api/users/ - List all users
- GET /api/users/{id}/ - Get user details

## Next Steps

1. Customize the models to fit your needs
2. Add authentication (JWT recommended)
3. Add more features (comments, attachments, etc.)
4. Deploy to production
5. Add tests

## Production Deployment

### Backend
```bash
# Update settings.py
DEBUG = False
ALLOWED_HOSTS = ['your-domain.com']

# Collect static files
python manage.py collectstatic

# Use gunicorn
gunicorn pms_project.wsgi:application
```

### Frontend
```bash
# Build for production
npm run build

# Preview production build
npm run preview

# Or generate static site
npm run generate
```

## Resources

- Django REST Framework: https://www.django-rest-framework.org/
- Nuxt 3 Documentation: https://nuxt.com/
- Nuxt UI Documentation: https://ui.nuxt.com/
- TailwindCSS: https://tailwindcss.com/
