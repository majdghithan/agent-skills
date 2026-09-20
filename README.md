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
| [`lahja`](skills/lahja) | Write Arabic in a real dialect (8 dialects): grammar, not sample words. Composes with fasih |
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

### `lahja` (لهجة)

Arabic dialects writing skill. Most AI "dialect" text swaps a few words (بدي for أريد) but keeps formal grammar (سوف, لقد, ليس, أنْ), so it still reads as translated فصحى. lahja fixes the grammar layer. It detects the dialect (or asks one question), then loads one of eight per-dialect guides covering negation, future and aspect markers, demonstratives and question words, pronouns, spelling habits, MSA leaks to remove, how English tech terms sit inside dialect text, and worked MSA -> dialect rewrites. Every grammar claim is cited.

**Built on the fasih method.** lahja follows the approach of [fasih](https://github.com/maherelgamil/fasih-skill) by Maher El Gamil, the Arabic writing and editing skill: natural Arabic over literal translation, adapt rather than translate word for word, never invent a fact or a form, keep the register consistent, and keep `SKILL.md` lean with the depth in `references/`. fasih covers Arabic levels and tone and deliberately keeps dialect short (its `tone-and-dialects.md` is about 30 lines); lahja is the dialect-grammar layer built under that same method. Credit for the approach goes to Maher; lahja is not affiliated with or endorsed by the fasih project.

lahja is standalone; if fasih is installed alongside it, the agent invokes fasih for editorial quality (meaning, tone, microcopy) while lahja owns the dialect forms.

**Install:**

```bash
npx skills add majdghithan/agent-skills --skill lahja
```

**Coverage:**

| Dialect | Anchor | Also covers | Guide |
|---|---|---|---|
| Levantine | urban Palestinian | rural Palestinian, Jordanian, Syrian, Lebanese | `references/levantine.md` |
| Egyptian | Cairene | - | `references/egyptian.md` |
| Gulf | Kuwaiti | Emirati, Najdi, Hejazi | `references/gulf.md` |
| Iraqi | Baghdadi (gilit) | southern Iraqi, Mosuli qeltu | `references/iraqi.md` |
| Maghrebi | Moroccan Darija | Algerian, Tunisian | `references/maghrebi.md` |
| Libyan | Tripoli | eastern Libyan | `references/libyan.md` |
| Sudanese | Khartoum | - | `references/sudanese.md` |
| Yemeni | Sanaani | Adeni, Hadhrami | `references/yemeni.md` |

Each guide cites its sources and marks what it does not cover, so the agent leaves a gap open instead of inventing a form.

**Feedback and contributions welcome.** A skill may help or may not, and Arabic dialects vary by city, generation, and family. If you hit an error, or a dialect you speak is missing or handled badly, email **majd.ghithan20@gmail.com**, or open an issue or PR here. The most useful corrections name the form, the region, and who uses it.

## License

MIT (c) Majd Ghithan. Skill content is provided as-is; verify version-specific API against the official [Filament docs](https://filamentphp.com/docs) for your exact version.
