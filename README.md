# PMS - Project Management System

A full-stack Project Management System built with Django REST Framework (backend) and Nuxt 3 with Nuxt-UI (frontend).

## Features

- 📊 **Dashboard** - Overview of projects and tasks with statistics
- 📁 **Project Management** - Create, view, and manage projects
- ✅ **Task Management** - Create, assign, and track tasks
- 🎨 **Modern UI** - Beautiful interface built with Nuxt-UI and TailwindCSS
- 🔄 **Real-time Updates** - Seamless integration between frontend and backend
- 🐳 **Docker Support** - Easy deployment with Docker Compose

## Tech Stack

### Backend
- **Django 4.2** - Python web framework
- **Django REST Framework** - RESTful API toolkit
- **PostgreSQL** - Database (SQLite for development)
- **CORS Headers** - Cross-origin resource sharing

### Frontend
- **Nuxt 3** - Vue.js framework
- **Nuxt-UI** - Beautiful UI component library
- **TailwindCSS** - Utility-first CSS framework
- **$fetch** - Nuxt's native HTTP client for API calls

## Project Structure

```
PMS/
├── backend/                 # Django backend
│   ├── pms_project/        # Django project settings
│   ├── projects/           # Projects app
│   ├── tasks/              # Tasks app
│   ├── users/              # Users app
│   ├── manage.py
│   └── requirements.txt
├── frontend/               # Nuxt frontend
│   ├── app/
│   │   ├── pages/         # Application pages
│   │   ├── layouts/       # Layout components
│   │   └── components/    # Vue components
│   ├── composables/       # Composables (useApi)
│   ├── nuxt.config.ts
│   └── package.json
└── docker-compose.yml     # Docker configuration
```

## Getting Started

### Prerequisites
- Python 3.12+
- Node.js 20+
- npm or yarn
- Docker (optional)

### Installation

#### Option 1: Local Development

**Backend Setup:**

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

The backend API will be available at `http://localhost:8000`

**Frontend Setup:**

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

#### Option 2: Docker

```bash
# Build and start all services
docker-compose up --build

# Run in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Access the application:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Django Admin: `http://localhost:8000/admin`

## API Endpoints

### Projects
- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create a new project
- `GET /api/projects/{id}/` - Get project details
- `PUT /api/projects/{id}/` - Update a project
- `DELETE /api/projects/{id}/` - Delete a project

### Tasks
- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Get task details
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task

Query parameters:
- `project` - Filter by project ID
- `status` - Filter by status (todo, in_progress, review, done)
- `priority` - Filter by priority (low, medium, high, urgent)
- `assignee` - Filter by assignee ID

### Users
- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Get user details

## Development

### Backend

**Run tests:**
```bash
python manage.py test
```

**Create migrations:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Access Django admin:**
- Create a superuser: `python manage.py createsuperuser`
- Visit: `http://localhost:8000/admin`

### Frontend

**Build for production:**
```bash
npm run build
```

**Preview production build:**
```bash
npm run preview
```

**Generate static site:**
```bash
npm run generate
```

## Data Models

### Project
- `name` - Project name
- `description` - Project description
- `status` - planning, in_progress, completed, on_hold
- `owner` - Project owner (User)
- `members` - Project members (Many-to-Many with User)
- `start_date` - Project start date
- `end_date` - Project end date
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

### Task
- `title` - Task title
- `description` - Task description
- `project` - Associated project
- `assignee` - Assigned user
- `priority` - low, medium, high, urgent
- `status` - todo, in_progress, review, done
- `due_date` - Task due date
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

## Environment Variables

### Backend
- `DEBUG` - Debug mode (default: True)
- `SECRET_KEY` - Django secret key
- `DATABASE_URL` - Database connection string
- `ALLOWED_HOSTS` - Allowed hosts

### Frontend
- `NUXT_PUBLIC_API_BASE` - Backend API base URL (default: http://localhost:8000/api)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For support, please open an issue in the GitHub repository.
