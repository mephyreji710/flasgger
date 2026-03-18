python3 -c "
content = '''import os
import sys

path = \"/home/mephyreji/job_portal/jobportal\"
if path not in sys.path:
    sys.path.insert(0, path)

os.environ[\"DJANGO_SETTINGS_MODULE\"] = \"jobportal.settings\"
os.environ[\"SECRET_KEY\"] = \"tb-prod-x9z2!k@m#p$q7&r8*yYvLnW3eFjHsAuI\"
os.environ[\"DEBUG\"] = \"False\"
os.environ[\"ALLOWED_HOSTS\"] = \"mephyreji.pythonanywhere.com\"
os.environ[\"SITE_URL\"] = \"https://mephyreji.pythonanywhere.com\"
os.environ[\"EMAIL_HOST_USER\"] = \"development.skillopt@gmail.com\"
os.environ[\"EMAIL_HOST_PASSWORD\"] = \"skrj mfsj gyun smdp\"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
with open('/var/www/mephyreji_pythonanywhere_com_wsgi.py', 'w') as f:
    f.write(content)
print('Done!')
"
