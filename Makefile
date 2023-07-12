run-dev:
	export ENV=dev && uvicorn main:app --reload

run-prod:
	export ENV=prod && uvicorn main:app --reload

railway-environment:
	railway environment

railway-run:
	railway run uvicorn main:app --reload

railway-up:
	railway up

update:
	git submodule update --remote
