# Jamoko Links - Smart Hotspot Management

Jamoko Links is a comprehensive solution designed to bridge MikroTik hotspot routers with M-Pesa mobile payments. It allows hotspot business owners to automate their revenue collection, manage user sessions, and monitor business performance through a centralized dashboard.

## Core Features

*   MikroTik Integration: One-click configuration for MikroTik routers.
*   Automated Payments: Full M-Pesa STK Push integration for instant voucher generation.
*   Revenue Share Model: Transparent 2% platform fee on processed transactions.
*   Real-time Analytics: Monitor active users, sales trends, and router health.
*   Flexible Packages: Create custom data and time-limited internet packages.

## Tech Stack

*   Frontend: Tailwind CSS, Vanilla JavaScript
*   Backend: Laravel (PHP)
*   Database: MySQL / PostgreSQL
*   Authentication: Laravel Sanctum
*   API: RESTful architecture

## Getting Started

### Prerequisites

*   Web server (Nginx/Apache)
*   PHP 8.1 or higher
*   Composer
*   MySQL database

### Installation

1. Clone the repository
2. Install PHP dependencies:
   ```bash
   composer install
   ```
3. Configure your environment variables in .env:
   ```bash
   cp .env.example .env
   php artisan key:generate
   ```
4. Run database migrations:
   ```bash
   php artisan migrate
   ```
5. Start the development server:
   ```bash
   php artisan serve
   ```

## License
This project is licensed under the MIT License.
