# Passport School — WordPress Exit & Rebuild Options

**Prepared:** November 14, 2026 · **By:** Spencer (outgoing MSP), compiled with Hermes Agent · **For:** school leadership + incoming MSP
**Status:** DECIDED 2026-11-14 — **Option A** (Astro + Sveltia CMS on Cloudflare Pages), **school-owned accounts**, flexible timeline (optimize for quality), SSH used for content export only. Facts about the current site were verified against the live site, DNS, and registry today.

---

## 1. Why we're rebuilding

The site was hit in the **PHP2Shell incident**. PHP2Shell is not a WordPress or plugin flaw — it is a pair of pre-authentication remote-code-execution vulnerabilities **in PHP itself** (CVE-2026-109618 / CVE-2026-109619, CVSS v4.0 9.2). Every unpatched PHP installation serving web requests is at risk, Apache/mod_php configurations most of all; on mod_php the flaw fires before any application code runs, so CMS updates and plugin hygiene do not change exposure.[1] Mass exploitation has been underway since October 2026 — WordPress stacks have mostly held so far, but a successful attack hands over the site's files, database, and passwords, and successful intrusions follow the classic pattern: reverse shell, webshell persistence, tooling, privilege escalation.[2]

**Implication:** the durable fix is not "a cleaner WordPress." It is removing internet-exposed PHP from the school's web stack entirely. Both options recommended below do that by architecture, not by patching discipline.

The rebuild is also the natural moment to fix custody: the site (AWS Lightsail), the domain (Hover), and related accounts currently live on the outgoing MSP's personal accounts. The rebuild moves everything to school-owned accounts the new MSP can administer.

## 2. Current state (verified 2026-11-14)

| What | Found |
|--|--|
| Stack | WordPress 7.1.4 · Elementor 4.3.5 + Elementor Pro 4.3.3 · Hello Elementor theme · ~10 Elementor add-on plugins (Happy Addons, TM Elementor, card-elements-pro, item-lists-pro, teamcard, tfteam) · Smash Balloon Instagram Feed 6.15.0 + Reviews Feed |
| Content | 24 pages (Appendix A) · no blog posts — "Latest News" and events are hand-edited on the homepage · homepage HTML is 217 KB (Elementor bloat) |
| Hosting | AWS Lightsail, Apache |
| Domain | passportcharter.org · registrar Tucows (Hover) · registered 1998 · **expires 2029-06-10** · transfer-locked (normal) |
| Email | **Microsoft 365** via Hover DNS (MX = `passportcharter-org.mail.protection.outlook.com`) — these records must move intact through any DNS change |

Security observations on the live site (verified 2026-11-14, including via SSH):

- REST API exposes the admin username (`/wp-json/wp/v2/users` → login `user`); the users sitemap exposes the author archive.
- `readme.html` is world-readable (version disclosure). `xmlrpc.php` is blocked (good). `wp-login.php` is open (normal, but rate-limit it).
- **The Lightsail origin runs PHP 8.2.23 (built Sept 2024) via php-fpm + mpm_event.** That build predates the PHP2Shell disclosure and its fixes by two years — whatever post-incident remediation occurred, the vulnerable-era runtime remained in place as of export day. Patch the stack or accelerate decommission; do not treat the box as clean.
- Uploads directory checked during export: no webshell or suspicious PHP in `wp-content/uploads` (only benign WPForms/template-kit `index.php` stubs).

## 3. Requirements

1. CMS editable by school staff (front office), no developer involved in day-to-day edits.
2. Least expensive option that still meets the security and design bar.
3. A real design refresh (currently: generic Elementor template look).
4. Clean custody handoff: school-owned accounts, incoming MSP has admin, outgoing MSP fully off the critical path.
5. Keep: domain, URL paths (parents' and OCPS bookmarks), M365 mail, Instagram presence, FortifyFL link, calendar, news/events.

## 4. Options compared (prices verified Nov 14, 2026)

### Option A — Static site (Astro) + Sveltia CMS on Cloudflare Pages — **RECOMMENDED**

A hand-built static site with a custom design refresh. Sveltia CMS — the maintained, feature-complete successor to Netlify/Decap CMS — gives staff a clean web editor (forms, media library, preview); every save is a version-controlled Git commit.[11][12] Cloudflare Pages hosts it on the free tier: 500 builds/month, unlimited bandwidth, 20,000 files.[18]

- **Cost: ≈ $11/yr.** Hosting $0 · domain at Cloudflare Registrar at-cost with zero markup (≈ $10–12/yr for .org)[19] · forms via Formspree free tier (50 submissions/mo; over-limit submissions are queued, not lost)[21].
- **Security:** no PHP, no database, no server-side execution anywhere. The PHP2Shell class of attack is eliminated by architecture. Worst-case CMS credential abuse = edited content, not a server shell — and every change is an auditable commit.
- **Staff UX:** bookmark `/admin/` → form-based editing with image upload; publish in ~30–60 s. One-time setup per editor: free GitHub account + invite to the school org (10-minute runbook), or one shared school editor login in the school's password manager.
- **Handoff:** the new MSP inherits a normal Git repo and a Cloudflare dashboard — standard tooling, nothing exotic.
- **Design:** fully custom — the refresh can be exactly what the school wants.
- **Honest caveats:** Sveltia is pre-1.0 but production-proven and actively maintained.[11][12] Staff logins are GitHub-based (one-time friction). The Instagram feed becomes a curated grid the office updates with photos (Smash Balloon already cached all the images locally, so nothing is lost) or official per-post embeds.

### Option B — Squarespace (Basic plan) — runner-up

- **Cost:** $19/mo billed annually ≈ **$228/yr** ($25/mo monthly billing); first-year domain registration included on annual plans.[4][5] JavaScript embeds (countdown timers, some third-party widgets) require the Core plan at $29/mo annual ≈ $348/yr.[4][6]
- **Security:** SaaS — no servers to patch, that's the vendor's job. Same architectural win as A, minus self-management.
- **Staff UX:** best-in-class drag-and-drop; plain email logins.
- **Instagram:** a native Instagram block exists but requires an Instagram *professional* account and periodic manual reconnection (Meta retired the old Basic Display API in Dec 2024); it shows up to 20 recent posts and has a documented habit of silently disconnecting.[7][8]
- **Design:** excellent templates, but template-shaped — a refresh, not a custom design.
- Note: Squarespace renamed its plans in Oct 2026 (Basic/Core/Plus/Advanced); older articles referencing Personal/Business plans are stale.

### Other credible options — and why they lose here

- **Wix Light** — $17/mo annual ≈ $204/yr with a free first-year domain, but the Light plan caps at 2 site collaborators and 2 GB storage, and the design ceiling is weaker for a school.[9][10]
- **Ghost(Pro)** — Starter is $15/mo billed yearly ($180/yr) but allows a single staff user; more editors need Publisher at $29/mo ($348/yr). Superb for news/newsletter-driven orgs, but page-structured school sites are second-class.[14][15]
- **TinaCMS instead of Sveltia (variant of A)** — friendlier live visual editing; the free tier covers 2 users/3 roles, then $29/mo per project. Only if the office dislikes Sveltia's UI after trying it.[13]
- **School-specific CMS (Edlio, Apptegy, Finalsite)** — purpose-built K-12: accessibility tooling, teacher pages, branded apps, messaging, payments, unlimited staff support; annual subscription, **pricing on request** (budget low-thousands per year and up — our estimate, not a quote).[16][17] Right choice if the board wants a vendor contract and integrated parent communications; not "least expensive."
- **Managed WordPress / WordPress.com** — rejected: the requirement is *off WordPress*, and self-hosted WP keeps the §1 runtime exposure.
- **Google Sites** — free and staff-friendly, but cannot deliver a credible design refresh.

## 5. Cost summary (first 12 months)

| Option | Recurring | Year-1 total | Who supports it |
|--|--|--|--|
| **A. Astro + Sveltia + Cloudflare** | ~$11 (domain at cost) | **~$11** | Any MSP with Git basics; school owns accounts |
| B. Squarespace Basic | $228 | ~$228 | Vendor + any admin |
| B′. Squarespace Core (JS embeds) | $348 | ~$348 | Vendor + any admin |
| C. Wix Light | $204 | ~$204 | Vendor + any admin |
| D. Ghost(Pro) Starter / Publisher | $180 / $348 | — | Vendor |
| E. Edlio-class (quote) | ~$2k+ (est.) | — | Vendor |
| Status quo: WP on Lightsail | ~$60–120/yr VPS + patching labor + standing PHP exposure | — | MSP only |

Build labor is $0 either way — the outgoing MSP is donating the rebuild before handoff. Option A's remaining cost is *time*: it needs the design phase done right (~1–2 weeks of calendar time alongside normal work).

## 6. Recommendation

**Option A** — it is simultaneously the cheapest and the most secure, it's the only one that allows a genuinely custom design refresh, and it produces the cleanest custody story (school-owned GitHub org + Cloudflare account; both MSPs get delegated access; nobody's personal accounts are load-bearing). Its only real trade-off is the one-time GitHub login setup for staff.

Choose **B** instead if the school values "never think about the website" and vendor phone support over ~$217/yr and custom design. Choose **E** if the board later funds a K-12 communications platform.

## 7. Migration plan

**Phase 0 — Interim hardening (days; old site stays live while we build)**
1. Patch PHP to a fixed build for its branch (public research verified 8.5.11 vulnerable / 8.5.12 fixed on the affected line) and confirm Apache's SAPI mode — mod_php is the highest-risk configuration.[1][3]
2. Rotate every credential: DB, WP salts/keys, SMTP, Instagram token, Hover, AWS.
3. Disable REST user enumeration + the users sitemap; delete `readme.html`; rate-limit `wp-login.php`.
4. Optionally put Cloudflare (free) in front of the origin — WAF, hides the origin IP, and pre-stages the cutover. Recreate the DNS zone carefully around the live M365 MX records.
5. Snapshot for records.

**Phase 1 — Content export (needs Lightsail SSH)**
`wp db export`, rsync `wp-content/uploads`, `wp plugin list`; convert the 24 pages to markdown collections; re-encode all media through the new image pipeline (re-encoding destroys any payload bytes, and a static host serves bytes only — there is no uploads-directory code-execution path to re-exploit).

**Phase 2 — Build & design refresh**
Astro site; collections for news/events/pages/staff/settings; Google Calendar embed for the calendar (staff already live in Google); Formspree for any forms (50/mo free)[21]; Instagram as a CMS-curated photo grid; FortifyFL link and the countdown preserved (countdown target becomes a CMS setting); **preserve all existing URL paths** so no bookmark or OCPS link breaks.

**Phase 3 — Custody & cutover**
1. Create school-owned Cloudflare account (DNS first, then Registrar) and school-owned GitHub org; invite both MSPs.
2. Unlock + transfer the domain from Hover/Tucows to Cloudflare Registrar (at-cost; transfer adds a year; **do not transfer within 45 days of a renewal** — that year is lost; ours renews June 2029 so no issue).[19][20]
3. Recreate the DNS zone with the M365 MX records intact; lower TTLs before cutover; flip A/CNAME to the new host.
4. Final Lightsail snapshot for the school's archive, then decommission the instance.

**Phase 4 — Compliance & launch**
Passport School is a public entity under ADA Title II. DOJ's web rule requires web content to conform to **WCAG 2.1 Level AA**; after the April 2026 interim final rule, deadlines are April 26, 2027 (entities serving ≥50,000 population) and April 26, 2028 (smaller entities and special districts).[22][23][24] There is no exception for school course-content links, and charter schools are frequent OCR complaint targets — build born-accessible and run axe/WAVE audits before launch (A and B can both reach AA; A just requires disciplined building).

**Phase 5 — Handoff pack**
Accounts inventory (registrar, DNS, hosting, CMS, forms, analytics, socials), staff runbooks (post news / add event / add photo / change countdown), break-glass credentials in the school's password manager, uptime monitoring, and this document.

## Appendix A — Current page inventory (24 pages, via REST + sitemap)

| Path | Title | Last updated |
|--|--|--|
| `/` | Home Page | 2024-12-17 |
| `/about-us/` | "Contact Us" *(content bug — nav says About Us, page title says Contact Us)* | 2024-11-07 |
| `/board-info/` | Board Info | 2024-11-07 |
| `/parents/`, `/students/` | Parents / Students hubs | 2024-11-07 |
| `/smsoptin/` | Parent SMS Signup | 2025-03-04 |
| `/privacy-policy/`, `/terms-conditions/` | Privacy / Terms | 2025-02-10 |
| `/faculty-and-staff/` | Faculty and Staff | 2019-08-19 |
| `/extended-day-program/` | Extended Day Program | 2019-08-21 |
| `/additions-and-volunteering/` | ADDitions and Volunteering | 2019-08-21 |
| `/parents-2/` + 5 subpages | Committees, Emergency Procedures, Enrollment Information, School Calendar, Title I Information | 2019-08-19 |
| `/students-2/` + 6 subpages | Grading Scale, Helpful Websites, Report Suspicious Activity, School News and Information, Student Policies, Supplies List by Grade | 2019-08-19 |

## Appendix B — Domain & mail facts for the handoff

- Registered 1998 · expires **2029-06-10** · registrar Tucows (Hover) · NS `ns1/ns2.hover.com` · status: clientTransferProhibited + clientUpdateProhibited (normal locks; unlock at Hover before transfer).
- MX: `passportcharter-org.mail.protection.outlook.com` (Microsoft 365) — **verify mail flow immediately after any DNS change.**
- Homepage currently 217 KB HTML; the rebuilt static homepage should land well under 50 KB.

## Sources

[1] https://www.bitdefender.com/en-us/blog/businessinsights/technical-advisory-php2shell-pre-auth-rce — Bitdefender advisory: PHP2Shell pre-auth RCE CVE-2026-109618/109619
[2] https://www.securityweek.com/php2shell-attacks-root-palo-alto-firewalls-but-fail-against-wordpress — SecurityWeek: PHP2Shell exploitation status vs WordPress
[3] https://github.com/FranklinF25/php2shell/blob/main/docs/finding-sheet.md — php2shell finding sheet: PHP 8.5.11 vulnerable vs 8.5.12 fixed
[4] https://www.squarespace.com/pricing — Squarespace pricing page (Basic/Core/Plus/Advanced)
[5] https://www.squarespace.com/assets/pricing.txt — Squarespace plan details incl free domain on annual
[6] https://vitraz.io/integrations/squarespace — Squarespace plan requirements for JavaScript code blocks
[7] https://support.squarespace.com/hc/en-us/articles/206543367-Instagram-blocks — Squarespace Instagram blocks help
[8] https://www.jotform.com/blog/how-to-add-social-media-feed-to-squarespace — Squarespace IG block behavior Aug 2026
[9] https://www.wix.com/plans — Wix plans page
[10] https://www.wix.com/blog/how-much-is-a-wix-website — Wix pricing explainer Nov 2026
[11] https://sveltiacms.app/en — Sveltia CMS: successor to Netlify/Decap CMS
[12] https://github.com/sveltia/sveltia-cms — Sveltia CMS repository
[13] https://tina.io/pricing — TinaCMS pricing (free tier 2 users)
[14] https://ghost.org/pricing — Ghost(Pro) pricing
[15] https://docs.ghost.org/hosting — Ghost hosting comparison
[16] https://www.edlio.com/apps/pages/websites — Edlio school websites product page
[17] https://www.itechguides.com/products/edlio — Edlio review: pricing on request
[18] https://developers.cloudflare.com/pages/platform/limits — Cloudflare Pages free plan limits
[19] https://www.cloudflare.com/domains — Cloudflare Registrar at-cost domains
[20] https://developers.cloudflare.com/registrar/faq — Cloudflare Registrar FAQ: transfer rules
[21] https://help.formspree.io/articles/account-management/account-limits — Formspree account limits (50/mo free)
[22] https://www.ada.gov/assets/pdfs/web-rule.pdf — DOJ ADA Title II web accessibility rule
[23] https://www.ada.gov/resources/web-rule-first-steps — DOJ first steps: extended compliance deadlines
[24] https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web — Federal Register 2026 IFR: deadline extension
