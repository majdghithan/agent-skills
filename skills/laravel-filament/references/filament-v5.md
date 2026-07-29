# Filament v5 — reference

**Released:** January 16, 2026. **The one thing to understand:** v5 is "v4 running on Livewire 4." It ships **zero new Filament features** and **no Filament-level breaking changes** over v4 - the major bump exists purely because it swaps the underlying Livewire dependency from v3 to v4, which is a breaking change for anyone with custom Livewire code.

## Compatibility

| Dependency | Requirement |
|---|---|
| PHP | 8.2+ |
| Laravel | 11.28+ |
| **Livewire** | **4.0+** (the only floor that moved vs v4) |
| Tailwind CSS | 4.0+ |

## API: use the v4 reference

Filament v4 and v5 share essentially the entire public API surface - the same schemas, forms, tables, actions, resources, infolists, relation managers, widgets, and multi-tenancy. **If you are on v5, apply everything in `filament-v4.md` verbatim.** A developer fluent in v4 already knows v5; there is no separate v5 syntax to learn.

Confirmed by the launch post (Dan Harrin: *"Apart from Livewire v4 support, Filament v5 has no additional changes over v4"*), Laravel News, and independent write-ups (Sadique Ali, hafiz.dev). The major number reflects the dependency swap, not a redesign.

## What Livewire 4 unlocks (the real reason to be on v5)

The value of v5 is entirely what Livewire 4 brings to your existing Filament UI:

- **Parallel live updates** - `wire:model.live` requests now run in parallel instead of one-at-a-time. This is the most tangible win: live-bound Filament fields feel immediate instead of laggy.
- **Non-blocking polling** - a refreshing dashboard/widget no longer blocks other interactions.
- **Async actions** - run actions in parallel via the `.async` modifier.
- **Islands** - isolated regions that re-render independently for big perf gains.
- **Single-file / multi-file components**, **`wire:sort`** (built-in drag-and-drop), **`wire:intersect`**, **`wire:ref`**, slots + attribute forwarding, deferred loading.

For a Filament-only app (no hand-written Livewire), the felt benefit is mostly **snappier live forms and non-blocking widgets**. The newer primitives matter more when you author custom Livewire components.

## Upgrading is not urgent

The Filament team continues shipping features to **both v4 and v5** (Dan Harrin: *"We'll continue pushing features to both versions"*). Staying on v4 does not strand you on a frozen branch. Reasonable reasons to wait: a critical plugin lacks v5 support, you rely heavily on Tailwind v3 custom theming, or stability outweighs the Livewire 4 perf gains.

## Early v5 gotchas (verified)

- **`afterStateUpdatedJs` regression** ([#19054](https://github.com/filamentphp/filament/issues/19054)): JS state helpers stopped firing in early v5 due to a Livewire 4 interaction. Fixed in PR #19079; a follow-up for flex components landed in **v5.2.0**. If you hit this, upgrade to **>= v5.2**.
- **Upgrade-script false positives + Windows crash** ([#19246](https://github.com/filamentphp/filament/issues/19246)): the `filament-v5` script wrongly flagged an already-compatible plugin, and crashed on Windows (*"Prompts is not currently supported on Windows"*). Run the upgrade under **WSL**; temporarily remove a flagged plugin, finish, then reinstall its v5 version.

## Upgrading to v5

See `upgrades/v4-to-v5.md` - run the automated `filament-v5` script, then handle the Livewire v3 -> v4 changes for any custom Livewire code.

## Sources
- [Filament 5.x docs & upgrade guide](https://filamentphp.com/docs/5.x/upgrade-guide)
- [Introducing Filament v5 - Dan Harrin (official)](https://filamentphp.com/insights/danharrin-filament-v5-blueprint)
- [Filament v5 Released - Laravel News](https://laravel-news.com/filament-5)
- [Livewire 4.x upgrade guide](https://livewire.laravel.com/docs/4.x/upgrading)
- [What actually changed - Sadique Ali](https://sadiqueali.medium.com/filament-v5-is-out-heres-what-actually-changed-and-what-you-should-upgrade-for-first-bbd27cbbd80f) · [hafiz.dev](https://hafiz.dev/blog/filament-v5-released-whats-new-what-changed-and-should-you-upgrade)
