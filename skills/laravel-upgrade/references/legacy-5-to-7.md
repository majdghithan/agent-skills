# Legacy: Laravel 5.x / 6 / 7 -> get to 8 first

If you are on 5.x, 6, or 7, do not try to plan a jump straight to a modern version. Get to Laravel 8 through the old hops, then follow the main skill's 8 -> 13 path. This file is a pointer, not a full guide, these versions are years out of security support and the specifics are best read from the official per-version upgrade docs.

## The realistic hops

- **5.x -> 6**: PHP 7.2+. Laravel 6 was the last LTS. Biggest change: string/array helpers (`str_`, `array_`) moved out to the `laravel/helpers` package or the `Str`/`Arr` classes, authorization responses, Carbon 2. Frontend scaffolding split into `laravel/ui`.
- **6 -> 7**: PHP 7.2+. Symfony 5, new `firstOrCreate` behavior, Blade component tags, custom casts, the `laravel/ui` split matured. Date serialization format changed (this one bites APIs).
- **7 -> 8**: PHP 7.3+. Model factories became classes, `app/Models` directory, `php artisan serve` changes, pagination moved to Tailwind by default, `Route::group` namespace behavior changed (the one that breaks controller references, `App\Http\Controllers` prefix is no longer auto-applied).

## Strong recommendation for legacy leaps

An app this far behind, on unsupported versions, with almost certainly a thin test suite, is the textbook case for **Laravel Shift**. Five-plus hops of mechanical renames across abandoned versions is exactly the toil worth paying to skip. Use Shift to chain the hops, review each PR, then rejoin the modern 8 -> 13 path in the main skill for the runtime bites Shift cannot catch.

For each hop, read the official guide for that target version: `laravel.com/docs/{6,7,8}.x/upgrade`.
