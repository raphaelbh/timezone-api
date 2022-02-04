#!/bin/bash

SCRIPT_PATH=`readlink -f "$0"`
SCRIPT_DIR=`dirname "$SCRIPT_PATH"`
BASE_DIR="$SCRIPT_DIR/.."

# docker image that will be pushed
docker_image="raphaelbh/timezone-api"

# getting last image tag 
last_image_tag=`cat $BASE_DIR/app/version.txt`

# getting new image tag
IFS='.'
read -a last_image_tag_arr <<< "$last_image_tag"
build_version=$(( last_image_tag_arr[2] + 1 ))
tag="${last_image_tag_arr[0]}.${last_image_tag_arr[1]}.$build_version"

# push docker image: new image
docker image build -t "$docker_image:$tag" "$BASE_DIR"
echo "docker image builded: $docker_image:$tag"
docker push "$docker_image:$tag"
echo "docker image pushed: $docker_image:${tag}"

# push docker image: update latest tag
docker image build -t "$docker_image:latest" "$BASE_DIR"
echo "docker image builded: $docker_image:latest"
docker push "$docker_image:latest"
echo "docker image pushed: $docker_image:latest"

# update version file
cat > "$BASE_DIR/app/version.txt" << ENDOFFILE
$tag
ENDOFFILE