"""
Celery application configuration for Alachua Civic Intelligence System.

Usage:
    # Start worker
    celery -A src.tasks.celery_app worker --loglevel=info
    
    # Start beat scheduler
    celery -A src.tasks.celery_app beat --loglevel=info
"""

import os
from celery import Celery
from celery.schedules import crontab

# Load broker URL from environment
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# Create Celery app
celery_app = Celery(
    "alachua_civic",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=[
        "src.tasks.scout_tasks",
    ]
)

# Celery configuration
celery_app.conf.update(
    # Task settings
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="America/New_York",
    enable_utc=True,
    
    # Task execution settings
    task_acks_late=True,
    task_reject_on_worker_lost=True,
    
    # Result settings
    result_expires=86400,  # 24 hours
    
    # Worker settings
    worker_prefetch_multiplier=1,
    worker_concurrency=4,
)

# Beat schedule (periodic tasks)
celery_app.conf.beat_schedule = {
    # Daily scout runs at 6 AM Eastern
    "daily-scout-run": {
        "task": "src.tasks.scout_tasks.run_all_critical_scouts",
        "schedule": crontab(hour=6, minute=0),
        "options": {"queue": "scouts"}
    },
    
    # Weekly analyst run on Monday at 9 AM Eastern
    "weekly-analyst-run": {
        "task": "src.tasks.analyst_tasks.run_weekly_analysis",
        "schedule": crontab(hour=9, minute=0, day_of_week=1),
        "options": {"queue": "analysts"}
    },
    
    # Monthly synthesizer run on 1st of month at 10 AM Eastern
    "monthly-newsletter": {
        "task": "src.tasks.synthesizer_tasks.generate_monthly_newsletter",
        "schedule": crontab(hour=10, minute=0, day_of_month=1),
        "options": {"queue": "synthesizers"}
    },
}

# Task routing
celery_app.conf.task_routes = {
    "src.tasks.scout_tasks.*": {"queue": "scouts"},
    "src.tasks.analyst_tasks.*": {"queue": "analysts"},
    "src.tasks.synthesizer_tasks.*": {"queue": "synthesizers"},
}


if __name__ == "__main__":
    celery_app.start()
