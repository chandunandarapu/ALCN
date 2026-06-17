# Phase 2 - Quick Setup Guide

## ✅ Pre-requisites
- Phase 1 backend fully operational ✓
- Python 3.14+ with Django 6.0.5 ✓
- PostgreSQL or SQLite configured ✓
- Redis running ✓

---

## 📦 Installation Steps

### Step 1: Install Phase 2 Dependencies
```bash
cd backend
pip install -r requirements-phase2.txt
```

### Step 2: Register New Apps in settings.py
Add these to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ... existing apps ...
    'apps.communications',
    'apps.documents',
    'apps.payments',
    'apps.notifications',
    'apps.audit',
    'apps.integrations',
    
    # New packages
    'channels',
    'drf_spectacular',
]
```

### Step 3: Update URL Configuration
Add to `backend/config/urls.py`:
```python
urlpatterns = [
    # ... existing paths ...
    path('api/', include('apps.communications.urls')),
    path('api/', include('apps.documents.urls')),
    path('api/', include('apps.payments.urls')),
    path('api/', include('apps.notifications.urls')),
    path('api/', include('apps.audit.urls')),
]
```

### Step 4: Update ASGI for WebSockets (Optional - needed for real-time chat)
```bash
# Will need to update config/asgi.py with:
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
```

### Step 5: Create Migrations
```bash
python manage.py makemigrations communications
python manage.py makemigrations documents
python manage.py makemigrations payments
python manage.py makemigrations notifications
python manage.py makemigrations audit
python manage.py migrate
```

### Step 6: Update Environment Variables
Add to `.env`:
```env
# Email Configuration
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Stripe Configuration (optional)
STRIPE_PUBLIC_KEY=pk_test_YOUR_KEY
STRIPE_SECRET_KEY=sk_test_YOUR_KEY
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

---

## 🧪 Testing Phase 2 Setup

### Test Communications
```bash
curl -X POST http://127.0.0.1:8000/api/communications/messages/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"receiver": 1, "subject": "Test", "content": "Hello"}'
```

### Test Documents
```bash
curl -X POST http://127.0.0.1:8000/api/documents/ \
  -H "Authorization: Bearer <token>" \
  -F "file=@document.pdf" \
  -F "project=1"
```

### Test Payments
```bash
curl -X POST http://127.0.0.1:8000/api/payments/invoices/ \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"project": 1, "amount": 5000, "due_date": "2026-07-17"}'
```

### Test Notifications
```bash
curl http://127.0.0.1:8000/api/notifications/ \
  -H "Authorization: Bearer <token>"
```

---

## 📊 New Apps Overview

| App | Purpose | Key Models |
|-----|---------|-----------|
| **communications** | Messaging & proposals | Message, Proposal, Feedback |
| **documents** | File management | Document, DocumentVersion |
| **payments** | Invoicing & transactions | Invoice, Transaction |
| **notifications** | User alerts | Notification, EmailLog |
| **audit** | Compliance & logging | ActivityLog |
| **integrations** | Third-party APIs | (No models - utility module) |

---

## 🔧 Development Workflow

### For Developers
1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make changes to models/views
3. Create migrations: `python manage.py makemigrations`
4. Write tests: Add tests to `tests.py` in each app
5. Run tests: `pytest`
6. Push and create Pull Request

### For Code Quality
```bash
# Format code
black apps/

# Check linting
flake8 apps/

# Sort imports
isort apps/

# Run tests with coverage
pytest --cov=apps
```

---

## 🚀 Next Steps

1. **Frontend Setup** - Create React/Vue.js SPA
2. **WebSocket Integration** - Implement real-time chat
3. **Payment Integration** - Connect Stripe webhook
4. **Email Service** - Set up Celery email tasks
5. **Testing** - Write comprehensive test suites
6. **Deployment** - Docker, AWS/GCP setup

---

## 📝 Important Notes

- ✅ All new apps follow Phase 1 patterns
- ✅ JWT authentication required for all endpoints
- ✅ Database migrations are reversible
- ✅ Backward compatible with Phase 1 API
- ✅ Ready for horizontal scaling with Redis

---

## 🆘 Troubleshooting

### Issue: Import errors for new apps
**Solution**: Make sure apps are registered in `INSTALLED_APPS`

### Issue: Migration conflicts
**Solution**: Delete `db.sqlite3` and run fresh migrations

### Issue: WebSocket not working
**Solution**: Install `channels-redis` and update `ASGI_APPLICATION`

---

**Last Updated**: 2026-06-17  
**Status**: ✅ READY FOR IMPLEMENTATION
