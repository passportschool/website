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
- [x] **Phase 2 — Design refresh (built 2026-11-14, finish review + DESIGN.md pending):** canon at modern district-site craft (owner's explicit choice): maroon/Barlow/warm-white system, real-photo hero, grouped nav (Parents/Students/School), all 24 URLs preserved (`/parents-2/` + `/students-2/` hubs 301→`/parents/`,`/students/`), 21 staff with photos + emails in the CMS, events + settings collections live, forms built with Formspree endpoints deferred to cutover. Verified: no horizontal overflow at 1440/390px, 0 broken images, contrast 7.5–17.2:1, burger/countdown/redirects functional
- [ ] Phase 3 — School-owned Cloudflare account + GitHub org (update `backend.repo` in `public/admin/config.yml`), deploy, cutover. **Preserve the M365 MX records** (`passportcharter-org.mail.protection.outlook.com`) through any DNS change. Domain transfer note: not within 45 days of a renewal (renews June 2029)
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
