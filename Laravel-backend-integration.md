# Backend Integration Guide

Technical reference for API endpoints and database schema required by the Jamoko Links frontend.

## 1. User Model

Path: `app/Models/User.php`

```php
protected $fillable = [
    'name',
    'business_name',
    'email',
    'phone',
    'password',
    'mpesa_paybill',
    'is_admin',
];

protected $casts = [
    'email_verified_at' => 'datetime',
    'is_admin' => 'boolean',
];
```

## 2. Migration for `is_admin`

```bash
php artisan make:migration add_is_admin_to_users_table --table=users
```

Then update the migration:

```php
public function up()
{
    Schema::table('users', function (Blueprint $table) {
        $table->boolean('is_admin')->default(false)->after('password');
    });
}

public function down()
{
    Schema::table('users', function (Blueprint $table) {
        $table->dropColumn('is_admin');
    });
}
```

## 3. Middleware

Create `EnsureAdmin` middleware:

```php
php artisan make:middleware EnsureAdmin
```

In `app/Http/Middleware/EnsureAdmin.php`:

```php
public function handle($request, Closure $next)
{
    if (! $request->user() || ! $request->user()->is_admin) {
        return response()->json(['message' => 'Unauthorized'], 403);
    }

    return $next($request);
}
```

Register it in `app/Http/Kernel.php`:

```php
protected $routeMiddleware = [
    // ...
    'admin' => \App\Http\Middleware\EnsureAdmin::class,
];
```

## 4. API routes

In `routes/api.php`:

```php
use App\Http\Controllers\AdminController;
use App\Http\Controllers\ClientController;
use App\Http\Controllers\PortalController;
use App\Http\Controllers\PaymentController;

Route::post('/admin/login', [AdminController::class, 'login']);

Route::middleware(['auth:sanctum', 'admin'])->group(function () {
    Route::get('/admin/dashboard', [AdminController::class, 'dashboard']);
    Route::get('/admin/clients', [AdminController::class, 'clients']);
    Route::get('/admin/routers', [AdminController::class, 'routers']);
    Route::get('/admin/transactions', [AdminController::class, 'transactions']);
    Route::get('/admin/commission', [AdminController::class, 'commissionReport']);
    Route::put('/admin/clients/{id}/status', [AdminController::class, 'updateClientStatus']);
    Route::post('/admin/commission/{id}/pay', [AdminController::class, 'payCommission']);
});

Route::post('/client/login', [ClientController::class, 'login']);
Route::post('/client/register', [ClientController::class, 'register']);
Route::middleware('auth:sanctum')->group(function () {
    Route::post('/client/logout', [ClientController::class, 'logout']);
    Route::get('/client/dashboard', [ClientController::class, 'dashboard']);
    Route::get('/client/routers', [ClientController::class, 'getRouters']);
    Route::post('/client/routers', [ClientController::class, 'createRouter']);
    Route::put('/client/routers/{id}', [ClientController::class, 'updateRouter']);
    Route::post('/client/routers/{id}/test', [ClientController::class, 'testRouter']);
    Route::post('/client/routers/{id}/configure', [ClientController::class, 'configureRouter']);
    Route::delete('/client/routers/{id}', [ClientController::class, 'deleteRouter']);
    Route::get('/client/packages', [ClientController::class, 'getPackages']);
    Route::post('/client/packages', [ClientController::class, 'createPackage']);
    Route::put('/client/packages/{id}', [ClientController::class, 'updatePackage']);
    Route::delete('/client/packages/{id}', [ClientController::class, 'deletePackage']);
    Route::get('/client/active-users', [ClientController::class, 'activeUsers']);
    Route::delete('/client/active-users/{id}', [ClientController::class, 'disconnectActiveUser']);
    Route::get('/client/transactions', [ClientController::class, 'transactions']);
    Route::get('/client/earnings', [ClientController::class, 'earnings']);
    Route::put('/client/profile', [ClientController::class, 'updateProfile']);
    Route::put('/client/password', [ClientController::class, 'changePassword']);
});

Route::get('/public/packages/{businessId}', [PortalController::class, 'packages']);
Route::post('/payment/stk-push', [PaymentController::class, 'initiateStkPush']);
Route::get('/payment/status', [PaymentController::class, 'status']);
```

## 5. Controller notes

- Admin login should issue a Sanctum token.
- Client registration should create a user and return an API token.
- `PortalController::packages` should return public package data for the business.
- `PaymentController::initiateStkPush` should start M-Pesa STK Push and return `checkout_request_id`.
- `PaymentController::status` should return `status` and `voucher_code`.

## 6. Example response shape

### Login response

```json
{
  "token": "abc123",
  "user": {
    "id": 1,
    "email": "client@example.com",
    "business_name": "My Hotspot"
  }
}
```

### Package list

```json
[
  { "id": 1, "name": "Hourly", "price": 50, "time_minutes": 60, "is_active": true },
  { "id": 2, "name": "Daily", "price": 200, "time_minutes": 1440, "is_active": true }
]
```

### STK response

```json
{
  "checkout_request_id": "ws_CO_12345"
}
```

### Payment status response

```json
{
  "status": "success",
  "voucher_code": "HOTSPOT-1234"
}
```

---

If you want, I can also generate a complete `routes/api.php` stub plus controller skeleton files in a Laravel project structure when your backend is available in this workspace.