---
name: Passport School
description: The canon modern district-site system for passportcharter.org — warm white ground, brand maroon, Barlow, standard components at high polish.
colors:
  maroon: "#590304"
  maroon-deep: "#3f0203"
  maroon-wash: "#f7ecec"
  ink: "#241b1d"
  ink-soft: "#5d5254"
  paper: "#ffffff"
  surface: "#f7f5f3"
  line: "#e7e1de"
  focus: "#590304"
  input-border: "#cfc7c3"
  input-border-hover: "#b9aeaa"
typography:
  display:
    fontFamily: "Barlow, 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "clamp(2rem, 1.5rem + 2.2vw, 2.9rem)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Barlow, 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.45rem, 1.2rem + 1.2vw, 1.9rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Barlow, 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "Barlow, 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Barlow, 'Segoe UI', system-ui, -apple-system, sans-serif"
    fontSize: "0.72rem"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.06em"
rounded:
  radius: "10px"
  radius-sm: "6px"
spacing:
  container-inline: "1.25rem"
  grid-gap: "1.25rem"
  card-pad: "1.4rem"
  section-block: "clamp(2.75rem, 4rem + 2.5vw, 4.5rem)"
  section-tight-block: "clamp(2rem, 2.5rem + 1.5vw, 3.25rem)"
  band-block: "clamp(2rem, 4vw, 3rem)"
components:
  button-primary:
    backgroundColor: "{colors.maroon}"
    textColor: "{colors.paper}"
    rounded: "{rounded.radius-sm}"
    padding: "0.72rem 1.35rem"
  button-primary-hover:
    backgroundColor: "{colors.maroon-deep}"
    textColor: "{colors.paper}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.maroon}"
    rounded: "{rounded.radius-sm}"
    padding: "0.72rem 1.35rem"
  button-outline-hover:
    backgroundColor: "{colors.maroon-wash}"
    textColor: "{colors.maroon-deep}"
  button-light:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.maroon}"
    rounded: "{rounded.radius-sm}"
    padding: "0.72rem 1.35rem"
  button-light-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.maroon-deep}"
  button-ghost-light:
    backgroundColor: "rgba(255,255,255,0.08)"
    textColor: "#ffffff"
    rounded: "{rounded.radius-sm}"
    padding: "0.72rem 1.35rem"
  button-ghost-light-hover:
    backgroundColor: "rgba(255,255,255,0.18)"
    textColor: "#ffffff"
  card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.radius}"
    padding: "1.4rem"
  input:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.radius-sm}"
    padding: "0.65rem 0.8rem"
  date-chip:
    backgroundColor: "{colors.maroon}"
    textColor: "{colors.paper}"
    rounded: "{rounded.radius-sm}"
    padding: "0.35rem 0.25rem"
    width: "3.4rem"
  form-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.radius}"
    padding: "clamp(1.5rem, 3vw, 2.25rem)"
  page-band:
    backgroundColor: "{colors.maroon}"
    textColor: "{colors.paper}"
  site-footer:
    backgroundColor: "{colors.maroon-deep}"
    textColor: "rgba(255,255,255,0.85)"
---

# Design System: Passport School

## Overview

**Creative North Star: "The Trusted Front Door"**

Passport School's site is the canon modern district site at full fidelity: the Apptegy/Edlio-class register the owner chose deliberately on 2026-11-14 over thematic or art-directed worlds. A parent lands on a real photograph of the school, reads the mission in plain sight, and reaches news, events, enrollment, or the parent hub in one scroll and zero thought. Credibility comes from type scale, spacing discipline, and real photography — not from decoration. The site is the school's front door, and the front office knows every family: the design's job is to feel that reliable.

The system is one warm world with one voice. A deep oxblood maroon carries every structural and active moment — utility bar, page bands, buttons, links, date chips, the footer — while everything else sits on warm whites (pure paper alternating with a warm-tinted surface) and warm near-black ink. Barlow does all the talking in four weights, large and plain, with tight tracking on display sizes and uppercase reserved for tiny tracked labels. Cards, chips, and photos all round to the same two radii, so every page reads as the same hand.

Accessibility is a load-bearing wall, not a feature: WCAG 2.1 AA (the school's mission is inclusion; the site must practice it), measured text contrast of 7.5–17.2:1 across the system's pairs, a skip link, white focus indicators on every dark band, and motion that collapses under `prefers-reduced-motion`. Confirmed visual rejections: thematic art direction, template noise, second hues, decorative illustration, stock photography.

**Key Characteristics:**

- Warm white ground (paper `#ffffff` alternating with surface `#f7f5f3`) with warm ink text (`#241b1d`)
- A single brand hue — deep maroon `#590304` — spent on structure and action, never on large content areas
- Barlow only (weights 400/500/600/700), big clear type, negative tracking on display sizes, uppercase only on micro-labels
- Two radii (10px containers, 6px controls), two shadows (resting `shadow-sm`, hover `shadow-md`), hairline borders (`#e7e1de`)
- Real school photography through the astro:assets pipeline; standard components (utility bar, grouped nav, hero, card grids, fat footer) at high polish
- WCAG 2.1 AA throughout: 3px maroon focus rings that flip to white on dark bands, tabular numerals in the countdown, 68ch reading measure
- One system across all 24 pages: maroon page band → alternating sections → deep-maroon 4-column footer

## Colors

A warm near-monochrome ground carrying a single deep oxblood maroon that does all the brand work.

### Primary

- **Passport Maroon** (`#590304`, the `--maroon` token): The only hue on the site. Carries the utility bar, page-title bands, primary buttons, the Enrollment CTA, text links, event date chips, the countdown band, staff-role lines, required-field asterisks, selection background, and the focus ring (`--focus` is the same value, held as its own token so focus can diverge). It never tints large content areas.
- **Deepened Maroon** (`#3f0203`, `--maroon-deep`): The maroon's darkened resting place — the footer background and the hover color for primary buttons and text links.
- **Maroon Wash** (`#f7ecec`, `--maroon-wash`): The maroon's palest tint — announcement strip background, outline-button and dropdown-link hover fill, and the initials fallback tile on staff cards.

### Neutral

- **Warm Ink** (`#241b1d`, `--ink`): Body and heading text — a near-black with a red-brown cast that keeps the ground warm.
- **Soft Ink** (`#5d5254`, `--ink-soft`): Secondary text — card paragraphs, event details, section intros, "Last updated" lines, form notes.
- **Paper White** (`#ffffff`, `--paper`): The primary ground — page background, header, cards, form card.
- **Warm Surface** (`#f7f5f3`, `--surface`): The alternating band ground — alternate content sections sit on this warm off-white instead of a border.
- **Hairline** (`#e7e1de`, `--line`): Every 1px border and divider — header bottom, card edges, event-row separators, map frame, empty state.
- **Field Border** (`#cfc7c3`, `--input-border`; hover `#b9aeaa`): Input and textarea borders run slightly darker than hairline so fields read as fillable.

On maroon and deep-maroon surfaces, text is white with opacity steps rather than new colors: `rgba(255,255,255,0.92)` utility-bar links (→ `#fff` on hover), `0.85` footer links and page-band intros (→ `#fff` on hover), `0.8`/`0.75` secondary countdown text. The hero scrim is the maroon family darkened: `linear-gradient(to top, rgba(42,4,5,0.82) 0%, rgba(42,4,5,0.25) 55%, rgba(42,4,5,0.12) 100%)`.

### Named Rules

**The One Hue Rule.** Maroon is the only hue on any screen. If a color can't be named "maroon," "warm white," or "warm ink," it doesn't belong on the site.

**The White Focus Rule.** Every focus indicator on a maroon or deep-maroon surface (utility bar, page band, countdown, footer, hero) flips to white (`outline-color: #fff`) so it stays visible on the dark ground — WCAG 2.4.7.

## Typography

**Display Font:** Barlow (with `'Segoe UI', system-ui, -apple-system, sans-serif` fallback)
**Body Font:** Barlow (same stack) — there is no second typeface; weights 400/500/600/700 load from Google Fonts with `display=swap` and preconnect.

**Character:** One workhorse grotesque doing everything — big, plain, and confident on headlines, quiet and readable in body, tracked-out only at tiny label sizes. The register is district-site clarity, not editorial flair.

### Hierarchy

- **Display** (700, `clamp(2rem, 1.5rem + 2.2vw, 2.9rem)`, line-height 1.2, tracking −0.02em): The page H1 — white on the hero photo (max 18ch) or on the maroon page band.
- **Headline** (600, `clamp(1.45rem, 1.2rem + 1.2vw, 1.9rem)`, line-height 1.2, tracking −0.01em): Section H2s on paper/surface.
- **Title** (600, 1.2rem base, line-height 1.2): H3s; cards tighten to 1.08rem, event titles to 1.05rem, staff names to 1.02rem.
- **Body** (400, 1.0625rem / 17px, line-height 1.65): All running text in Warm Ink; prose caps at 68ch (`--measure`). Secondary text steps down to 0.97–0.95rem in Soft Ink.
- **Label** (600, 0.72rem, line-height 1.1, tracking +0.06em to +0.08em, uppercase): Micro-labels only — event-date months, countdown units ("Days", "Hours" at +0.08em), footer column heads (0.95rem at +0.07em).

Numerals in the countdown band are tabular (`font-variant-numeric: tabular-nums`) at 2.4rem/700 so digits don't dance as they tick.

### Named Rules

**The Uppercase Budget Rule.** Uppercase is reserved for micro-labels (0.72–0.95rem, 600 weight, +0.06–0.08em tracking). Headings and sentences stay in sentence case; nothing large is ever uppercase.

## Layout

Pages stack as full-width bands: maroon utility bar (address, phone, FortifyFL, 0.9rem) → white header (min-height 72px, hairline bottom, wordmark 48px tall, three grouped dropdowns — For Parents / For Students / Our School — and a maroon Enrollment CTA) → maroon page band with white H1 → content sections alternating paper and surface → deep-maroon 4-column footer. The header is static, not sticky.

- **Containers:** 74rem max width (`--container`), 52rem for narrow article/form pages; 1.25rem inline gutters.
- **Section rhythm:** `clamp(2.75rem, 4rem + 2.5vw, 4.5rem)` block padding (`--section`); tight variant `clamp(2rem, 2.5rem + 1.5vw, 3.25rem)`. Page bands pad `clamp(2rem, 4vw, 3rem)`.
- **Card grids:** `repeat(auto-fill, minmax(15rem, 1fr))`, gap 1.25rem; the 3-column directory variant uses `minmax(18rem, 1fr)`; staff grid `minmax(13.5rem, 1fr)`; photo grid `minmax(16rem, 1fr)` with 15rem-tall images.
- **Footer grid:** `1.4fr 1fr 1fr 1.2fr` → two columns at 900px → one column at 560px.
- **Breakpoints:** 940px (nav collapses to a burger panel; header CTA hides), 900px (footer), 800px (two-column home/about splits stack), 700px (Instagram strip 6→3 columns), 560px (footer stacks).
- **Reading:** prose sits in the narrow container at 68ch; section intros max 60ch; hero sub max 52ch. External links in prose get a `↗` suffix.
- **Hero:** full-width real photo at `min(78vh, 640px)` with the maroon-family scrim; content bottom-anchored, H1 max 18ch, two CTAs (light + ghost-light).

### Named Rules

**The Alternating Ground Rule.** Consecutive content sections alternate paper (`#ffffff`) and warm surface (`#f7f5f3`) — never two of the same ground in a row, and never a border where a ground change can do the work.

## Elevation & Depth

The system is flat at rest with two gentle shadows; most "depth" is actually tonal — the paper/surface alternation and the maroon bands carry the hierarchy. Shadows are ink-tinted, never black: both tokens cast from `rgba(36, 27, 29, …)`, the Warm Ink hue.

### Shadow Vocabulary

- **Resting** (`box-shadow: 0 1px 2px rgba(36, 27, 29, 0.06), 0 1px 3px rgba(36, 27, 29, 0.08)` — `--shadow-sm`): Cards, photos, map frame, form card at rest. Barely there.
- **Lifted** (`box-shadow: 0 2px 4px rgba(36, 27, 29, 0.06), 0 6px 16px rgba(36, 27, 29, 0.1)` — `--shadow-md`): Card hover (paired with `translateY(-2px)`), open nav dropdowns, and the mobile nav panel.

### Named Rules

**The Flat-at-Rest Rule.** Nothing rests above `shadow-sm`. The `shadow-md` lift appears only in response to interaction (hover, open state), and cards always pair it with `translateY(-2px)`.

## Shapes

Two radii, hairlines, and no other geometry. Containers round generously (10px, `--radius`): cards, form card, nav dropdowns, photos, map frame, empty state. Controls round tighter (6px, `--radius-sm`): buttons, inputs, event date chips, Instagram tiles, nav links, the skip link's outer corner. Inline prose images use a 4px micro-radius. Borders are 1px hairlines (`#e7e1de`) everywhere; the empty state is the one dashed border; the footer's bottom divider is `rgba(255,255,255,0.15)` on the deep maroon. Staff photos crop to 4:5, Instagram tiles to 1:1, photo-grid images to a 15rem band — always `object-fit: cover`, always 10px radius.

### Named Rules

**The Two Radii Rule.** Every rounded thing is 10px (container) or 6px (control). If a corner needs another number, the component is wrong.

## Components

### Buttons
Pill-adjacent, confident, quiet — a single `.btn` base (1rem/600, padding 0.72rem 1.35rem, 6px radius, 2px transparent border, 150ms ease-out color/border transitions) with four fills.
- **Primary:** Maroon fill, white text; hover deepens to Deepened Maroon. Used for the header Enrollment CTA and form submits.
- **Outline:** Transparent fill, 2px maroon border, maroon text; hover fills Maroon Wash and darkens text. Used for mid-page CTAs on light ground.
- **Light:** Paper fill, maroon text; hover fills Warm Surface. The hero's primary action.
- **Ghost-Light:** `rgba(255,255,255,0.08)` fill with `rgba(255,255,255,0.65)` border, white text; hover fill 0.18. The hero's secondary action over the photo.
- **Focus:** Global 3px solid maroon outline, 2px offset; white outline inside the hero.

### Chips
- **Event date chip:** A 3.4rem-wide maroon block (6px radius) — day in 1.35rem/700, month in the uppercase label style, both white, line-height 1.1. Purely informational; `aria-hidden` with the full date in adjacent text.

### Cards / Containers
- **Card:** Paper fill, 1px hairline border, 10px radius, 1.4rem padding, resting shadow; hover lifts (shadow-md + `translateY(-2px)`, 150ms). H3 at 1.08rem; body in Soft Ink at 0.97rem; maroon "card-link" at 0.95rem/600 when it links out. Link-cards (directory pages, 404) swap the H3 to maroon and drop the underline.
- **Form card:** Paper fill, hairline border, 10px radius, `clamp(1.5rem, 3vw, 2.25rem)` padding, resting shadow, max 40rem — the card that holds every form.
- **Empty state:** The one dashed hairline box (10px radius, 1.5rem padding) with a Soft Ink sentence — used when events/news collections run dry.
- **Map frame:** Hairline border, 10px radius, resting shadow, clipping a 24rem iframe.

### Inputs / Fields
- **Style:** Paper fill, 1px `#cfc7c3` border, 6px radius, 0.65rem 0.8rem padding; hover border `#b9aeaa`.
- **Focus:** 3px solid maroon outline at 1px offset plus a maroon border — the maroon focus ring again.
- **Labels:** 600 weight, 0.97rem; required asterisks in maroon; checkboxes take `accent-color: maroon`; the honeypot field (`.hp`) is visually removed.

### Navigation
White header, static, 72px min-height, hairline bottom. Wordmark (48px tall, the wide PNG via astro:assets) left; three grouped dropdowns (For Parents / For Students / Our School) right; maroon Enrollment CTA far right. Toggles are 1rem/600 text buttons with a 10px caret that rotates 180° when expanded; dropdowns are paper panels (min-width 15rem, 10px radius, shadow-md, 0.5rem padding) whose links (0.97rem/500) fill Maroon Wash on hover/focus. Opens on hover, `:focus-within`, and click (JS-managed `aria-expanded`); at 940px the nav collapses to a burger button and a full-width paper panel. Above it: the maroon utility bar (0.9rem, white links at 0.92 → solid on hover). Below everything: the deep-maroon footer — white brand row, uppercase tracked column heads, white 0.85 links → solid on hover, bottom bar over a white 0.15 divider.

### Signature Components
- **Hero:** Real school photo, maroon-family scrim, bottom-anchored white H1 (max 18ch) + sub (max 52ch) + two CTAs. The first viewport is a photograph, not a layout.
- **Page band:** Maroon strip with the white H1 (and optional 0.85-white intro, max 60ch) that opens every inner page.
- **Countdown band:** Maroon strip (tight rhythm) with 2.4rem/700 tabular numerals over uppercase tracked labels; ticks once a second to the CMS-set target date.
- **Event row:** Hairline-separated flex row — maroon date chip left, 1.05rem title + Soft Ink date right; last row drops its border.
- **Staff card:** Centered 4:5 photo (10px radius, resting shadow); when no photo exists, a Maroon Wash tile carries the person's initials in 2.2rem/700 maroon. Name at 1.02rem, role in maroon 0.92rem/500, mail link in Soft Ink 0.85rem.
- **Announcement strip:** When the front office sets one, a Maroon Wash strip with a hairline bottom edge sits above the hero — 600-weight Deepened Maroon text, `role="status"`.
- **Instagram strip:** Six square tiles (6px radius) of real community photos, three per row under 700px; tiles zoom to `scale(1.05)` on hover (200ms).
- **Article layout:** Page band → narrow container → 68ch prose with a "Last updated" line (Soft Ink 0.88rem over a hairline) when the CMS carries a date.
- **404:** Page band ("Page Not Found") + three link-cards — homepage, calendar, contact the office.
- **Skip link:** Hidden until focused, then a maroon tab with white 600 text at the viewport's top-left (bottom-right corner rounded 6px).

## Do's and Don'ts

### Do:
- **Do** spend maroon on structure and action only — utility bar, page bands, buttons, links, date chips, countdown, footer — never as a large content ground.
- **Do** flip `:focus-visible` to white (`outline-color: #fff`) on every maroon or deep-maroon surface: utility bar, page band, countdown, footer, hero.
- **Do** use real school photography through the astro:assets pipeline (responsive `widths`, `sizes`, lazy except the hero) — never stock, never illustration.
- **Do** render every date through UTC-pinned `Intl.DateTimeFormat` formatters (`timeZone: 'UTC'`).
- **Do** keep prose within the 68ch measure; section intros at 60ch.
- **Do** give cards the resting shadow only, adding the hover lift (shadow-md + `translateY(-2px)`) on interaction.
- **Do** use Barlow at 400/500/600/700 with tight tracking on display sizes (−0.02em H1, −0.01em H2).
- **Do** preserve every existing URL path; retire one only with a true 301 (`public/_redirects`).
- **Do** collapse all animation and transition durations under `prefers-reduced-motion: reduce`.

### Don't:
- **Don't** introduce a second hue, gradient decoration, or thematic motifs — the register is the conventional modern district site, chosen over art-directed worlds.
- **Don't** uppercase sentences or headings; uppercase belongs to 0.72–0.95rem tracked micro-labels.
- **Don't** use shadows beyond the two tokens, or `shadow-md` on resting content.
- **Don't** use any radius besides 10px (containers) and 6px (controls).
- **Don't** invent staff, events, photos, or claims — real content only, published by the front office.
- **Don't** use another focus treatment: 3px solid maroon, 2px offset (white on dark bands), nothing else.
- **Don't** add a second typeface or a display font pairing — Barlow is the whole system.
