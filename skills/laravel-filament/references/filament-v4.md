# Filament v4 — reference

**Released:** v4.0 stable on August 12, 2025 (beta June 10, 2025). The big architectural break from v3. Verified against `filamentphp.com/docs/4.x` and the 4.x upgrade guide. **Note:** v5 (Jan 2026) shares v4's entire API — if you're on v5, use this file plus `filament-v5.md`.

## Compatibility

| Dependency | Requirement |
|---|---|
| PHP | 8.2+ |
| Laravel | 11.28+ / 12 / 13 |
| Livewire | ^3.5 |
| Tailwind CSS | 4.1+ (only for custom themes) |
| doctrine/dbal | **no longer required** by Filament |

Packages (lock-step versioned): `filament/filament`, **`filament/schemas`** (new), `filament/forms`, `filament/infolists`, `filament/tables`, `filament/actions`, `filament/notifications`, `filament/widgets`, `filament/support`.

## Headline changes vs v3

### 1. Schema unification (the big one)
Forms and infolists are now both built on a single package **`filament/schemas`**, exposing **`Filament\Schemas\Schema`** - a generic container that can mix editable fields, read-only entries, and layout components in one tree. `filament/forms` and `filament/infolists` became thin component layers on top.

**Practical fallout: layout components moved namespace** from `Filament\Forms\Components\*` to **`Filament\Schemas\Components\*`** (`Section`, `Grid`, `Fieldset`, `Flex`, `Tabs`, `Wizard`, ...). Fields stay in `Filament\Forms\Components\*`.

### 2. Actions namespace consolidation
All actions now live under one **`Filament\Actions`** namespace, replacing v3's context-specific ones (`Filament\Tables\Actions\*`, etc.). One `Filament\Actions\Action` / `BulkAction` / `ActionGroup` / `BulkActionGroup` everywhere.

### 3. Performance
~2-3x faster server-side render on large tables (fewer Blade includes, Tailwind classes extracted via `@apply`). New partial-render controls (`partiallyRenderComponentsAfterStateUpdated()`, `skipRenderAfterStateUpdated()`) and JS-driven helpers that skip a round-trip (`hiddenJs()`/`visibleJs()`, `afterStateUpdatedJs()`, `JsContent`).

### 4. Tailwind v4
Framework CSS on Tailwind v4; colors moved `rgb` -> **`oklch`**. `tailwind.config.js` is gone; theming uses CSS `@source` directives.

### 5. Other additions
Nested resources (hierarchical breadcrumbs/URLs); **static data tables** (`$table->records(...)`, no Eloquent needed); Rich Editor rebuilt on TipTap; new fields Slider / Code Editor / Table Repeater / ModalTableSelect; built-in **MFA** (TOTP + email); `authorizeIndividualRecords()` on bulk actions.

## Core syntax (v4 - and where it differs from v3)

### Schema (unified form/infolist)
```php
use Filament\Schemas\Schema;
use Filament\Schemas\Components\Section;   // v3: Filament\Forms\Components\Section
use Filament\Forms\Components\TextInput;   // fields stay here

public static function form(Schema $schema): Schema   // v3: form(Form $form): Form
{
    return $schema->components([            // v3: $form->schema([...])
        Section::make('Details')->schema([
            TextInput::make('name')->required(),
        ]),
    ]);
}

public static function infolist(Schema $schema): Schema { /* v3 took Infolist; now Schema */ }
```

### Tables (action renames)
```php
use Filament\Tables\Table;
use Filament\Tables\Columns\TextColumn;
use Filament\Actions\Action;          // v3: Filament\Tables\Actions\Action
use Filament\Actions\BulkAction;
use Filament\Actions\ActionGroup;

public function table(Table $table): Table
{
    return $table
        ->columns([ TextColumn::make('title')->searchable() ])
        ->recordActions([                 // v3: ->actions([...])
            ActionGroup::make([ Action::make('edit')->url(fn ($r) => route('posts.edit', $r)) ]),
        ])
        ->toolbarActions([                // v3: ->bulkActions([...])
            BulkAction::make('delete')->action(fn ($records) => $records->each->delete()),
        ])
        ->headerActions([ Action::make('create') ]);
}
```

**v3 -> v4 rename cheat-sheet:** `form(Form)`/`infolist(Infolist)` -> `form(Schema)`/`infolist(Schema)`; layout components -> `Filament\Schemas\Components`; all actions -> `Filament\Actions`; `->actions()` -> `->recordActions()`; `->bulkActions()` -> `->toolbarActions()`.

### Multi-tenancy & authorization (behavior changes)
- **Tenancy auto-scopes all panel queries** to the current tenant and **auto-associates** new records via model events - the manual `getEloquentQuery()` scoping from v3 is usually no longer needed (and can double-scope if carried over).
- **Authorization:** stop overriding `can*()` methods; put logic in **model policies**. For custom responses override `get*AuthorizationResponse()` (returns a policy response, not a bool). Per-record bulk checks via `authorizeIndividualRecords()`.

## Best practices & gotchas (v4)

- **Import layout components from `Filament\Schemas\Components`** - the #1 silent break when pasting v3 code.
- **One action namespace:** always `use Filament\Actions\...`.
- **File visibility on non-local disks is now `private`** - add `->visibility('public')` if you serve files directly.
- **Table filters are deferred** (Apply button) by default - opt out with `->deferFilters(false)`.
- **`Section`/`Grid`/`Fieldset` no longer span full width** - add `->columnSpanFull()` to restore the v3 look.
- **`unique()` ignores the current record by default** now (pass `ignoreRecord: false` to include it).
- **Enum fields always return the enum instance** (or null) - type `afterStateUpdated` closures as `?MyEnum`.
- **Env:** use `FILESYSTEM_DISK` (v4), not `FILAMENT_FILESYSTEM_DISK` (v3).
- `columnSpan(2)` targets `>= lg` by default; tables auto-sort by primary key (opt out `->defaultKeySort(false)`).

## Upgrading

From v3: see `upgrades/v3-to-v4.md` (the big one). To v5: see `upgrades/v4-to-v5.md` (mostly Livewire v4).

## Sources
[v4 is Stable](https://filamentphp.com/insights/alexandersix-filament-v4-is-stable) · [What's new in v4](https://filamentphp.com/content/leandrocfe-whats-new-in-filament-v4) · [Docs: Overview](https://filamentphp.com/docs/4.x/introduction/overview) · [Schemas](https://filamentphp.com/docs/4.x/schemas/overview) · [Tables/Actions](https://filamentphp.com/docs/4.x/tables/actions) · [Upgrade guide](https://github.com/filamentphp/filament/blob/4.x/docs/14-upgrade-guide.md)
