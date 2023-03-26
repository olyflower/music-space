#!/bin/bash

#celery -A config worker -l ${CELERY_LOG_LEVEL} -S django
celery -A config worker -l ${CELERY_LOG_LEVEL} -S django &
celery -A config beat -l ${CELERY_LOG_LEVEL} -S django_celery_beat.schedulers:DatabaseScheduler