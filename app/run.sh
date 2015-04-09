sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# sudo uwsgi --http-socket :8000 --plugin python --callab app --wsgi-file /home/bear/cs373-idb/app/funruns.py
sudo uwsgi --ini config/config.ini