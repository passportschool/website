# Cutover Plan — Phase 3

**Goal:** move passportcharter.org to school-owned Cloudflare hosting with zero mail disruption, independent of any Git-host decision.

## The live DNS zone (audited 2026-11-14 via dns.google)

These records **must exist in the Cloudflare zone before the nameserver flip** — replicate verbatim, then review individually later (zero-change principle):

| Type | Name | Value | Notes |
|--|--|--|--|
| A | `@` | `98.84.249.20` | Lightsail origin — points at Cloudflare Pages at cutover |
| A | `www` | `98.84.249.20` | Same |
| MX | `@` | `0 passportcharter-org.mail.protection.outlook.com` | **M365 mail — critical** |
| TXT | `@` | `v=spf1 include:spf.protection.outlook.com -all` | SPF |
| TXT | `@` | `MS=ms38446657` | M365 tenant verification |
| TXT | `@` | `google-site-verification=PemkKAEZLsh9TgtLnFG_Kqs4A5v3RBkX-ZVlcUOL9QY` | Google (Search Console/Workspace) |
| TXT | `@` | `apple-domain-verification=8qzIqTZivzOeCMfy` | Apple |
| TXT | `@` | `brevo-code:75797b7644210b22d27a3bada5a09b19` | Brevo (email marketing) |
| TXT | `@` | `logmein-verification-code=9fa92081-1211-42ec-8659-a9f03f689d20` | ⚠️ **Legacy vendor token (LogMeIn remote access). Replicate now; review for removal with the school after cutover — it authorizes a third-party remote-access vendor against the domain.** |
| TXT | `_dmarc` | `v=DMARC1; p=quarantine; rua=mailto:mrspiegler@passportcharter.org; ruf=mailto:mrspiegler@passportcharter.org` | DMARC — reports go to mrspiegler@ (note for the school) |
| CNAME | `autodiscover` | `autodiscover.outlook.com` | M365 Outlook autodiscover |
| CNAME | `selector1._domainkey` | `selector1-passportcharter-org._domainkey.thepassportschoolinc.onmicrosoft.com` | M365 DKIM |
| CNAME | `selector2._domainkey` | `selector2-passportcharter-org._domainkey.thepassportschoolinc.onmicrosoft.com` | M365 DKIM |
| CNAME | `enterpriseregistration` | `enterpriseregistration.windows.net` | Entra ID device join |
| SRV | `_sip._tls` | `10 1 443 sipdir.online.lync.com` | Teams/Skype |

No AAAA records exist. Current nameservers: `ns1.hover.com`, `ns2.hover.com` (Hover/Tucows). Proxy status at import: **DNS-only (grey cloud) for everything** until the site cutover step, then proxy the website records only.

## Sequence (each step small and reversible)

1. **Cloudflare zone** (school account, web@passportcharter.org): Add site → Free plan → enter the records above → Cloudflare shows two assigned nameservers (e.g. `*.ns.cloudflare.com`).
2. **Nameserver flip at Hover**: replace `ns1/ns2.hover.com` with the two Cloudflare nameservers. *Before flipping*, set TTLs at Hover to minimum (they're 300–900 already). **Verify immediately after:** `MX` + SPF + DKIM + DMARC resolve via dns.google, and send a test email to/from an M365 mailbox (e.g. office@).
3. **Create the Pages project** (`passport-school`) and deploy the current build by **direct upload**: `npx wrangler pages deploy dist/` — no Git needed. Smoke-test on the `*.pages.dev` URL (all 23 routes, a link click-through, the countdown, a form).
4. **Git host for the CMS** (independent branch, does not block launch):
   - Preferred: appeal the GitHub flag (https://support.github.com/contact — the account owner files it; typically cleared in hours–days). Then create the **school-owned** org — owner should be a school-controlled account, not the MSP's personal account — push the repo, connect Pages to it (direct upload becomes the fallback), set `backend.repo` in `public/admin/config.yml`, done.
   - Alternative: GitLab (Sveltia supports `backend: name: gitlab`; Pages integrates) — config swap is one line.
5. **Site cutover** (maintenance-free, any low-traffic hour): at Cloudflare, change `@` and `www` A records → CNAME to the Pages project (apex via CNAME flattening), **proxy ON (orange cloud)** for both. Verify site + old URLs (spot-check `/parents-2/school-calendar/`, a 301, a deep article). Lightsail stays up as instant rollback for 2 weeks.
6. **Forms**: create two Formspree endpoints (free tier, 50 submissions/mo): contact form → `office@passportcharter.org`; SMS opt-in → front office. Set the two `action` URLs (marked `TODO` in `src/pages/about-us.astro` and `src/pages/smsoptin.astro`), rebuild, redeploy.
7. **Decommission**: final Lightsail snapshot for the school's records → keep 30 days → delete instance. Remove the LogMeIn TXT if the school confirms. Consider moving the school's other M365 admin contacts into the handoff pack.
8. **Domain transfer to Cloudflare Registrar** (optional, saves Hover renewal cost): unlock at Hover + EPP code; transfer adds a year at cost. **Not within 45 days of a renewal** (renews June 2029 — no conflict).

## Rollback at any point
- After NS flip, mail issue → point Hover nameservers back (keep the Hover zone records untouched until step 7).
- After site cutover, site issue → flip the two A records back to `98.84.249.20` (Lightsail untouched).

## Staff CMS wiring (when Git host lands)
1. Org: school-owned. Members: outgoing MSP + incoming MSP (admin), office staff (write access via Sveltia login only).
2. Set `backend.repo` in `public/admin/config.yml`, redeploy.
3. Each editor: creates a free account on the Git host (one-time, 10-minute runbook), gets invited, logs in at `passportcharter.org/admin/`.
