# Passport School — new website (passportcharter.org)

Static rebuild of the school's site, exiting WordPress after the PHP2Shell incident (a pre-auth RCE in the PHP runtime itself — see `docs/wordpress-exit-options.md` §1). **Decided 2026-11-14:** Astro + Sveltia CMS on Cloudflare Pages; school-owned accounts; flexible timeline.

Full analysis, migration plan, and custody checklist: [`docs/wordpress-exit-options.md`](docs/wordpress-exit-options.md)

## Stack
- **Astro** — static site generator. No PHP, no database, no server-side execution anywhere.
- **Sveltia CMS** — staff editing UI at `/admin/` (config: `public/admin/config.yml`; content model: `src/content.config.ts`).
- **Cloudflare Pages** — hosting (free tier). **Cloudflare Registrar** — domain, at-cost.
- Content collections: `news`, `events`, `staff`, `settings` (countdown date, announcement, Instagram URL).

## Status
- [x] Recon, options analysis, decision (2026-11-14)
- [x] **Phase 1 — Content export (done 2026-11-14):** full export pulled to `data/export/passport-export/` (gitignored: DB dump 4.2 MB gz, Elementor `_elementor_data` trees per page, menus, media manifest, plugins/themes/users, uploads archive — 2,204 files / 202 MB). Uploads hygiene check passed: only 2 PHP files found, both benign plugin directory-protect stubs (WPForms 404 stub + empty template-kit index). **Server finding:** Lightsail runs PHP 8.2.23 (built Sept 2024) via php-fpm + mpm_event — the build predates the PHP2Shell disclosure/fixes; patch or accelerate decommission.
- [x] **Phase 2 — Design refresh (COMPLETE 2026-11-14, finish review: SHIP):** canon at modern district-site craft (owner's explicit choice): maroon/Barlow/warm-white system, real-photo hero, grouped nav (Parents/Students/School), all 24 URLs preserved (`/parents-2/` + `/students-2/` hubs true-301→`/parents/`,`/students/`; school calendar at its legacy `/parents-2/school-calendar/`), 21 staff with photos + emails in the CMS, events + settings collections live, forms built (Formspree endpoints deferred to cutover). Two-round independent finish review: 4 material defects found → fixed → verdict pass scored all resolved (ship). Verification: 877 internal links/0 broken, contrast 7.5–17.2:1, UTC-pinned dates, white focus rings on maroon surfaces, no overflow at 1440/390px
- [x] **Phase 3 — staging COMPLETE (2026-11-14):** school-owned Cloudflare (`web@`) + GitHub (`passportschool`); repo **github.com/passportschool/website**; staging auto-builds on Cloudflare Workers (Git-connected Workers Builds + static assets) at **passportschool.web-f67.workers.dev** — all routes 200, legacy 301s preserved; CMS auth via Sveltia CMS Authenticator worker (`sveltia-cms-auth.web-f67.workers.dev`) + a GitHub App installed on the repo (Contents r/w); **editing loop verified end-to-end**: Sveltia edit → GPG-verified commit to `main` → auto-build → live (~40 s), zero deploy steps. CMS exposes News / Events / Faculty & Staff / Site Settings / Pages (URL + dates locked as hidden fields).
- [ ] **Phase 3 — production cutover: BLOCKED on Hover access** (school must identify who holds the account; domain actively renewed, expires 2029). Then: Cloudflare zone with the full audited record set (`docs/cutover-plan.md`), MX-preserving nameserver flip, custom domain on the Worker, Formspree endpoints for both forms, Lightsail decommission.
- [ ] Phase 4 — WCAG 2.1 AA audit (axe/WAVE) + launch
- [ ] Phase 5 — Staff runbook + MSP handoff pack

## Local development
```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
```

## Staff editing (after launch)
Go to `/admin/`, log in with the school's GitHub account. News, Events, Faculty & Staff, and Site Settings are all form-based — no code involved.
