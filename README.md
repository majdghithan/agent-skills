# agent-skills

Agent skills by [Majd Ghithan](https://github.com/majdghithan) - Full-Stack Engineer & Tech Lead. Open-format `SKILL.md` skills for Claude Code and other agents, installable with the [Skills CLI](https://skills.sh).

## Skills

| Skill | What it does |
|---|---|
| [`laravel-filament`](skills/laravel-filament) | Version-aware Filament best practices (v1-v5) + every upgrade path |
| [`livewire`](skills/livewire) | Version-aware Livewire best practices (v1-v4) + every upgrade path |
| [`filament-plugin-development`](skills/filament-plugin-development) | Build & publish custom Filament plugins (v4/v5): contract, assets, hooks, publishing |
| [`laravel-architecture-review`](skills/laravel-architecture-review) | Audit a Laravel codebase's design (runs Larastan/Rector/Pest + anti-dogma heuristics) and report where logic belongs |
| [`laravel-upgrade`](skills/laravel-upgrade) | Upgrade Laravel across majors (8 -> 13) one hop at a time: runtime bites + when to use Shift |
| [`laravel-mysql-to-postgres`](skills/laravel-mysql-to-postgres) | Migrate a Laravel app from MySQL to PostgreSQL without silent breakage |
| [`laravel-mixpost`](skills/laravel-mixpost) | Self-host & operate Mixpost (install, providers, scheduling, gotchas) |
| [`geo-llm-optimization`](skills/geo-llm-optimization) | Get cited inside AI-assistant answers (GEO): crawlers, structure, llms.txt |
| [`skill-authoring`](skills/skill-authoring) | Author, verify, and publish a high-quality agent skill (the meta-skill) |

Install any skill with `npx skills add majdghithan/agent-skills --skill <name>` (or `--all`).

### `laravel-filament`

Version-aware best practices for [Filament](https://filamentphp.com) (the Laravel admin-panel / TALL-stack framework), covering **v1 through v5** plus every upgrade path. It detects the installed Filament major version first (the API differs a lot between majors, especially v3 -> v4) and then applies only that version's rules.

**Install:**

```bash
npx skills add majdghithan/agent-skills --skill laravel-filament
```

**Covers:**

| Version | Era | Upgrade guide |
|---|---|---|
| v1 | Earliest release, pre-panel | - |
| v2 | TALL-stack admin panel (Livewire 2) | v1 -> v2 |
| v3 | Unified panels, split packages | v2 -> v3 |
| v4 | Schema unification + performance rewrite (big break from v3) | v3 -> v4 |
| v5 | v4 API + Livewire v4 support | v4 -> v5 |

Every version has a dedicated reference (real namespaces, class names, method signatures, patterns, gotchas) under `skills/laravel-filament/references/`, and each upgrade path has its own guide under `references/upgrades/`.

## License

MIT (c) Majd Ghithan. Skill content is provided as-is; verify version-specific API against the official [Filament docs](https://filamentphp.com/docs) for your exact version.
