# Symfony Assessment Project

This is a Symfony application for PR review assessment.

## Setup

1. Install dependencies:
```bash
composer install
```

2. Configure your database in `.env`

3. Run migrations:
```bash
php bin/console doctrine:migrations:migrate
```

4. Start the development server:
```bash
symfony server:start
```

## API Endpoints

### Users
- `GET /users` - List all users
- `GET /user/{id}` - Get user by ID
- `POST /user` - Create new user
- `PUT /user/{id}` - Update user
- `DELETE /user/{id}/delete` - Delete user
- `GET /users/search?name={name}` - Search users by name
- `PATCH /user/{id}/activate` - Activate user
- `POST /admin/users/cleanup` - Delete inactive users

### Orders
- `GET /orders` - List all orders
- `POST /order` - Create new order
- `PATCH /order/{id}/status` - Update order status
- `GET /user/{userId}/orders` - Get user orders

## Testing

Run tests with:
```bash
php bin/phpunit
```
