# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Astro static site + Sveltia CMS (staff editing), deployed on Cloudflare Pages. Existing codebase in this repo.

## Users

Primary: current parents, mostly on phones, checking news, events, calendar, forms, and policies. Secondary: prospective families evaluating enrollment; students and staff using resource pages; the front office (Mrs. Vargas) publishing news and events.

## Product Purpose

The public website of Passport School, Inc. — an inclusive K-8 charter school in Orlando, Florida (OCPS's first charter school). The school's front door: mission, enrollment information, parent/student resources, news and events, staff directory, and compliance pages (Title I, governing board, FortifyFL).

## Positioning

Inclusive education: children with disabilities educated alongside their non-disabled peers; low student-teacher ratios, cooperative learning, multi-sensory hands-on learning; a small school where the front office knows every family.

## Operating Context

After cutover, staff edit news/events/staff/site-settings through Sveltia CMS at /admin (GitHub-backed). The school calendar is driven by the events collection (and, at cutover, a Google Calendar embed). Forms post via Formspree. Mail runs on Microsoft 365 — MX records must be preserved through any DNS change. Domain expires 2029-06-10 at Hover/Tucows.

## Capabilities and Constraints

Static build only — no server-side code by design (the WordPress exit after the PHP2Shell runtime RCE). Must meet WCAG 2.1 Level AA (DOJ ADA Title II web rule). Every existing URL path must be preserved (parents' and OCPS bookmarks). Instagram presence is @passportpanthers.

## Brand Commitments

Name: Passport School (the "Passport Panthers"). Existing logo (`data/export/passport-export/uploads/2024/12/logo.png`), brand maroon `#590304` (dominant color across the entire site's data), Barlow typeface, real school photography.

STANDING PREFERENCE (decided 2026-11-14): **conventional modern district-site design** — the Apptegy/Edlio-class register with big clear type, clean card grids, real photo hero, generous whitespace, high accessibility. Chosen deliberately over thematic/art-directed worlds; no gimmicks, no smuggled quirk.

## Evidence on Hand

Full WordPress export in `data/export/passport-export/` (gitignored): 24 pages of Elementor content trees, media manifest (200 attachments), 2,204 upload files (202 MB), menus, users, DB dump. Mission and philosophy text verified. 18 real staff members with photos and roles. Real upcoming events. No invented claims, staff, or events — nothing may be fabricated.

## Product Principles

1. A parent finds today's answer (news, event, form, policy) in under a minute.
2. Accessibility is a requirement, not a feature — the school's mission is inclusion; the site must practice it.
3. The site must be safe to hand off: standard tooling, documented, school-owned accounts.
4. Real content only.

## Accessibility & Inclusion

WCAG 2.1 Level AA is mandatory (ADA Title II entity). The audience explicitly includes children with disabilities and their families.
