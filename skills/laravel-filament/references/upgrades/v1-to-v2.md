# Upgrade: Filament v1 -> v2

Official guide: [filamentphp.com/docs/2.x/admin/upgrade-guide](https://filamentphp.com/docs/2.x/admin/upgrade-guide). The maintainer shipped **automated upgrade tooling** to handle the repetitive renames. First bump the platform: PHP 8.0, Laravel 8.6+, Alpine 3, Tailwind 3 (Livewire stays v2).

> Caveat: many web summaries conflate this with v2->v3. Items like `FILAMENT_FILESYSTEM_DISK`, Heroicons v2, `@filamentScripts`, typed `Get`/`Set`, and Livewire v3 belong to **v2->v3**, not here.

## Resources & pages
- `Filament\Resources\Forms\Form` -> `Filament\Resources\Form`; `Filament\Resources\Tables\Table` -> `Filament\Resources\Table`
- Property `$icon` -> `$navigationIcon`; `$primaryColumn` -> `$recordTitleAttribute`
- Method `relations()` -> `getRelations(): array`; `routes()` -> `getPages(): array`
- Pages register as `'index' => Pages\ListUsers::route('/')`

## Forms
- Namespace move: `Filament\Resources\Forms` -> `Filament\Forms`
- Removed `when()` / `only()` / `except()` -> use closures
- `dependable()` -> `reactive()`; `helpMessage()` -> `helperText()`
- Checkbox/Toggle `stacked()` -> `inline(false)`; Select `emptyOptionsMessage()` -> `searchPrompt()`
- TagsInput now stores JSON arrays -> add `separator(',')` for old behavior
- Layout components (Fieldset, Grid, Section, Tabs) take children via a `schema()` method instead of directly in `make()`

## Tables
- Namespace move: `Filament\Resources\Tables` -> `Filament\Tables`
- Column classes gain the `Column` suffix (`Text` -> `TextColumn`)
- `currency()` -> `money()`; `formatUsing()` -> `formatStateUsing()` (`$state` param); `getValueUsing()` -> `getStateUsing()`
- `primary()` removed - all columns link by default
- Filters use a dedicated `query()` method instead of the second `make()` argument

## Auth / config
- No `filament_users` table in v2 -> migrate access to `App\Models\User` + the **`FilamentUser`** interface (`canAccessFilament()`), authorization via policies
- Republish config: `php artisan vendor:publish --tag=filament-config --force`

## Medium / low
- Relation-manager base classes are relationship-specific now: `HasManyRelationManager`, `MorphManyRelationManager`, `BelongsToManyRelationManager`
- `Filament\Filament` facade -> `Filament\Facades\Filament`
- `Filament::ignoreMigrations()` removed (v2 has no migrations); theming rebuilt for Tailwind JIT
- **Never install a mix of v1 and v2 packages** (Composer dependency exception)

## Source
[Official v1 -> v2 upgrade guide](https://filamentphp.com/docs/2.x/admin/upgrade-guide) · [Discussion #495](https://github.com/filamentphp/filament/discussions/495)
