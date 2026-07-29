# Upgrade: Livewire v2 -> v3

Official guide: [livewire.laravel.com/docs/3.x/upgrading](https://livewire.laravel.com/docs/3.x/upgrading). New minimums: PHP 8.1, Laravel 10+.

## Automated path
```bash
composer require livewire/livewire "^3.0"
php artisan livewire:upgrade      # automates most breaking changes
php artisan view:clear
```
Remove any `livewire:discover` calls from build/deploy scripts.

## Namespace & directory moves
- `App\Http\Livewire` -> **`App\Livewire`** (or keep old location via `'class_namespace' => 'App\\Http\\Livewire'` in `config/livewire.php`).
- Layout `resources/views/layouts/app.blade.php` -> **`resources/views/components/layouts/app.blade.php`** (or set `'layout' => 'layouts.app'`).

## `wire:model` now deferred by default (the big one)
```
wire:model="..."        ->  wire:model.live="..."     (to KEEP v2 real-time behavior)
wire:model.defer="..."  ->  wire:model="..."          (deferred is the default now)
wire:model.lazy="..."   ->  wire:model.blur="..."
@entangle(...)          ->  @entangle(...).live
@entangle(...).defer    ->  @entangle(...)
```

## Event API (`emit` -> `dispatch`)
```
$this->emit('event')            ->  $this->dispatch('event')
$this->emitTo('foo','event')    ->  $this->dispatch('event')->to('foo')
$this->dispatchBrowserEvent(..) ->  $this->dispatch(..)
$this->emitUp(..)               ->  removed (events bubble by default)
```
All dispatch params must be **named**: `dispatch('event', postId: $id)`. Test helper `assertEmitted()` -> `assertDispatched()`.

## Alpine & scripts
- Livewire 3 bundles Alpine + core plugins - **remove manual Alpine CDN/script tags**.
- Custom bundle importing Alpine: replace `@livewireScripts` with `@livewireScriptConfig` and import from `vendor/livewire/livewire/dist/livewire.esm`.

## Other breaking changes
- Config removed: `app_url`, `asset_url`, `middleware_group`, `manifest_path`, `back_button_cache`.
- Component id: use `$this->getId()` (not `$this->id`).
- JS lifecycle: `livewire:load` -> `livewire:init`; `Livewire.onPageExpired()` -> `Livewire.hook('request', ...)`.
- Pagination: `$this->page = 2` -> `$this->paginators['page'] = 2`; remove `wire:click.prefetch`; re-publish pagination views.
- Query-string props now appear only once modified after load - use `#[Url(keep: true)]` to restore v2's always-present behavior.

## Source
[Official v2 -> v3 upgrade guide](https://livewire.laravel.com/docs/3.x/upgrading)
