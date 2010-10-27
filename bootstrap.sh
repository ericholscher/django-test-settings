if [ -d "django-test-settings" ]; 
then
    git --git-dir=django-test-settings/.git pull
else
    git clone git://github.com/ericholscher/django-test-settings.git
fi
