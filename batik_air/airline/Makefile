TAG = latest

build-image:
	docker build -t nameko/nameko-example-airline:$(TAG) ./airline

docker-tag:
	docker tag nameko/nameko-example-airline:$(TAG) \
	nameko/nameko-example-airline:$(TAG)

push-image:
	docker push nameko/nameko-example-airline:$(TAG)
