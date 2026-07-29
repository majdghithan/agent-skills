# Upgrade: Livewire v3 -> v4

Official guide: [livewire.laravel.com/docs/4.x/upgrading](https://livewire.laravel.com/docs/4.x/upgrading). This is the version Filament v5 requires. The two silent regressions to watch: **`wire:model` stops bubbling** and **`.blur`/`.change` no longer send a request**.

## Config renames (`config/livewire.php`)
```
'layout'           ->  'component_layout'
'lazy_placeholder' ->  'component_placeholder'
```
Also: smart `wire:key` default flipped `false` -> `true`.

## `wire:model` - listens on the element only now
```blade
<div wire:model="value"><input></div>        {{-- v3 caught bubbling child events --}}
<div wire:model.deep="value"><input></div>   {{-- v4: add .deep to restore that --}}
```

## `wire:model` sync-timing modifiers imply client-only now
| v3 | v4 (to also send a request) |
|---|---|
| `wire:model.blur` | `wire:model.live.blur` |
| `wire:model.change` | `wire:model.live.change` |
Bonus: square brackets in `wire:model` are now property accessors - `wire:model="items[0].name"`.

## Component tags must be self-closing
```blade
<livewire:component-name />   {{-- else trailing markup becomes slot content --}}
```

## `wire:transition` modifiers removed (now View Transitions API)
`wire:transition` still works; `.opacity`, `.scale`, `.duration`, `.origin.*` are removed.

## `Route::livewire()` - required for single-file / multi-file page components
```php
Route::livewire('/dashboard', Dashboard::class);
Route::livewire('/dashboard', 'pages::dashboard');
```

## Other breaking changes
- `wire:scroll` -> `wire:navigate:scroll`.
- Streaming: `$this->stream('#el', 'text')` -> `$this->stream('text', el: '#el')` (or `->to(ref: 'name')`).
- Asset URL prefix `/livewire/` -> `/livewire-{hash}/` (hash from `APP_KEY`) - update firewall/middleware.
- JS: `$wire.$js('name', fn)` -> `$wire.$js.name = fn`; hooks `commit`/`request` -> `interceptMessage`/`interceptRequest`.

## Volt folds into core v4
- `Livewire\Volt\Component` -> `Livewire\Component`
- `Volt::route()` -> `Route::livewire()`; `Volt::test()` -> `Livewire::test()`
- Remove `VoltServiceProvider` from `bootstrap/providers.php`; `composer remove livewire/volt`.

## Source
[Official v3 -> v4 upgrade guide](https://livewire.laravel.com/docs/4.x/upgrading)
