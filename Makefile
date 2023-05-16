
run-dev:
	export ENV=dev && uvicorn main:app --reload

run-prod:
	export ENV=prod && uvicorn main:app --reload
