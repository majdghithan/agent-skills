# Levantine Arabic (شامي / فلسطيني) - writing guide

**Coverage:** urban Palestinian, with notes where rural Palestinian, Jordanian, Syrian, and Lebanese differ. This is the deepest guide in the skill. Every form below is cited to the sources at the end; anything the sources didn't settle is marked and must not be generated.

**Tags:** `[S]` South Levantine (Palestinian + Jordanian), `[N]` North Levantine (Syrian + Lebanese), `[PU]` urban Palestinian, `[PR]` rural Palestinian, `[J]` Jordanian, `[Syr]` Syrian, `[Leb]` Lebanese. Bracketed keys like `[LAG]` point to Sources at the end.

## 0. Pick the sub-dialect, then stay in it

Default is **urban Palestinian** unless the user names another. Keep every row in one column for the whole text.

| Feature | Urban Palestinian (default) | Rural Pal. / Jordanian | Syrian | Lebanese |
|---|---|---|---|---|
| "not" + noun/adjective | مش | مش | مو | مش |
| "not" + verb | ما (ما...ش less common) | ما...ش / ...ش common | ما | ما |
| Future | رح + subjunctive: رح أروح | رح أروح | رح | رح, also رح + بـ-verb: رح بروح |
| In progress | عم (بشتغل) or plain بـ | قاعد + verb | عم | عم |
| "we" | إحنا | إحنا | نحنا | نحنا |
| "they" | همّ | همّ | هنّ / هنّي | هنّ / هنّي |
| "your" (pl) / "their" | ـكم / ـهم | ـكم / ـهم | ـكن / ـهن | ـكن / ـن |
| "now" | هلأ / هلق | هسّا [J], هلقيت [PR] | هلق | هلّق |
| "this" (m / f) | هاد(ا) / هاي | هاد / هاي (هذا is native in rural [J]) | هاد / هيّ | هيدا / هيدي |
| "thing" | إشي | إشي | شي | شي |

Sources: [LAG] [PalWiki] [JordWiki] [Wikt-rah] [Hoyt10] [Wikt-am].

## 1. Negation

- **ما + verb or pseudo-verb** (past and present, all Levantine): ما كتب، ما بحكي إنجليزي، ما بدي، ما عندي وقت، ما في مشكلة. [LAG] [TLT-neg]
- **مش + everything that isn't a conjugated verb**: adjectives, participles, nouns, prepositional phrases, ممكن/لازم: الكود مش جاهز، مش عارف، مش ممكن، مش هون. Syrian uses **مو** in the same slot: مو منيح. [LAG] [Hoyt10]
- **Negated future**: ما رح أروح = مش رح أروح (both fine). [LAG] [Wikt-rah]
- **ما...ش circumfix** `[S]`, also rural Syria/Lebanon: ما بعرفش، ما كتبش. The host must be one word with a person marker (verb, كان, عندي, في). **Less common in urban Palestinian**, so the default voice uses plain ما; use ما...ش for a rural or Jordanian voice. [Hoyt10] [Obeidat22]
- **ش alone, without ما** `[S]`: only on بـ-imperfect, بدّ-, في, مع-, and prohibitions: بعرفش، بديش، فيش. Never on the past tense: ~~شربش~~. [LAG] [Obeidat22]
- **Existential**: ما في `[all]`; مافيش / فيش `[S]`. [TLT-neg] [Hoyt10]
- **Prohibition (don't)**: ما تنسى `[all]`, ما تنساش / تنساش `[S]`. لا تنسى also occurs; sources disagree on how formal it sounds, so prefer ما تنسى. [WBneg] [TLT-neg]
- **Emphatic negative pronouns** ("I'm NOT"): `[S]` مانيش، مانتاش، ماهوش; `[N]` ماني، مانك، مانو. Use sparingly, for emphasis only. [Hoyt10] [TLT-neg]
- **Unverified - don't generate by default:** مش + بـ-verb (مش بعرف). Sources only confirm مش with non-verbs.

## 2. Future

- **رح + verb** is the default. `[S]` uses the **subjunctive (no بـ)**, and 1sg keeps أ: رح أروح، رح نبلّش، رح يعمل. [Wikt-rah] [LAG]
- **رح + بـ-verb** (رح بروح) is **mainly Lebanese**. Don't use it in a Palestinian text. [Wikt-rah]
- **حـ prefix** (حشوفك بكرة) is attested Levantine but less typical; pick رح or حـ and don't alternate. [LAG] [CODA]
- **Intent / near future**: بدّي + subjunctive: بدي أخلّص الـ PR بكرة. [LAG]
- **Plain بـ-present** can carry a planned future: بشوفك بكرة. [LAG]

## 3. Aspect and mood

- **بـ prefix = indicative** (present, habitual, planned): بكتب، بتكتب، بيكتب. Palestinian 1sg: بَكتب; Palestinian 3ms: بِكتب (Lebanese/Syrian بيكتب). [LAG] [PalWiki]
- **1pl** "we do": منكتب and بنكتب both occur in Palestine (منـ is described as more common, بنـ as Jerusalem). **Choose one and keep it.** [LAG]
- **In progress right now**: عم `[N]` + urban `[PU]`, with or without بـ: شو عم تعمل؟ / عم بشتغل على الـ migration. Rural `[PR]` and Jordanian use **قاعد**: قاعد بشتغل. [Wikt-am] [Hoyt10]
- **Subjunctive = bare verb, no أنْ.** After بدّ-، لازم، ممكن، بقدر، بحب، مفروض، صار، بلّش، ضلّ: بدها تشرب قهوة، لازم نعمل deploy، بلّشت أكتب. [LAG] [TLT-b]
- **Yes/no questions** have **no هل**; the statement itself is the question: جاهز الـ build؟ [WBq]

## 4. Demonstratives, question words, connectors

- **this / that / these** `[S]`: هاد(ا) m، هاي / هادي f، هدول pl; far: هداك، هديك. [LAG] [JordWiki]
- **هالـ** = "this/the" for something at hand, any gender or number: هالمشروع، هالشي. [LAG]
- **Question words**: شو (all) / إيش `[S]`، وين، ليش، كيف، مين، إيمتى، قدّيش، كم، أيّ / أنو `[S]`. [LAG] [PalWiki] [Wikt-anu]
  - ليه is Lebanese (some Palestinians borrow it); شلون is Syrian. Keep them out of a Palestinian text. [LAG]
- **that (complementizer)**: إنّه: بعرف إنه الـ API بطيء. Because: لإنه / عشان (with a subjunctive, عشان means "so that"). [Wikt-inno] [Wikt-ashan]
- **who/which (relative)**: اللي. [PalWiki]

## 5. Pronouns

أنا، إحنا `[S]` / نحنا `[N]`، إنتَ، إنتِ، إنتو، هو، هي، همّ `[S]` / هنّ `[N]`.

Suffixes: ـك (you m and f are written the same), ـكم `[S]` / ـكن `[N]`, ـه (pronounced -o) `[S]` / ـو `[N]`, ـها `[S]` / ـا `[N]`, ـهم `[S]` / ـهن `[N]`. [LAG] [PalWiki]

## 6. Spelling habits (informal written Levantine)

- **ق stays ق** in writing whatever the pronunciation (ʔ urban, g Gaza/Bedouin/Jordan, k central rural): قلت، قدّيش، طريق. Hamza spellings (ألت، طريء) exist in chat but look sloppy in published text. [Lingualism] [CODA] [LevWiki]
- **ج stays ج** (said ʒ in cities, dʒ in rural areas). [LevWiki]
- **ث / ذ**: urban speech says t/d (تاني، هدا) or s/z in MSA loans. Writers vary: common words often follow pronunciation (كتير، تاني), learned words keep the original letter. **Pick per word and stay consistent.** [Lingualism] [CODA]
- **"now"**: هلأ or هلق (both standard Levantine spellings); هسّا for Jordanian. One per text. [Wikt-halla] [PalWiki]
- **Plural verb ending**: write ـوا (بيعرفوا، يتأثروا), per CODA. [CODA]
- **لـ + الـ = للـ**, also before an English word: للـ feature، للـ users.
- **Final ة**: prefer ة (مدرسة، جديدة). ه also appears in chat; don't mix within one text. [CODA]
- **Lebanese imala** is sometimes written with final ي (طويلي). Don't carry that into Palestinian. [LevWiki]
- **No tanween, no short-vowel marks** in informal text; shadda optional (see SKILL.md). Frozen MSA adverbs (أبدا) are fine; write them without the tanween mark. [LAG]
- **Attach single-letter clitics** (بـ، حـ، لـ), and write رح as a separate word: رح أكتب، بالكود. [CODA]
- **Arabizi** (3 = ع، 7 = ح، 2 = ء/ق): don't use it unless the user writes in it. [AbuElhija12]

## 7. MSA leaks - kill on sight

| Leak (MSA) | Levantine | Note |
|---|---|---|
| سوف / سـ | رح | [Salameh18] |
| لم / لن / لا + verb | ما / ما رح | "all verbs are negated with ما" [TeamMaha7] |
| ليس | مش (Syr. مو) | [TeamMaha3] |
| لقد | drop it | [LevWiki] parallel text |
| إنّ at sentence start | drop it | [LevWiki] parallel text |
| أنْ + verb | bare verb: بدي أروح | [LAG] |
| هل | drop; question by intonation | [WBq] |
| الذي / التي / الذين | اللي | [PalWiki] |
| هذا / هذه | هاد / هاي | rural Jordanian هذا is native [JordWiki] |
| ماذا / لماذا / متى / أين | شو / ليش / إيمتى / وين | [PalWiki] |
| الآن | هلأ / هلق | [Zaidan14] |
| أيضاً | كمان | [Wikt-kaman] |
| جداً | كتير | [LAG] |
| يريد / أريد | بدو / بدي | [PalWiki] |
| يستطيع | بيقدر | [Wikt-qdr] |
| فقط | بس | [LAG] |
| لا يوجد | ما في | [TLT-neg] |
| شيء | إشي `[S]` / شي `[N]` | [PalWiki] |
| غداً | بكرة | [Wikt-bukra] |
| لأن | لإنه / عشان | [Wikt-inno] [Wikt-ashan] |
| جيد / جيداً | منيح (good / well, all Levantine) | [Wikt-mnih] |
| عندما | لمّا | [Wikt-lamma] |
| قام بـ + verbal noun | plain verb: قمنا بإطلاق -> أطلقنا | style rule, see SKILL.md |

Also watch **word order**: MSA leans verb-first (VSO); dialect text sounds natural subject-first or topic-first. [Zaidan14]

## 8. English tech terms

Code-switching into English is normal in Levantine professional speech, including for technical words that have Arabic equivalents. Don't "purify" it. [LevWiki] [JordWiki]

- **Keep in Latin script, inline:** product and framework names, commands, code identifiers, acronyms, and common dev nouns such as bug, PR, review, deploy, staging, production, feature, query, build, API.
- **Arabic article on an English noun:** write `الـ` + space + the Latin word: الـ API، الـ staging. Arabic clitics attaching to Latin-script words is attested. [Hamed25]
- **Verbs, choice 1: light verb عمل + English noun** for anything not already Arabized: عملت deploy، بعمل review، رح نعمل merge. Attested Jordanian pattern: عمل delete / download. [Smith25]
- **Verbs, choice 2: established Arabized verbs** (Form II / quadriliteral): سيّف (save)، شيّك (check)، شيّر (share)، بلّك (block)، كنسل (cancel). Attested in Jordanian and Lebanese speech (Arabic-script spellings are ours). [Smith25] [Beiruter]
- **Don't coin new Arabized verbs** (~~دبلويت~~، ~~ميرجت~~) or mix scripts inside a word (~~deployت~~). If it isn't on the list above, use عمل + English.
- **Don't translate a term the audience uses in English** into a formal coinage (~~طلب الدمج~~ for PR).

## 9. Worked rewrites (MSA -> urban Palestinian)

**1. Announcement** (سوف, لقد, أنْ)
- MSA: لقد قررنا أن ننقل المشروع من MySQL إلى PostgreSQL، وسوف نبدأ الأسبوع القادم.
- Pal: قررنا ننقل المشروع من MySQL لـ PostgreSQL، ورح نبلّش الأسبوع الجاي.
- Dropped لقد and أنْ; سوف became رح + subjunctive; نقل, not هجرة.

**2. Debugging** (negation)
- MSA: لا أعرف لماذا لا يعمل الـ build، فأنا لم أغيّر أي شيء.
- Pal: مش عارف ليش الـ build مش شغّال، أنا ما غيّرت إشي.
- مش on the participles (عارف، شغّال), ما on the verb. A rural or Jordanian voice would write ما بعرفش ليش...

**3. Team chat** (question words, هل, demonstrative)
- MSA: ماذا تريد أن تفعل الآن؟ هل نصلح هذا الخطأ قبل النشر؟
- Pal: شو بدك تعمل هلأ؟ نصلّح هاد الـ bug قبل الـ deploy؟
- هل dropped; the English noun stays English with الـ.

**4. Personal-brand post** (aspect, because, tech terms)
- MSA: أعمل حالياً على ميزة جديدة، وأختبرها على بيئة الـ staging لأنني لا أريد أي مفاجآت في الإنتاج.
- Pal: هلأ عم بشتغل على feature جديدة، وبجرّبها على الـ staging عشان ما بدي أي مفاجآت على الـ production.
- عم + بـ for "right now"; عشان for "because"; ما بدي, not لا أريد.

## 10. Voice profile: Palestinian developer (author's personal brand)

Use this profile when the user asks for "my voice", a LinkedIn or personal-brand post by a Palestinian dev, or this profile by name. It is the author's own voice spec, applied on top of sections 1-9.

- **Register:** Palestinian colloquial, professional but conversational, first person. It should sound like a dev talking to a colleague, not a press release.
- **Adapt, don't translate.** If there's an English version, rebuild the idea in Arabic; a word-for-word version "looks translated" and nobody reads it.
- **No tanween and no heavy diacritics.** Formal MSA plus tanween reads as machine translation.
- **English tech terms inline** (section 8): review، PR، bug، staging، deploy، query، code، feature، user.
- **Everyday words that set the tone:** بدي، مش، هيك، هلأ، عشان، لما، كتير، بس، في / ما في، زي.
- **Word choices (author preference, not dialect rules):**
  - **إنشاء, never توليد**, for making or creating something. توليد reads as machine output.
  - **نقل or تحويل المشروع, never الهجرة**, for moving a project or database (e.g. from MySQL to Postgres).
- **Punctuation:** no em dash or en dash. Use a plain hyphen or restructure the sentence.

## Feedback

**Found something wrong or missing?** Arabic dialects vary by city, generation, and family, and this guide will not match every speaker. Tell Majd: majd.ghithan20@gmail.com, or open an issue or PR at https://github.com/majdghithan/agent-skills.

## Sources

- [LAG] Levantine Arabic grammar - https://en.wikipedia.org/wiki/Levantine_Arabic_grammar
- [LevWiki] Levantine Arabic - https://en.wikipedia.org/wiki/Levantine_Arabic
- [PalWiki] Palestinian Arabic - https://en.wikipedia.org/wiki/Palestinian_Arabic
- [JordWiki] Jordanian Arabic - https://en.wikipedia.org/wiki/Jordanian_Arabic
- [WBneg] Wikibooks, Levantine Arabic/Negation - https://en.wikibooks.org/wiki/Levantine_Arabic/Negation
- [WBq] Wikibooks, Levantine Arabic/Questions - https://en.wikibooks.org/wiki/Levantine_Arabic/Questions
- [Hoyt10] Hoyt 2010, Negative Concord in Levantine Arabic (dissertation) - https://fmhoyt.colliertech.org/Hoyt_Dissertation.pdf
- [Obeidat22] Obeidat & Wardat 2022, JLLS - https://www.jlls.org/index.php/jlls/article/viewFile/3577/1551
- [TLT-neg] theLevanTongue, negation - https://thelevantongue.com/levantine-arabic/ma-mu-mesh-negation-words-levantine-arabic/
- [TLT-b] theLevanTongue, b-prefix - https://thelevantongue.com/levantine-arabic/b-prefix-verbs-levantine-arabic-simplified/
- [TeamMaha3] https://teammaha.com/2017/02/fusha-to-shami-3/ · [TeamMaha7] https://teammaha.com/2017/02/fusha-to-shami-7/
- [CODA] CAMeL CODA* orthography guidelines - https://camel-guidelines.readthedocs.io/en/latest/orthography/
- [Lingualism] Levantine Arabic orthography - https://resources.lingualism.com/levantine-arabic/levantine-arabic-orthography/
- [AbuElhija12] Abu Elhija 2012, Arabizi in Israel/Palestine - https://ejournals.bc.edu/index.php/levantine/article/download/2157/1799/0
- [Zaidan14] Zaidan & Callison-Burch 2014, Arabic Dialect Identification - https://aclanthology.org/J14-1006.pdf
- [Salameh18] Salameh et al. 2018, Fine-Grained Arabic Dialect Identification - https://aclanthology.org/C18-1113.pdf
- [Hamed25] Hamed et al. 2025, COLING - https://aclanthology.org/2025.coling-main.307.pdf
- [Smith25] Smith 2025, English loan verbs in Jordanian Arabic - https://www.emerald.com/insight/content/doi/10.1108/sjls-09-2024-0053/full/html
- [Beiruter] The Beiruter, Arabinglizi - https://www.thebeiruter.com/article/what-is-the-language-of-lebanon-inside-the-world-of-arabinglizi/1706
- Wiktionary: [Wikt-rah] https://en.wiktionary.org/wiki/رح · [Wikt-am] https://en.wiktionary.org/wiki/عم · [Wikt-inno] https://en.wiktionary.org/wiki/إنه · [Wikt-anu] https://en.wiktionary.org/wiki/أنو · [Wikt-halla] https://en.wiktionary.org/wiki/هلق · [Wikt-kaman] https://en.wiktionary.org/wiki/كمان · [Wikt-qdr] https://en.wiktionary.org/wiki/قدر · [Wikt-ashan] https://en.wiktionary.org/wiki/عشان · [Wikt-bukra] https://en.wiktionary.org/wiki/بكرة · [Wikt-mnih] https://en.wiktionary.org/wiki/منيح · [Wikt-lamma] https://en.wiktionary.org/wiki/لما
