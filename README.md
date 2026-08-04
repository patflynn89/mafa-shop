# Mafa Shop

A second-hand e-commerce marketplace for clothes, books, and more.

## Tech Stack

| Layer | Technology | Status |
|-------|-----------|--------|
| Backend | Python + Django + Django REST Framework | done |
| Frontend | Vue.js 3 + Nuxt 3 | done |
| Styling | Tailwind CSS | done |
| Database | PostgreSQL | done |
| State Management | Pinia | planned |
| Auth | JWT (djangorestframework-simplejwt) | planned |
| Payments | Stripe | planned |
| Containerization | Docker Compose | done |
| Hosting | Hetzner Cloud (CX22) | planned |
| CI/CD | GitHub Actions | planned |
| Reverse Proxy | Nginx | planned |
| Monitoring | Prometheus + Grafana | planned |
| User Analytics | Custom Django tracking | planned |

## Project Structure

```
mafa-shop/
├── backend/                  # Django project
│   ├── config/               # Django settings, urls, wsgi
│   ├── apps/
│   │   ├── accounts/         # User model, auth, profiles
│   │   ├── products/         # Product, Category, ProductImage (empty)
│   │   ├── cart/             # Cart, CartItem (empty)
│   │   ├── orders/           # Order, OrderItem, payment (empty)
│   │   └── analytics/        # Custom event tracking (empty)
│   ├── requirements.txt
│   ├── Dockerfile
│   └── manage.py
├── frontend/                 # Nuxt 3 project
│   ├── pages/                # File-based routing
│   ├── components/           # Reusable Vue components
│   ├── composables/          # Shared logic (useAuth, useCart)
│   ├── stores/               # Pinia stores (auth, cart)
│   ├── layouts/              # Page layouts
│   ├── Dockerfile
│   └── nuxt.config.ts
├── docker/
│   ├── nginx/                # Nginx config for production
│   ├── prometheus/           # Prometheus config
│   └── grafana/              # Grafana dashboards & datasources
├── docker-compose.yml        # Development environment
└── .github/workflows/        # CI/CD pipelines (planned, empty)
```

> **Status:** only `accounts` app has code (custom User model, 1 migration).
> `products`, `cart`, `orders`, `analytics` are empty placeholder dirs.
> `docker-compose.prod.yml` and CI workflows don't exist yet — planned for
> later phases.

## Development Phases

1. **Phase 1** (Weeks 1-2): Docker + Project Setup
2. **Phase 2** (Weeks 3-4): Django Models & REST API
3. **Phase 3** (Weeks 5-6): Vue/Nuxt Frontend Basics
4. **Phase 4** (Weeks 7-8): Frontend-Backend Integration
5. **Phase 5** (Weeks 9-10): Search, Filtering & Polish
6. **Phase 6** (Weeks 11-12): Shopping Cart & Checkout
7. **Phase 7** (Weeks 13-14): Stripe Payment Integration
8. **Phase 8** (Weeks 15-16): Production Deployment
9. **Phase 9** (Weeks 17-19): Monitoring & Analytics (Prometheus + Grafana)

## Getting Started

```bash
cp .env.example .env
docker compose up
```

`docker compose up` fails without `.env` — all three services load env vars
from it (`env_file: .env` in `docker-compose.yml`).

First run needs migrations applied inside the backend container:

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

Admin panel: http://localhost:8000/admin/

## License

MIT
