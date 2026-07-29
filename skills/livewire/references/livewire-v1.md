# Livewire v1 — reference

**Released:** v1.0.0 on 2020-02-26. The first stable Livewire. Rarely seen today - if you find it, prioritize upgrading (see `upgrades/v1-to-v2.md`). v1/v2 docs live on the legacy `laravel-livewire.com/docs/1.x`.

## Compatibility (from the v1.0.0 composer.json)
| Dependency | Constraint |
|---|---|
| PHP | `^7.1.3` |
| Laravel | `~5.6 \| ~5.7 \| ~5.8 \| ^6.0 \| ^7.0` |
| Alpine.js | optional, **loaded separately** (Livewire did not bundle Alpine until v3) |

## Core syntax
```php
namespace App\Http\Livewire;   // note: App\Http\Livewire (v3 moves this to App\Livewire)
use Livewire\Component;

class Counter extends Component
{
    public $message = 'Hello';   // public props are exposed to the browser - no secrets
    public function render() { return view('livewire.counter'); }
}
```
Blade view `resources/views/livewire/counter.blade.php` - **single root element required**. Layout uses `@livewireStyles` / `@livewireScripts`; render with `@livewire('counter')`.

```blade
<input wire:model="message">                 {{-- v1: LIVE by default (updates as you type) --}}
<input wire:model.lazy="message">            {{-- sync on change, not keystroke --}}
<input wire:model.debounce.500ms="name">
<button wire:click="doSomething">Go</button>
<form wire:submit.prevent="save">...</form>
```
Magic actions: `$refresh`, `$set('prop', v)`, `$toggle('prop')`, `$emit('event', ...params)`.

Computed: `public function getPostProperty() { return Post::find($this->postId); }` -> access `$this->post`.

Validation (inline only in v1 - no `$rules` property yet):
```php
public function submit() { $this->validate(['name' => 'required|min:6', 'email' => 'required|email']); }
public function updated($field) { $this->validateOnly($field, [...]); }   // real-time
```
Lifecycle hooks (narrower than v2): `mount`, `hydrate`, `updating`, `updated`, `updatingFoo`, `updatedFoo`. Routing used `Route::livewire(...)`.

## Gotchas
- `wire:model` is **live by default** (opposite of v3+).
- Public properties serialize to the front end - never store sensitive data.
- Single root element; rules are inline (no `$rules`).

## Upgrade
To v2: `upgrades/v1-to-v2.md`. In practice, go v1 -> v2 -> v3 -> v4 in sequence.

## Sources
[Livewire 1.0 - Laravel News](https://laravel-news.com/laravel-livewire-1-0-0) · [v1 docs (legacy)](https://laravel-livewire.com/docs/1.x/quickstart)
