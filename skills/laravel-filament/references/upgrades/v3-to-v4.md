# Upgrade: Filament v3 -> v4 (the big one)

Official guide: [github.com/filamentphp/filament/blob/4.x/docs/14-upgrade-guide.md](https://github.com/filamentphp/filament/blob/4.x/docs/14-upgrade-guide.md). New minimums: **PHP 8.2, Laravel 11.28+, Tailwind 4.1** (for custom themes). This is the version with real breaking changes - budget time and review the script's diff.

## Automated script
```bash
composer require filament/upgrade:"^4.0" -W --dev
vendor/bin/filament-v4
# run the unique commands it prints, then:
composer require filament/filament:"^4.0" -W --no-update
composer update
composer remove filament/upgrade --dev
```
- Windows PowerShell: use `"~4.0"` instead of `"^4.0"`.
- Requires **PHPStan v2+ / Larastan v3+** to run.
- Handles many mechanical changes (incl. namespace moves) but **not every** breaking change - review the diff.

Optional directory-structure migration (moves resources into the new nested layout):
```bash
php artisan filament:upgrade-directory-structure-to-v4 --dry-run
php artisan filament:upgrade-directory-structure-to-v4
```

## Namespace / API moves (the mechanical core)
- **Layout components** `Filament\Forms\Components\*` -> **`Filament\Schemas\Components\*`** (`Section`, `Grid`, `Fieldset`, `Tabs`, `Wizard`, ...). Fields stay in `Filament\Forms\Components`.
- **All actions** -> single **`Filament\Actions`** namespace (drop `Filament\Tables\Actions\*` etc.).
- `form(Form $form): Form` / `infolist(Infolist)` -> **`form(Schema $schema): Schema`** / `infolist(Schema)`; top-level `->schema([...])` -> `->components([...])`.
- Table: `->actions()` -> **`->recordActions()`**; `->bulkActions()` -> **`->toolbarActions()`**.

## Config
```bash
php artisan vendor:publish --tag=filament-config
```
- `default_filesystem_disk` -> `env('FILESYSTEM_DISK', 'public')`.
- New `file_generation.flags` block (`EMBEDDED_PANEL_RESOURCE_SCHEMAS`, `EMBEDDED_PANEL_RESOURCE_TABLES`, `PARTIAL_IMPORTS`, ...).

## High-impact behavior changes
1. **File visibility -> `private`** on non-local disks (`FileUpload`, `ImageColumn`, `ImageEntry`, Spatie variants). Restore with `->visibility('public')` or `Component::configureUsing(...)`.
2. **Tailwind v4 for custom themes:** theme CSS moves `@config 'tailwind.config.js'` -> `@source '...'`; run `npx @tailwindcss/upgrade`. `tailwind.config.js` is gone.
3. **Using Tailwind classes without a custom theme** now requires one: `php artisan make:filament-theme` then add `@source` paths.
4. **Table filters deferred** by default -> `->deferFilters(false)` to opt out.
5. **`Grid`/`Section`/`Fieldset` don't span full width** -> add `->columnSpanFull()`.

## Medium-impact
- **`unique()` `ignoreRecord` defaults to `true`** (global: `Field::uniqueValidationIgnoresRecordByDefault(false)`).
- **Pagination `'all'` removed** -> re-add via `->paginationPageOptions([5,10,25,50,'all'])`.
- **`columnSpan(2)` targets `>= lg`**; explicit breakpoint arrays still work.
- **Enum field state always returns the enum instance** (type closures `?MyEnum`).
- **URL query param renames:** `activeRelationManager->relation`, `activeTab->tab`, `tableFilters->filters`, `tableSearch->search`, `tableSort->sort`, `tableGrouping->grouping`, etc.
- **Tenancy: automatic global scoping + auto-association** - remove manual v3 scoping (it double-scopes now).
- `Radio::inline()` only lays out buttons now - use `->inline()->inlineLabel()` for the old label behavior.
- Import/Export jobs: 3 retries / 60s backoff (was 24h continuous).

## Low-impact / misc
- `make()` relaxed to `make(?string $name = null)` on many classes - use `getDefaultName()` / `setUp()`.
- Tables auto-sort by primary key -> `->defaultKeySort(false)` to opt out.
- **Authorization:** stop overriding `can*()`; use policies or `get*AuthorizationResponse()`.
- Removed table override methods: `getTableRecordUrlUsing()->recordUrl()`, `getTableRecordClassesUsing()->recordClasses()`, `isTableRecordSelectable()->checkIfRecordIsSelectableUsing()`.
- Locale renames: `pt_PT->pt`, `np->ne`, `no->nb`, `kh->km`.

## Deprecations
- **Spatie Translatable plugin** deprecated (no v4 build) -> replace with [lara-zeus/spatie-translatable](https://github.com/lara-zeus/spatie-translatable); the script offers migration commands.

## Source
[Official v3 -> v4 upgrade guide](https://github.com/filamentphp/filament/blob/4.x/docs/14-upgrade-guide.md)
