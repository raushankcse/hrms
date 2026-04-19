## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd hrms
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Setup environment variables

Create a `.env` file using `.env.example`:

```bash
cp .env.example .env
```

Update values inside `.env`:

```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start server

```bash
python manage.py runserver
```
