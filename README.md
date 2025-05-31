# notification_manager

`notification_manager` is a microservice in the **BarberShop API** platform responsible for sending email notifications to customers. It listens asynchronously for booking events published by other services (specifically `customers_manager`) via RabbitMQ and sends confirmation emails through the Mailgun API.

Unlike other services, it does not expose any HTTP API and operates as a background worker.

## Features

- Asynchronous event consumption from RabbitMQ  
- Email notification sending using Mailgun  
- Stateless microservice with no external database  
- Runs as a long-lived background process  
- Triggered by appointment booking events from `customers_manager`

## Technologies

- Python 3.11  
- Pika (RabbitMQ client)  
- Mailgun API  
- Docker  
- Pytest

## Environment Variables / Secrets

The following secrets are required (via GitHub Secrets or a local `.env` file):


- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_ACCOUNT_ID`
- `MAIL_GUN_API_KEY`, `MAIL_GUN_DOMAIN`, `MAIL_GUN_SENDER_EMAIL`,
- `RABBITMQ_HOST`, `RABBITMQ_PORT`, `RABBITMQ_QUEUE`,

  ## ⚙️ Local Development
1. **Clone the repository**
   ```
   git clone https://github.com/Kar977/notification_manager.git
   cd notification_manager
   ```
2. **Build and run using Docker**
   ```
   docker compose build -t notification_manager .
   docker compose up

   ```
   The service will be available at:
   `http://localhost:8004`

>In production, the service is accessible only through the API Gateway.
### Running Tests
Run all tests using
```
python -m pytest
```

### Deployment
This microservice is containerized and deployed via AWS ECR and Portainer on EC2.<br></br>
Final deployment on EC2 is handled manually through Portainer.
