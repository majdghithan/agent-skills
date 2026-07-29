# Upgrade: Filament v2 -> v3

Official guide: [filamentphp.com/docs/3.x/forms/upgrade-guide](https://filamentphp.com/docs/3.x/forms/upgrade-guide). New minimums: **Laravel 10+, Livewire 3+**.

## Automated script (handles most of it)
```bash
composer require filament/upgrade:"^3.2" -W --dev
vendor/bin/filament-v3
php artisan filament:install       # republish assets
composer remove filament/upgrade   # remove the temp package
php artisan filament:upgrade       # clear caches + publish frontend assets
```
**Order matters: upgrade Filament before upgrading Livewire to v3.** Some v2 plugins have no v3 build - remove/swap/wait or PR the author.

## Breaking changes to work through
- Consolidated config: `php artisan vendor:publish --tag=filament-config --force`; delete the old `config/forms.php`.
- **Env rename:** `FORMS_FILESYSTEM_DRIVER` -> `FILAMENT_FILESYSTEM_DISK`.
- **Blade:** `@livewireScripts`/`@livewireStyles` -> `@filamentScripts`/`@filamentStyles`; remove manual `module.esm.css` + `FormsAlpinePlugin` imports (auto-loaded now).
- **`->reactive()` -> `->live()`**; closure params typed as `Filament\Forms\Get` / `Filament\Forms\Set`.
- **Heroicons v2** rename (icon names changed); **`secondary` color removed** -> use `gray`.
- **DateTimePicker defaults to the native browser picker** -> `->native(false)` to restore the JS picker.
- `exists()` / `unique()` rule callback renamed to `modifyRuleUsing()`.
- Input masking now uses the Alpine masking package syntax.

## Source
[Official v2 -> v3 upgrade guide](https://filamentphp.com/docs/3.x/forms/upgrade-guide)
