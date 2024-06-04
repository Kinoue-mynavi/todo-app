# Server
run-s:
	cd server && python server.py

db-migrate:
	cd server && python manage.py init_db

# Client
run-c:
	cd client && npm run dev