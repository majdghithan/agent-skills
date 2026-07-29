# Upgrade: Livewire v1 -> v2

Official guide: [laravel-livewire.com/docs/2.x/upgrading](https://laravel-livewire.com/docs/2.x/upgrading). Steps roughly by impact:

1. **Composer + assets:** bump `livewire/livewire` to `^2.0`, then `php artisan view:clear` and `php artisan livewire:publish --assets`.
2. **Alpine.js:** upgrade to **2.7.0+** if you use Alpine.
3. **Query string property renamed:** `protected $updatesQueryString = ['search'];` -> `protected $queryString = ['search'];`. It now auto-populates from the URL and uses `history.pushState` - remove manual seeding from `mount()`.
4. **Routing changed:** `Route::livewire('/post', 'show-posts');` -> `Route::get('/post', \App\Http\Livewire\ShowPosts::class);` (Laravel 7: remove `->namespace(...)` from `RouteServiceProvider`).
5. **Layout slot:** replace `@yield('content')` with `{{ $slot }}` in the full-page layout.
6. **Layout config moved into `render()`:** `return view('livewire.show-posts')->extends('layouts.base')->section('body');`.
7. **Turbolinks removed** from core (install a separate adapter to keep it).
8. **Testing:** `assertSet()` now asserts the real PHP property; use `assertPayloadSet()` for the JS payload.
9. **Property casters removed:** `protected $casts` is gone - Collections auto-cast; custom logic moves to `hydrateFoo()`/`dehydrateFoo()`.
10. **Pagination views -> Tailwind** by default; `protected $paginationTheme = 'bootstrap';` to restore.
11. **JS hooks renamed:** `componentInitialized` -> `component.initialized`, `beforeElementUpdate` -> `element.updating`, etc.; global is `Livewire.hook(...)`.

## Source
[Official v1 -> v2 upgrade guide](https://laravel-livewire.com/docs/2.x/upgrading)
