# Livewire v3 — reference

**Released:** v3.0.0 on 2023-08-24 (announced Laracon US 2023). Docs: use the explicit `livewire.laravel.com/docs/3.x/` prefix (the bare path now serves v4).

## Compatibility
| Dependency | Requirement |
|---|---|
| PHP | 8.1+ |
| Laravel | 10.x / 11.x |
| Alpine.js | **v3, bundled** with Livewire - remove manual Alpine CDN/script imports |

## Headline changes vs v2
- **`wire:model` is now DEFERRED by default** - real-time needs `.live`. (The single biggest v3 surprise.)
- New namespace/dirs: components in **`App\Livewire`** (was `App\Http\Livewire`); full-page layout at `resources/views/components/layouts/app.blade.php`.
- **Unified event API:** `emit*`/`dispatchBrowserEvent` all collapse into `dispatch()`; events bubble by default.
- **PHP-attribute API:** `#[Computed]`, `#[On]`, `#[Url]`, `#[Validate]`, `#[Locked]`, `#[Reactive]`, `#[Modelable]`, `#[Lazy]` under `Livewire\Attributes\*`.
- **`wire:navigate`** SPA navigation; **lazy components**; **form objects** (`Livewire\Form`).

## Core syntax
```php
namespace App\Livewire;
use Livewire\Component;
use Livewire\Attributes\{Url, Validate, Locked, Computed};

class Search extends Component
{
    #[Url(as: 'q', history: true, keep: true)] public $search = '';
    #[Validate('required|min:3')] public $title = '';
    #[Locked] public $id;                          // block client tampering

    #[Computed] public function results() { return Post::search($this->search)->get(); }  // $this->results in Blade
    public function render() { return view('livewire.search'); }
}
```
```blade
<input wire:model="title">                    {{-- DEFERRED (syncs on next action) --}}
<input wire:model.live="title">               {{-- real-time, 150ms debounce --}}
<input wire:model.live.debounce.250ms="title">
<input wire:model.blur="title">
<a href="/posts" wire:navigate>Posts</a>       {{-- SPA nav; .hover to prefetch --}}
<livewire:revenue lazy />                      {{-- lazy-load on viewport --}}
```
Events - `#[On]` + `dispatch()` (**params must be named**):
```php
$this->dispatch('post-created', title: $post->title);
$this->dispatch('post-created')->to(Dashboard::class);
#[On('post-created')] public function refresh($title) {}
```
Form objects:
```php
namespace App\Livewire\Forms;
use Livewire\{Form}; use Livewire\Attributes\Validate;
class PostForm extends Form {
    #[Validate('required|min:5')] public $title = '';
}
// in component: public PostForm $form;  ->  $this->validate(); Post::create($this->form->all());
// blade: <input wire:model="form.title">
```

## Best practices / gotchas
- `.live` only where you need it (search, live validation) - leave the rest deferred for fewer requests.
- Named event params are mandatory; `#[Locked]` any user-untouchable prop; `#[Computed]` for derived data.
- `boot()` runs every request, `mount()` only first - re-resolve models in `boot()`/computed.
- Alpine is already loaded - don't re-import it.
- Pagination page moved to `$this->paginators['page']` (`getPage()`/`setPage()`).

## Upgrade
From v2: `upgrades/v2-to-v3.md`. To v4: `upgrades/v3-to-v4.md`.

## Sources
[3.x docs](https://livewire.laravel.com/docs/3.x/quickstart) · [wire:model](https://livewire.laravel.com/docs/3.x/wire-model) · [events](https://livewire.laravel.com/docs/3.x/events) · [forms](https://livewire.laravel.com/docs/3.x/forms)
