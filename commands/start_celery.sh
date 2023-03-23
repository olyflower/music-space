#!/bin/bash

#celery -A config worker -l ${CELERY_LOG_LEVEL} -c ${CELERY_NUM_WORKERS}
celery -A config worker -l ${CELERY_LOG_LEVEL} -c ${CELERY_NUM_WORKERS} & celery -A config flower --broker=redis://redis
