
echo "Starting dev environment..."
docker compose -f "docker-compose.dev.yaml" down
docker compose -f "docker-compose.dev.yml" up --build
echo "Dev environment started."