cd mazdoor-sahay

echo "Started servers, hit control+c to quit ..."
(trap 'kill 0' SIGINT; python3 admin-control/main.py & python3 backend/main.py & python3 frontend/main.py)

wait
