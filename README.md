# agent-skills

Agent skills by [Majd Ghithan](https://github.com/majdghithan) - Full-Stack Engineer & Tech Lead. Open-format `SKILL.md` skills for Claude Code and other agents, installable with the [Skills CLI](https://skills.sh).

## Skills

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
