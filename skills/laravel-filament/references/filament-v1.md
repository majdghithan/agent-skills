# Filament v1 — reference

**Released:** March 2021 (line ran v1.0.0 -> v1.13.4). The first production-ready TALL-stack admin panel. **Rarely seen in the wild today** - if you find a v1 app, the priority is almost always to upgrade it (see `upgrades/v1-to-v2.md`), not to extend it.

> Depth caveat: v1's original docs site (`filamentadmin.com`) is dead. The surviving canonical source is the `docs/` markdown on the `1.x` GitHub branch. Anything beyond that (deep widget/theming internals) is effectively unarchived - treat as unverified.

## Compatibility (from `1.x` composer.json / package.json)

| Dependency | Constraint |
|---|---|
| PHP | `^7.4 \| ^8.0` |
| Laravel | `^8.0` (Laravel 8 only) |
| Livewire | `^2.6` |
| Alpine.js | `^2.8` (**Alpine v2**) |
| Tailwind CSS | `^2.1` (**Tailwind v2**, `@tailwindcss/jit`) |
| Icons | Heroicons v1 |

## What it was

A **single monolithic admin-panel package**. Forms and Tables existed only as sub-namespaces *inside* the admin package - not independently installable builders. v1 shipped its own **`filament_users` table** and dedicated authentication.

## Actual v1 API (note how different it is)

```php
// Filament v1
public static $model = Customer::class;   // untyped public static props
public static $label = 'customer';

use Filament\Resources\Forms\Form;        // note: Resources\Forms namespace
public static function form(Form $form)   // no return type
{
    return $form->schema([ /* ... */ ]);
}
```

**Form fields** - namespace `Filament\Resources\Forms\Components`:
```php
use Filament\Resources\Forms\Components;
Components\TextInput::make('name')->autofocus()->required(),
Components\Select::make('type'),
Components\BelongsToSelect::make('category_id')->relationship('category', 'name'),
```
Fields: `TextInput, Textarea, Select, Checkbox, Toggle, DatePicker, DateTimePicker, FileUpload, KeyValue, MarkdownEditor, RichEditor, TagsInput`.

**Table columns** - namespace `Filament\Resources\Tables\Columns`; **column classes have NO "Column" suffix**:
```php
use Filament\Resources\Tables\Columns;
use Filament\Resources\Tables\Filter;
->columns([
    Columns\Text::make('name')->primary(),   // ->primary() marks the clickable/link column
    Columns\Boolean::make('is_active'),
])
->filters([
    Filter::make('active', fn ($query) => $query->where('is_active', true)),  // closure as 2nd arg
])
```
Column classes: `Text, Boolean, Icon, Image, View`. Relations via a static `relations()` method; relation managers set static `$primaryColumn` and extend `Filament\Resources\RelationManager`.

## v1 conventions & gotchas

- Filters take the query closure as the **second argument** to `Filter::make()`.
- The clickable column is marked `->primary()`; there's no default-all-link behavior.
- v1 owns a `filament_users` table (real migration; `Filament::ignoreMigrations()` existed).

## Upgrading

To v2: see `upgrades/v1-to-v2.md`. In practice you'll usually go v1 -> v2 -> v3 -> v4/v5 in sequence.

## Sources
[Filament through the years](https://filamentphp.com/insights/alexandersix-filament-through-the-years) · [`1.x` branch docs & composer.json](https://github.com/filamentphp/filament/tree/1.x) · [Packagist release lines](https://packagist.org/packages/filament/filament)
