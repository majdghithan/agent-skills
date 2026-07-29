# Filament v2 — reference

**Released:** staged in 2021 - Forms (Aug/Sep), Tables (Sep/Oct), Admin Panel officially **Dec 9, 2021**. The release that split Filament into independent packages and set its signature look.

## Compatibility (from `2.x` composer.json / package.json)

| Dependency | Constraint |
|---|---|
| PHP | `^8.0` |
| Laravel | `^8.6 \| ^9.0 \| ^10.0` (widened over the v2 lifecycle) |
| Livewire | `^2.10` (**still Livewire v2**) |
| Alpine.js | `^3.9` (**upgraded to Alpine v3**) |
| Tailwind CSS | `^3.0` (**upgraded to Tailwind v3** JIT) |
| Icons | Heroicons v1 |

## What it was — the headline change

v2 **split the monolith into independent packages**: Admin Panel, Forms, Tables, Notifications (+ Support, + Spatie plugins). **Forms and Tables became standalone builders usable in any Livewire component**, not just the admin panel. Added reactive forms, dark mode, the visual redesign, a Notifications package, relation managers, 50+ field types, JSON repeaters, block/page builder, Spatie Media Library support.

## Actual v2 API

Resources use typed `form(Form $form): Form` / `table(Table $table): Table` with the **flattened** `Filament\Forms` / `Filament\Tables` namespaces:

```php
// Filament v2
use Filament\Forms;
use Filament\Tables;

public static function form(Form $form): Form
{
    return $form->schema([
        Forms\Components\TextInput::make('name')->required(),
        Forms\Components\TextInput::make('email')->email()->required(),
    ]);
}

public static function table(Table $table): Table
{
    return $table
        ->columns([
            Tables\Columns\TextColumn::make('name'),   // "Column" suffix now required (v1 had none)
            Tables\Columns\TextColumn::make('email'),
        ])
        ->filters([ /* ... */ ])
        ->actions([ Tables\Actions\EditAction::make() ]);
}
```
Standalone use (outside a panel): a Livewire component implementing the table/form contracts defines `getTableColumns()` / `getFormSchema()`.

## v2 conventions & gotchas

- **No `filament_users` table.** Grant access by pointing Filament at `App\Models\User` and implementing the **`FilamentUser`** interface (`canAccessFilament()`); authorization runs through **policies**; roles are your own concern.
- Column classes carry the `Column` suffix now (`TextColumn`, `IconColumn`, ...), and **all columns link by default** (v1's `->primary()` is gone).
- Reactivity uses **`->reactive()`** (v3 later renames this to `->live()`).
- **Never mix v1 and v2 packages** - Composer will throw a dependency exception.

## Upgrading

From v1: `upgrades/v1-to-v2.md`. To v3: `upgrades/v2-to-v3.md`.

## Sources
[Filament through the years](https://filamentphp.com/insights/alexandersix-filament-through-the-years) · [Staged-release discussion #495](https://github.com/filamentphp/filament/discussions/495) · [Docs 2.x: Resources](https://filamentphp.com/docs/2.x/admin/resources/getting-started) · [Tables](https://filamentphp.com/docs/2.x/tables/getting-started)
