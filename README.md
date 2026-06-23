# Marfa Shop

A second-hand e-commerce marketplace for clothes, books, and more.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Django + Django REST Framework |
| Frontend | Vue.js 3 + Nuxt 3 |
| Styling | Tailwind CSS |
| Database | PostgreSQL |
| State Management | Pinia |
| Auth | JWT (djangorestframework-simplejwt) |
| Payments | Stripe |
| Containerization | Docker Compose |
| Hosting | Hetzner Cloud (CX22) |
| CI/CD | GitHub Actions |
| Reverse Proxy | Nginx |
| Monitoring | Prometheus + Grafana |
| User Analytics | Custom Django tracking |

## Project Structure

```
mafa-shop/
├── backend/                  # Django project
│   ├── config/               # Django settings, urls, wsgi
│   ├── apps/
│   │   ├── accounts/         # User model, auth, profiles
│   │   ├── products/         # Product, Category, ProductImage
│   │   ├── cart/             # Cart, CartItem
│   │   ├── orders/           # Order, OrderItem, payment
│   │   └── analytics/        # Custom event tracking
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
├── docker-compose.prod.yml   # Production environment
└── .github/workflows/        # CI/CD pipelines
```

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
docker compose up
```

## License

MIT
