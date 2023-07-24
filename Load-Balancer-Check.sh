# Replace 'my-service' with the name of your LoadBalancer service
SERVICE_NAME="flask-app-service"

while true; do
  STATUS=$(kubectl get svc "$SERVICE_NAME" -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
  if [ "$STATUS" ]; then
    echo "LoadBalancer is active. External IP: $STATUS"
    break
  else
    echo "LoadBalancer is still pending..."
    sleep 10
  fi
done
