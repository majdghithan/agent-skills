# Livewire v4 — reference

**Released:** v4.0.0 on 2026-01-14 (announced Laracon US 2025). This is the version **Filament v5 requires**. Docs: `livewire.laravel.com/docs/4.x`.

## Compatibility
| Dependency | Requirement |
|---|---|
| PHP | 8.1+ (**8.4** needed for the property-hooks feature) |
| Laravel | 10+ |
| Alpine | bundled (Alpine 3) |

## Headline features
- **Single-file components (SFC) - the new default:** class + view (+ optional JS/CSS) in one Blade file. Also multi-file components (`--mfc`).
- **Islands:** regions that re-render independently (`@island ... @endisland`) - an action inside an island re-renders only that island.
- **Parallel live updates & async actions:** `wire:model.live` and `.async`/`#[Async]` actions can run in parallel, bypassing the request queue.
- **Non-blocking polling** (`wire:poll` auto-throttles background tabs, `.visible`).
- **`wire:sort`** (drag-and-drop), **`wire:intersect`** (viewport), **`wire:ref`** (name/target an element or component).
- **`Route::livewire()`** - required for SFC/MFC page components.
- Blaze compiler (static parts pre-rendered), smarter `data-loading` states, Volt folded into core.

## Core syntax
```blade
{{-- resources/views/components/post/create.blade.php (single-file) --}}
<?php use Livewire\Component;
new class extends Component {
    public string $title = '';
    public function save() { $this->validate(['title' => 'required|max:255']); }
};?>
<div>
    <input wire:model="title">
    <button wire:click="save">Save</button>
</div>
```
Create: `php artisan make:livewire post.create` (page: `make:livewire pages::dashboard`). Route: `Route::livewire('/dashboard', 'pages::dashboard');`.

Islands / async / new directives:
```blade
@island(name: 'revenue', lazy: true)
    @placeholder <div class="animate-pulse h-32"></div> @endplaceholder
    <div>Revenue: {{ $this->revenue }} <button wire:click="$refresh">Refresh</button></div>
@endisland
<button wire:click="loadMore" wire:island.append="feed">Load more</button>   {{-- infinite scroll, no JS --}}

<button wire:click.async="logActivity">Track</button>
<ul wire:sort="handleSort">@foreach ($tasks as $t)<li wire:key="{{ $t->id }}" wire:sort:item="{{ $t->id }}">...</li>@endforeach</ul>
<div wire:intersect="loadMore"></div>
<input wire:model.blur.live="title">     {{-- .blur is sync-timing only now; add .live to send a request --}}
<div wire:model.deep="value"><input></div>{{-- opt back into child-element events --}}
```

## Best practices / early gotchas
- **`.async` only for fire-and-forget** (analytics, logging). Never mutate UI-reflected state in an async action - parallel execution = race conditions.
- **`wire:model` no longer bubbles** - custom-input wrappers relying on child events break silently; add `.deep`. (Most likely silent upgrade regression.)
- **`.blur`/`.change` no longer hit the server** on their own - add `.live`.
- **Self-closing component tags are mandatory:** `<livewire:foo />`.
- **Islands can't sit directly inside `@foreach`/`@if`** and don't see outer loop variables - move the control flow inside.
- **Asset URL prefix changed** `/livewire/` -> `/livewire-{hash}/` (from `APP_KEY`) - update WAF/middleware allowlists.
- Prefer PHP 8.4 property hooks over simple `updated*` hooks; use `data-[loading]:*` over manual `wire:loading`.

## Upgrade
From v3: `upgrades/v3-to-v4.md` (includes Volt migration).

## Sources
[4.x docs](https://livewire.laravel.com/docs/4.x/quickstart) · [islands](https://livewire.laravel.com/docs/4.x/islands) · [wire:model](https://livewire.laravel.com/docs/4.x/wire-model) · [upgrade guide](https://livewire.laravel.com/docs/4.x/upgrading) · [Livewire 4 - Laravel blog](https://laravel.com/blog/livewire-4-is-here-the-artisan-of-the-day-is-caleb-porzio)
