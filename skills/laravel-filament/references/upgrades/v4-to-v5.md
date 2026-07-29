# Upgrade: Filament v4 -> v5

Official guide: [filamentphp.com/docs/5.x/upgrade-guide](https://filamentphp.com/docs/5.x/upgrade-guide). **This is a small upgrade for Filament itself** - v5 has no Filament breaking changes. The real work is the **Livewire v3 -> v4** bump that comes with it, and only if you have custom Livewire code. Minimums are the same as v4 except **Livewire 4.0+**.

## Automated script
```bash
# 1. temporary upgrade tooling
composer require filament/upgrade:"^5.0" -W --dev
# 2. run the migration script (rewrites your code for v5)
vendor/bin/filament-v5
# 3. run the unique commands it prints, e.g.:
composer require filament/filament:"^5.0" -W --no-update
composer update
# 4. remove the tooling
composer remove filament/upgrade --dev
```
- **Windows:** use `~5.0` instead of `^5.0`, and prefer **WSL** - the script can crash on Windows (*"Prompts is not currently supported on Windows"*, [#19246](https://github.com/filamentphp/filament/issues/19246)).
- Review the script's changes - some manual adjustment may still be needed.
- Land on **>= v5.2** to get the `afterStateUpdatedJs` fix ([#19054](https://github.com/filamentphp/filament/issues/19054)).

## Third-party plugins
Some plugins may not have v5 releases yet. Options: temporarily remove them, swap for a v5-compatible equivalent, wait for the author, or PR the upgrade. Note the script may **false-positive** a plugin that already supports v5 (#19246) - verify before removing.

## The Livewire v3 -> v4 upgrade that rides along
The Filament script does **not** fully handle this. If you have custom Livewire components, follow the [Livewire 4.x upgrade guide](https://livewire.laravel.com/docs/4.x/upgrading). Key breaking changes:
- **Config renames:** `'layout'` -> `'component_layout'`, `'lazy_placeholder'` -> `'component_placeholder'`.
- **`wire:model` only listens for events on the element itself** - add **`.deep`** to restore v3 behavior for child-element events.
- **Sync-timing modifiers:** `.blur`/`.change` now control client-side sync; add **`.live`** to preserve v3's live-update behavior.
- **Component tags must be self-closing:** `<livewire:component />` (otherwise following markup is parsed as slot content).
- **`wire:transition` modifiers removed:** `.opacity`, `.scale`, `.duration` no longer supported.
- **Routing:** `Route::livewire()` is preferred and required for single-file/multi-file components.

**For most Filament-only projects (no hand-written Livewire), you won't need any of these.**

## Is it worth upgrading?
The payoff is entirely Livewire 4: parallel live updates (snappier live-bound forms), non-blocking polling/widgets, async actions, islands. The Filament team keeps shipping features to **both** v4 and v5, so it is not urgent. Reasonable to wait if a critical plugin lacks v5 support or you rely on heavy Tailwind v3 custom theming.

## Sources
[Filament 5.x upgrade guide](https://filamentphp.com/docs/5.x/upgrade-guide) · [Livewire 4.x upgrade guide](https://livewire.laravel.com/docs/4.x/upgrading) · [Introducing v5 - Dan Harrin](https://filamentphp.com/insights/danharrin-filament-v5-blueprint)
