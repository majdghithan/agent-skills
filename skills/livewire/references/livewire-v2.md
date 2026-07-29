# Livewire v2 — reference

**Released:** v2.0.0 on 2020-09-07. Tighter Alpine interop and better ergonomics. Docs on the legacy `laravel-livewire.com/docs/2.x`.

## Compatibility (from the v2.0.0 composer.json)
| Dependency | Constraint |
|---|---|
| PHP | `^7.2.5` |
| Laravel | `^7.0 \| ^8.0` |
| Alpine.js | **2.7.0+** if used, still loaded separately |

## What changed vs v1
Component definition, `wire:model`, `wire:click`, computed properties are **unchanged from v1** (so `wire:model` is still LIVE by default). New in v2: the `$wire` object + `@entangle`, `wire:model.defer`, the `$rules` property, scoped events, and a `history.pushState` query-string system.

## Key v2 additions
```php
// $rules property + argument-less validate() (NEW in v2; inline validate([...]) still works)
protected $rules = ['name' => 'required|min:6', 'email' => 'required|email'];
public function submit() { $this->validate(); }
public function updated($prop) { $this->validateOnly($prop); }
```
```php
// Events - scoped variants added
$this->emit('postAdded');                 // global
$this->emitUp('postAdded');               // to parent
$this->emitTo('counter', 'postAdded');    // to a named component
$this->emitSelf('postAdded');             // self only (NEW)
$this->dispatchBrowserEvent('name-updated', ['newName' => $v]);  // browser event (NEW)
protected $listeners = ['postAdded' => 'incrementPostCount'];
```
```blade
{{-- @entangle: two-way bind Livewire <-> Alpine (NEW in v2) --}}
<div x-data="{ open: @entangle('showDropdown') }">...</div>
<div x-data="{ open: @entangle('showDropdown').defer }">...</div>
<input wire:model.defer="title">   {{-- batch value with next request (NEW) --}}
```
`$wire` inside Alpine: `$wire.foo`, `$wire.someMethod(p)`, `$wire.get/set('prop', v)`, `$wire.emit(...)`, `$wire.on(...)`.

Lifecycle (expanded): adds `boot`/`booted`, `dehydrate`, per-property `hydrateFoo`/`dehydrateFoo`.

Query string: property renamed `$updatesQueryString` -> **`$queryString`**; uses `history.pushState` and auto-populates from the URL on load.

## Gotchas
- `wire:model` still **live by default** (v3 flips this).
- Routing moved to standard `Route::get('/path', Component::class)`.
- Default pagination theme switched to **Tailwind** (`protected $paginationTheme = 'bootstrap';` to restore).
- Layout injection moved into the component's `render()` (`->extends()->section()`).

## Upgrade
From v1: `upgrades/v1-to-v2.md`. To v3: `upgrades/v2-to-v3.md`.

## Sources
[v2 events](https://laravel-livewire.com/docs/2.x/events) · [v2 Alpine](https://laravel-livewire.com/docs/2.x/alpine-js) · [v2 validation](https://laravel-livewire.com/docs/2.x/input-validation)
