# Filament v3 — reference

**Released:** v3.0.0 on August 1, 2023. The widely-deployed stable line before v4. Verified against `filamentphp.com/docs/3.x`.

## Compatibility

| Dependency | Requirement |
|---|---|
| PHP | 8.1+ |
| Laravel | 10.0+ (also 11) |
| Livewire | **3.0+** (v2 dropped) |
| Tailwind CSS | 3.x |

Install:
```bash
composer require filament/filament:"^3.3" -W
php artisan filament:install --panels
php artisan make:filament-user
```
Add `@php artisan filament:upgrade` to the composer `post-autoload-dump` hook so assets republish after updates.

## Architecture — the "panel" concept (the v2 -> v3 headline)

Everything is organized around **Panels**. A panel is a self-contained Livewire app (its own path, auth, branding, resources, pages, widgets). You can run **multiple panels** (`/admin`, `/app`) in one Laravel install, each configured by its own Panel Provider (`Filament\Panel\PanelProvider`).

**Package structure** — a monorepo of standalone packages, each usable independently in any Livewire app:

| Package | Purpose | Namespace |
|---|---|---|
| `filament/filament` | Panel Builder | `Filament\` |
| `filament/forms` | Form Builder | `Filament\Forms\` |
| `filament/tables` | Table Builder | `Filament\Tables\` |
| `filament/actions` | Page/modal actions | `Filament\Actions\` |
| `filament/infolists` | Read-only displays | `Filament\Infolists\` |
| `filament/notifications` | Flash & DB notifications | `Filament\Notifications\` |
| `filament/widgets` | Stats/chart/table widgets | `Filament\Widgets\` |
| `filament/support` | Shared internals | `Filament\Support\` |

## Core syntax (v3 — note it differs from v4)

### Resource
```php
use Filament\Resources\Resource;
use Filament\Forms; use Filament\Forms\Form;
use Filament\Tables; use Filament\Tables\Table;

class CustomerResource extends Resource
{
    protected static ?string $model = Customer::class;
    protected static ?string $navigationIcon = 'heroicon-o-users';

    public static function form(Form $form): Form          // v3: Form (v4: Schema)
    {
        return $form->schema([                             // v3: ->schema([...])
            Forms\Components\TextInput::make('name')->required()->maxLength(255),
            Forms\Components\Select::make('status')
                ->options(['draft' => 'Draft', 'published' => 'Published'])
                ->required()->live(),                      // v3: ->live() (v2 was ->reactive())
        ])->columns(2);
    }

    public static function table(Table $table): Table
    {
        return $table
            ->columns([
                Tables\Columns\TextColumn::make('name')->searchable()->sortable(),
                Tables\Columns\TextColumn::make('author.name'),   // dot notation → eager-loaded
                Tables\Columns\IconColumn::make('is_featured')->boolean(),
            ])
            ->actions([Tables\Actions\EditAction::make()])         // v3: ->actions() (v4: ->recordActions())
            ->bulkActions([                                        // v3: ->bulkActions() (v4: ->toolbarActions())
                Tables\Actions\BulkActionGroup::make([Tables\Actions\DeleteBulkAction::make()]),
            ]);
    }

    public static function getRelations(): array { return [RelationManagers\PostsRelationManager::class]; }
    public static function getPages(): array
    {
        return [
            'index'  => Pages\ListCustomers::route('/'),
            'create' => Pages\CreateCustomer::route('/create'),
            'edit'   => Pages\EditCustomer::route('/{record}/edit'),
        ];
    }
}
```

**Namespace pattern (v3):** form components `Forms\Components\*`, columns `Tables\Columns\*`, table actions `Tables\Actions\*`, filters `Tables\Filters\*`. Actions have **two namespaces**: `Filament\Actions\Action` (page headers) vs `Filament\Tables\Actions\Action` (table actions). *(v4 collapses these into one `Filament\Actions` namespace.)*

### Relation managers
`php artisan make:filament-relation-manager CategoryResource posts title` → extends `Filament\Resources\RelationManagers\RelationManager` with its own `form(Form)` / `table(Table)`, registered via `getRelations()`.

### Widgets, actions, notifications
- Widgets under `Filament\Widgets\` (`StatsOverviewWidget` with `Stat::make('Label', $value)`, chart/table widgets); register via `getHeaderWidgets()` / `getFooterWidgets()` or `discoverWidgets()`.
- Actions open a modal (with embedded form), run directly, or `->url()`. `->requiresConfirmation()`, `->form([...])`, `->action(fn (array $data) => ...)`.
- `Filament\Notifications\Notification::make()->title('Saved')->success()->send()` (flash) / `->sendToDatabase($user)` (DB).

### Authorization (standard Laravel policies)
Filament calls `viewAny`, `view`, `create`, `update`, `delete` + **`deleteAny`** (bulk uses the `*Any` variants), `forceDelete*`, `restore*`, `reorder`. Escape hatch: `protected static bool $shouldSkipAuthorization = true;`.

### Multi-tenancy
```php
$panel->tenant(Team::class);   // + ->tenantRegistration(), ->tenantProfile(), ->tenantRoutePrefix()
```
User implements `Filament\Models\Contracts\HasTenants` (`getTenants()`, `canAccessTenant()`); read current with `Filament::getTenant()`. **In v3 you often add manual query scoping** — v4 auto-scopes, so don't carry v3 manual scopes into v4.

## Best practices (v3)

- **N+1:** dot-notation columns auto-eager-load; for extra relations/aggregates use `->modifyQueryUsing(fn (Builder $q) => $q->with('author')->withCount('comments'))`.
- **Validation** on the field: `->required()`, `->maxLength()`, `->email()`, `->unique(ignoreRecord: true)`, `->rules([...])`. Reactive fields need `->live()`.
- **Testing (Pest + Livewire):** `livewire(CreateCustomer::class)->fillForm([...])->call('create')->assertHasNoFormErrors()`, `assertCanSeeTableRecords($records)`, `callAction(...)`. Multi-panel: `Filament::setCurrentPanel(Filament::getPanel('app'))`.

## Common v3 gotchas

- `->reactive()` (v2) is now **`->live()`**; closure params typed as `Filament\Forms\Get`/`Set`.
- **DateTimePicker uses the native browser picker** by default — `->native(false)` for the JS picker.
- `secondary` color removed → use `gray`. Heroicons v2 (names changed).
- Env `FORMS_FILESYSTEM_DRIVER` → `FILAMENT_FILESYSTEM_DISK`.
- Blade `@livewireScripts`/`@livewireStyles` → `@filamentScripts`/`@filamentStyles`.

## Upgrading

From v2: see `upgrades/v2-to-v3.md`. To v4: see `upgrades/v3-to-v4.md` (the big break).

## Sources
[Installation](https://filamentphp.com/docs/3.x/panels/installation) · [Resources](https://filamentphp.com/docs/3.x/panels/resources/getting-started) · [Forms](https://filamentphp.com/docs/3.x/forms/getting-started) · [Tables](https://filamentphp.com/docs/3.x/tables/getting-started) · [Actions](https://filamentphp.com/docs/3.x/actions/overview) · [Tenancy](https://filamentphp.com/docs/3.x/panels/tenancy) · [Testing](https://filamentphp.com/docs/3.x/panels/testing) · [v3.0.0 release](https://github.com/filamentphp/filament/releases/tag/v3.0.0)
