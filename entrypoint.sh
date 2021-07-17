echo 'wait for database initilized....'
sleep 10s
for i in `seq 1 25`;do python3.7 /src/migrate.py;done
exec uwsgi --ini wsgi.ini