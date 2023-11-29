build:
	@mkdir -p frontend/public/build/
	@docker-compose -p spam_filtering build
init:
	@docker-compose -p spam_filtering run app ./manage.py migrate
	@docker-compose -p spam_filtering run node npm install
run:
	@docker-compose -p spam_filtering up -d
stop:
	@docker-compose -p spam_filtering down -v
applogs:
	@docker-compose -p spam_filtering logs -f app
nodelogs:
	@docker-compose -p spam_filtering logs -f node
shell:
	@docker-compose -p spam_filtering exec app sh
django-shell:
	@docker-compose -p spam_filtering exec app ./manage.py shell
