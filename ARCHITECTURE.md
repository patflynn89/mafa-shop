# Mafa-Shop — Architecture Overview

> **For Claude, read this first.** This file exists so any future session can
> get oriented fast without re-deriving repo state from scratch. Update it
> whenever the architecture actually changes — don't let it rot.

## What this project is

A learning project (see `CLAUDE.md`). Mat is learning Django, DRF, Nuxt, and
Vue by building a second-hand e-commerce shop ("Mafa Shop" — clothes, books,
etc.). Learning has priority over shipping speed. **Teach concepts before
writing code**; don't dump finished files.

## Honest state of the repo (as of last check)

This is **scaffolding from a single one-shot session**, not a working app.
Treat almost everything below as "structure exists, behavior mostly doesn't":

- No migrations have been run against a real database.
- No REST API endpoints exist yet (`urls.py` only has `/admin/`).
- No `products`, `cart`, `orders`, `analytics` app code — only empty
  directories with `.gitkeep` placeholders, despite being listed in
  `INSTALLED_APPS`-adjacent docs. Only `accounts` has real code.
- Frontend is a single static "Welcome" page with plain Tailwind gray/white
  styling. **The retro / cyberpunk visual identity described by the user does
  not exist in code yet** — `tailwind.config.js` has no custom theme, no
  neon colors, no retro fonts, no CRT/scanline effects. This is a purely
  functional placeholder.
- There's a naming inconsistency: the repo/project is `mafa-shop`, but
  `frontend/pages/index.vue` and `README.md` still say "**Marfa Shop**" —
  leftover from before the rename (see git commit `b309334`). Worth fixing
  when touching that file.
- `docker-compose.prod.yml`, Nginx config, Prometheus/Grafana config, and
  `.github/workflows/*` are all referenced in the README's aspirational
  structure but don't actually exist yet (just empty dirs / `.gitkeep`).

**Don't assume any feature "must already be there" because the README or
CLAUDE.md describes the target architecture — verify with `Read`/`grep`
before relying on it.**

## Intended visual direction (not yet implemented)

The shop should ultimately look **retro / cyberpunk**: think neon accents,
dark backgrounds, monospace or pixel fonts, maybe CRT scanline/glow effects,
80s-terminal or synthwave aesthetics. This is a design goal for the Nuxt
frontend (Tailwind theme, custom components) — nothing in the current
codebase reflects it. When frontend work starts, this is the first thing
to establish (custom Tailwind theme colors/fonts) before building components.

## Stack

| Layer | Tech | Status |
|---|---|---|
| Backend | Django 5.1 + Django REST Framework | app skeleton only |
| Frontend | Nuxt 3 (Vue 3) + Tailwind CSS | one static page |
| Database | PostgreSQL 16 (Docker) | container defined, not migrated |
| Auth | Custom Django `User` model now; JWT (`djangorestframework-simplejwt`) planned | not implemented |
| Payments | Stripe (planned) | not implemented |
| State mgmt | Pinia (planned) | not installed yet — not in `package.json` |
| Reverse proxy | Nginx (planned, production) | config dir empty |
| Monitoring | Prometheus + Grafana (planned) | config dirs empty |
| CI/CD | GitHub Actions (planned) | workflows dir empty |
| Hosting | Hetzner CX22 (later) | n/a |

## Repository layout

```
mafa-shop/
├── CLAUDE.md                 # teaching rules for this project (READ THIS)
├── ARCHITECTURE.md           # this file
├── README.md                 # tech stack + planned phases
├── docker-compose.yml        # dev environment: db, backend, frontend
├── .env.example               # env var template (copy to .env)
│
├── backend/                  # Django project root
│   ├── manage.py
│   ├── requirements.txt      # django 5.1, DRF 3.15, psycopg2, cors-headers, Pillow
│   ├── Dockerfile
│   ├── config/                # Django project config
│   │   ├── settings.py        # DB, installed apps, CORS, DRF pagination
│   │   ├── urls.py             # only /admin/ registered so far
│   │   └── wsgi.py
│   └── apps/
│       ├── accounts/           # ONLY app with real code
│       │   ├── models.py       # custom User(AbstractUser), unique email
│       │   ├── admin.py        # registers User in Django admin
│       │   ├── apps.py
│       │   └── migrations/0001_initial.py   # exists, NOT applied to a DB
│       ├── products/            # empty — future: Product, Category, ProductImage
│       ├── cart/                # empty — future: Cart, CartItem
│       ├── orders/              # empty — future: Order, OrderItem, payment
│       └── analytics/           # empty — future: custom event tracking
│
├── frontend/                  # Nuxt 3 project root
│   ├── package.json            # nuxt 3.15, vue 3.5, vue-router 4.5, tailwind module
│   ├── nuxt.config.ts          # tailwind module, runtimeConfig.apiBase
│   ├── tailwind.config.js      # DEFAULT config, no custom theme yet
│   ├── app.vue                  # root: just <NuxtPage />
│   ├── pages/index.vue           # static "Welcome to Marfa Shop" page (plain gray Tailwind)
│   ├── components/               # empty
│   ├── composables/              # empty — future: useAuth, useCart
│   ├── stores/                   # empty — future: Pinia auth/cart stores
│   └── layouts/                  # empty
│
├── docker/
│   ├── nginx/         # empty — prod reverse proxy config, not written
│   ├── prometheus/    # empty
│   └── grafana/       # empty
│
├── .github/workflows/  # empty — no CI/CD pipelines defined yet
│
└── .claude/
    ├── CLAUDE.md         # project-level teaching instructions
    ├── agents/researcher.md   # doc-lookup subagent (Django/DRF/Nuxt/Docker/Postgres)
    └── skills/django-teacher/  # interactive Django-learning skill
```

## How the pieces connect (docker-compose.yml)

Three services, dev-only compose file:

- **`db`** — `postgres:16-alpine`, healthcheck via `pg_isready`, persisted volume.
- **`backend`** — builds `./backend`, runs `manage.py runserver 0.0.0.0:8000`,
  bind-mounts source for live reload, waits for `db` to be healthy.
- **`frontend`** — builds `./frontend`, runs `npm run dev` on port 3000,
  bind-mounts source (with `node_modules` excluded from the mount), depends
  on `backend`.

All three read config from a single `.env` file (see `.env.example` for the
required keys: Postgres creds, `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`,
`DJANGO_ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, `API_BASE_URL`).

No `docker-compose.prod.yml` exists yet despite being referenced in README.

## Django settings worth knowing (`backend/config/settings.py`)

- `AUTH_USER_MODEL = "accounts.User"` — custom user model, swapped in before
  any migrations ran (correct order — Django requires this to happen before
  the first `migrate`).
- `CORS_ALLOWED_ORIGINS` defaults to `http://localhost:3000` (the Nuxt dev
  server).
- DRF configured with `PageNumberPagination`, page size 20 — no other DRF
  settings (no auth classes, no permission classes) configured yet.
- Only `apps.accounts` is in `INSTALLED_APPS` — the other four app
  directories are not wired in yet.

## Where to look before making changes

- **Adding a Django app to the project**: it needs an `AppConfig`,
  `__init__.py`, and an entry in `INSTALLED_APPS` — none of `products`,
  `cart`, `orders`, `analytics` have this yet.
- **Adding an API endpoint**: `backend/config/urls.py` currently only has
  `/admin/` — there's no DRF router or `api/` namespace set up yet.
- **Frontend styling**: `tailwind.config.js` is the stock default — the
  retro/cyberpunk theme (colors, fonts, effects) needs to be defined here
  before it can be used in components.
- **Naming**: prefer "Mafa Shop" going forward; "Marfa Shop" in
  `index.vue`/`README.md` is stale.

## Related project files

- `CLAUDE.md` — teaching rules, current learning phase, mat's background.
- `README.md` — full planned tech stack and 9-phase roadmap (aspirational,
  not a status report).
- `.claude/skills/django-teacher/SKILL.md` — interactive Django teaching flow.
- `.claude/agents/researcher.md` — subagent for looking up Django/DRF/Nuxt/
  Docker/PostgreSQL official docs.
