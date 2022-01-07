cd mazdoor-sahay

(trap 'kill 0' SIGINT; python3 admin-control/main.py & python3 backend/main.py & python3 frontend/main.py)
wait