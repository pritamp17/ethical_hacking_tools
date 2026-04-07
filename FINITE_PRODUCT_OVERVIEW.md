# Finite — Product Overview for Designer

Hey, here's everything you need to understand Finite before you start designing.
Read this once before opening Figma. The psychology context matters as much as
the visual specs — it's what separates a stoic app from another generic
dark-themed productivity app.

---

## What is Finite?

Finite is a stoic productivity mobile app built around one core idea: a
real-time death countdown.

When users open the app, they see exactly how many days they have left to live
(calculated from their age + life expectancy). This number ticks down in real
time. Around this countdown, the app helps them stop wasting that time through
goal tracking, social media awareness, and a smart morning alarm.

**Tagline:** Your time is Finite. Make it count.

**Target user:** Self-improvement focused individuals aged 22-40 — founders,
developers, creators, students. People who already read stoic philosophy, follow
productivity creators, and want a tool that takes them seriously instead of
gamifying their attention with cartoon mascots.

---

## The core philosophy — why this app exists

Read this section twice. It shapes every design decision.

**Mortality awareness as motivation.** Most people unconsciously avoid thinking
about death. This avoidance makes them anxious, distracted, and aimless. Robert
Greene writes in _Laws of Human Nature_ that confronting mortality has the
paradoxical effect of making us feel more alive, focused, and purposeful. The
death counter is not morbid — it is a daily meditation on what matters.

**External discipline becoming self-discipline.** Chanakya in _Arthashastra_
describes appointing a minister to remind the king when he wastes time. Finite
plays this role digitally — alarms, reminders, and notifications act as a
"minister" that pricks the user when they drift. Over time, external discipline
internalizes.

**Diminishing returns of pleasure.** Social media delivers diminishing dopamine
returns. Users need more and more scrolling for less and less satisfaction.
Finite reframes this cost in the most visceral terms possible: percentage of
remaining life. "You spent 0.03% of your remaining life on Instagram today" hits
harder than "you spent 47 minutes."

**Purpose as a force multiplier.** When daily actions are connected to
life-level goals, motivation multiplies. Finite's goal system creates this
connection — every check-in feels meaningful because it's tied to a finite life.

---

## The feeling we want users to have

When a user opens this app, it should feel like checking a luxury watch that
reminds them their time is finite.

**Premium. Weighty. Honest. Slightly uncomfortable** — in a way that makes them
want to stop scrolling and start living.

**Reference vibes:**

- Apple Watch Hermès edition or Patek Philippe app
- A stoic philosophy book (dark, serif quotes)
- A minimal terminal UI (monospace numbers)
- The Stoic app on iOS (the dark serif aesthetic, not the overdone parts)

**NOT references:**

- Notion, Todoist, or any colorful productivity app
- Headspace's recent rainbow redesign
- Duolingo or any gamified app with mascots
- Any app with playful illustrations

If you ever catch yourself thinking "this needs more color" or "this needs an
illustration here" — stop. The restraint IS the brand.

---

## Brand system

### Colors — these are the only colors in the app

| Token         | Hex                        | Where it's used                                                      |
| ------------- | -------------------------- | -------------------------------------------------------------------- |
| void          | `#0A0A0A`                  | Primary background everywhere                                        |
| surface       | `#111111`                  | Cards, elevated surfaces                                             |
| surfaceLight  | `#1A1A1A`                  | Input fields, secondary cards                                        |
| **gold**      | `#C9A227`                  | The ONLY accent color — CTAs, death counter, progress, active states |
| goldMuted     | `rgba(201, 162, 39, 0.15)` | Gold tint backgrounds                                                |
| goldDim       | `rgba(201, 162, 39, 0.08)` | Subtle selected states                                               |
| text          | `#F5F5F5`                  | Primary text                                                         |
| textSecondary | `#888888`                  | Secondary text                                                       |
| textTertiary  | `#555555`                  | Hints, disabled                                                      |
| border        | `#222222`                  | Default borders                                                      |
| borderLight   | `#333333`                  | Subtle borders                                                       |
| danger        | `#FF4444`                  | Over-limit warnings ONLY                                             |
| dangerBg      | `rgba(255, 68, 68, 0.08)`  | Danger background tint                                               |
| success       | `#4CAF50`                  | Completed states                                                     |

**No blues, no purples, no pinks, no greens** (except success state). Gold is
the only accent. Dark backgrounds always. No light mode.

### Typography

| Role            | Font                               | Weight     | Used for                                |
| --------------- | ---------------------------------- | ---------- | --------------------------------------- |
| Counter numbers | Space Mono / JetBrains Mono        | 500        | Death counter, clock, all time displays |
| Headings        | Inter                              | 600        | Screen titles                           |
| Body            | Inter                              | 400        | Card text, descriptions                 |
| **Quotes**      | **Lora italic / Playfair Display** | 400 italic | **Stoic quotes ONLY**                   |
| Captions        | Inter                              | 400        | Timestamps, micro labels                |

**Critical:** All numbers use monospace. Equal-width digits prevent the death
counter from "jumping" as it ticks every second. This is non-negotiable.

**Critical:** Serif italic is reserved exclusively for stoic quotes. Don't use
it for headings or body. It marks the philosophical voice in the app.

### Spacing scale

Use only these values: `4px, 8px, 12px, 16px, 24px, 32px`

### Border radius

- Cards: `14px`
- Buttons (primary): `999px` (full pill)
- Input fields: `10px`
- Small badges: `6px`

### Logo

Use the gold hourglass file I'm sending you. **Do not redesign it.** Use it in:

- Welcome splash (large, centered)
- Onboarding header (small)
- Share card (with wordmark)
- Tab bar Home icon (very small)

---

## Design rules — what to do and not do

### Do

- ✅ Use generous whitespace — let the death counter breathe
- ✅ Make the death counter the visual hero of the home screen
- ✅ Keep numbers in monospace, equal-width
- ✅ Use serif italic ONLY for stoic quotes
- ✅ Use thin gold dividers (1px, 30% opacity)
- ✅ Use gold borders on selected/active states
- ✅ Use subtle progress bars (3px height max)
- ✅ Keep cards flat with subtle 1px borders
- ✅ Treat each screen like a meditation, not a dashboard

### Don't

- ❌ NO gradients of any kind
- ❌ NO drop shadows (except focus rings)
- ❌ NO glassmorphism or blur effects
- ❌ NO neon glow effects
- ❌ NO illustrations or characters
- ❌ NO emoji as core UI elements
- ❌ NO playful icons — use simple line icons only
- ❌ NO bubbly rounded everything
- ❌ NO additional accent colors beyond gold
- ❌ NO light mode variant
- ❌ NO "modern productivity app" vibes (think stoic temple, not Notion)

---

## App structure — the 12 screens

Here's the full app at a high level. The detailed brief I sent you has each
screen specified. This section just explains how everything connects.

### Onboarding flow (6 screens)

The user goes through these in order before reaching the main app. Each screen
builds emotional momentum toward the paywall.

1. **Welcome / splash** — logo + "Your time is Finite" + Begin button
2. **Age input** — user enters their age, immediately sees their remaining days
   calculated (this is the FIRST emotional hit)
3. **Goal selection** — user picks up to 3 life goals (they're now committing to
   something)
4. **Alarm time setup** — user picks their wake-up time (commitment to
   discipline)
5. **Social media app limits** — user sets daily limits for Instagram, YouTube,
   etc. (commitment to focus)
6. **Paywall** — appears at peak emotional engagement, after user has seen their
   death counter

**The paywall is the most important conversion screen.** By this point, the user
has emotionally invested in the death counter, picked goals, and committed to
discipline. They're primed to pay. The paywall must capitalize on this — it's
the highest-conversion moment in the entire user journey.

### Main app — 5 tabs

After onboarding (and paying or skipping), the user lands in the main app with 5
tabs at the bottom.

**Tab 1: Home (the soul of the app)**

- The death counter is the visual hero
- Below it: digital clock
- Below that: today's focus goal with progress
- At the bottom: a daily stoic quote in serif italic
- This is the screen users will open every morning. It must feel reverent.

**Tab 2: Goals**

- List of the user's life goals (max 3)
- Each goal has a daily check-in button
- Weekly progress bar (7 segments, gold = completed)
- Streak counter
- This is where habits form. The check-in must feel satisfying.

**Tab 3: Social media tracker (Guard)**

- List of tracked apps (Instagram, YouTube, TikTok, X, Reddit, Snapchat)
- Each shows minutes used today + life percentage cost
- Over-limit apps highlighted in red
- Bottom: weekly summary "This week: 4.2 hours lost • 0.04% of your remaining
  life"
- This is where guilt becomes motivation.

**Tab 4: Alarm (Wake)**

- User's set wake-up time
- Today's motivational message (changes daily)
- Today's alarm sound (changes daily)
- This is what they see before going to sleep.

**Tab 5: Leaderboard (Rank)**

- "Warriors of discipline" — weekly rankings
- User's own rank highlighted at top
- Top 50 users with points + streaks
- Resets every Monday
- This creates social accountability.

### Secondary screens

- **Settings** — profile, goals, notifications, subscription, about
- **Share card modal** — generates a shareable image (1080×1920) with user's
  remaining days for Instagram Stories
- **Morning alarm overlay** — full-screen takeover when user opens app after
  alarm fires

---

## Feature deep dive

### 1. The death counter (the most important element in the entire app)

**What it shows:**

- Main number: total days remaining (e.g., "18,247")
- Below: breakdown of years / months / days / hours
- Updates in real-time (ticks every second)

**How it's calculated:**

- User enters their current age during onboarding
- App assumes 75-year life expectancy by default (configurable in settings)
- Remaining time = death date - current time
- Recalculated continuously

**Design importance:** This is THE component. If the death counter looks weak,
the entire product fails. It must feel weighty, premium, intentional. Like a
luxury watch face.

**Variants you'll design:**

- **Large** (home screen) — 48-56px gold mono number with full breakdown row
- **Medium** (paywall, alarm overlay) — 32px gold mono number with label
- **Mini** (notifications, share button area) — 16-20px inline format

### 2. Goal tracker

**What it does:**

- User picks up to 3 life goals during onboarding (e.g., "Build a profitable
  business", "Get physically fit")
- Each day, user checks in: "Did I work on this goal today?"
- Building streaks rewards consistency
- Breaking streaks shows in danger red

**Design importance:** The check-in interaction must feel satisfying. When the
user taps the checkbox, it should animate (gold fill + subtle haptic). The
weekly progress bar should make 7 days visible at a glance.

### 3. Social media tracker

**What it does:**

- Tracks time spent on Instagram, YouTube, TikTok, X, Reddit, Snapchat
- On Android: uses real usage data via system APIs
- On iOS: uses self-report (user tells app what they were on)
- Shows time as percentage of remaining life: "47 minutes = 0.03% of your
  remaining life"
- Notifies when user exceeds daily limit

**Design importance:** This is where guilt becomes motivation. The "life
percentage" number must be visible and prominent. Over-limit state must use red
without being cartoonish.

### 4. Smart alarm with motivation

**What it does:**

- User sets wake-up time (e.g., 5:00 AM)
- Each morning, the alarm fires with a different sound and a different
  motivational message
- Sounds and messages are pulled from the backend daily
- When user opens app after alarm, they see a full-screen "good morning" overlay
  with the death counter, today's message, and today's goal

**Design importance:** The alarm tab must feel like a ritual. The morning
overlay must feel like a wake-up call from a stoic mentor.

### 5. Leaderboard (warriors of discipline)

**What it does:**

- Weekly rankings based on points earned
- Points come from goal check-ins, alarm wake-ups, staying under social limits,
  streaks
- Top 50 users shown
- User's own rank highlighted at top
- Resets every Monday

**Design importance:** This creates social accountability. Users see they're not
alone in trying to be disciplined. The user's own rank card must feel personal
(gold border).

### 6. Share card

**What it does:**

- User can generate a shareable image of their death counter
- Shows: "I have 18,247 days left. How many do you have?"
- Format: 1080×1920 (Instagram Stories)
- Black background, gold number, Finite branding at bottom
- This is a viral growth mechanism — every share is a free ad

**Design importance:** This image will be seen by people who don't have the app
yet. It must be striking enough to stop the scroll on Instagram Stories. The
number must dominate. The branding must be subtle but recognizable.

---

## The user journey emotional arc

This is the psychological journey the design must support:

1. **Welcome** — curiosity. "What is this?"
2. **Age input** — slight anxiety. "How old am I?"
3. **First death counter reveal** — SHOCK. "I only have THAT many days?"
4. **Goal selection** — determination. "I need to do something about this."
5. **PAYWALL** — peak emotional engagement. They're emotionally invested and
   ready to commit.
6. **Home screen (daily use)** — reverence. "Let me check my time today."
7. **Goal check-in** — satisfaction. "I'm doing it."
8. **Social tracker** — guilt → motivation. "I wasted that much?"
9. **Alarm tomorrow morning** — discipline. "Time to rise."

Every screen must support its place in this arc. The home screen should feel
reverent, not transactional. The social tracker should feel like a mirror, not
an accusation. The leaderboard should feel like a brotherhood, not a
competition.

---

## Tab bar specification (appears on all 5 main screens)

This is critical — it appears on every main tab so it must be perfect.

**Specs:**

- Background: `#0A0A0A`
- Top border: 1px `#222222`
- Height: 64px + safe area padding
- 5 tabs evenly distributed
- Each tab has: icon (20×20) + label (10px) below

**Active state:**

- Gold icon (`#C9A227`)
- Gold label visible
- Subtle gold tint background (optional)

**Inactive state:**

- Icon color: `#555555`
- Label NOT visible (only the active tab shows its label)

**Tabs:**

1. **Hourglass icon** — "Home"
2. **Target / circle icon** — "Goals"
3. **Shield icon** — "Guard"
4. **Bell icon** — "Wake"
5. **Trophy / star icon** — "Rank"

Use simple line icons. No filled icons. No detailed illustrations.

---

## Key components to design

These will be reused across screens. Build them as Figma components with
variants.

### Buttons

- **GoldButton (Primary)** — gold bg, black text, pill shape, 48px height
- **OutlineButton (Secondary)** — transparent, gray border, gray text, pill
  shape
- **GhostButton (Tertiary)** — transparent, no border, gold text, used for
  skip/cancel
- **IconButton** — circular, dark surface bg, gold icon

### Cards

- **SurfaceCard** — `#111` bg, no border, 14px radius, 16px padding
- **BorderedCard** — `#111` bg, 1px `#222` border
- **SelectedCard** — gold dim bg, 1px gold border (for selected goals, options)
- **DangerCard** — danger bg tint, 1px danger border (for over-limit social
  apps)
- **HighlightedCard** — gold muted bg, 1.5px gold border (for user's own rank)

### Death counter (3 variants)

- **Large** — home screen hero
- **Medium** — paywall, alarm overlay
- **Mini** — notifications, inline displays

### Other components

- **WeeklyProgressBar** — 7 segments showing Mon-Sun
- **StreakBadge** — small pill with day count
- **QuoteCard** — italic serif quote + gold attribution
- **GoalCheckbox** — square, 24×24, gold filled when checked
- **SocialAppCard** — over-limit and under-limit variants
- **LeaderboardRow** — top 3 special variants + regular
- **TabBar** — full bar with 5 tab states
- **DividerGold** — 1px line at 30% opacity gold
- **SectionLabel** — uppercase gold label with letter-spacing

---

## What success looks like

When the design is done, here's what I should see:

1. **The home screen makes me feel something.** Opening it should feel like
   reading the first page of _Meditations_ by Marcus Aurelius. Reverent. Honest.
   Slightly uncomfortable.

2. **The death counter is unmistakable.** It's the largest, most prominent
   element on the home screen. There's no doubt what this app is about.

3. **Every screen feels intentional.** No random spacing, no decorative elements
   that don't serve a purpose. Every pixel earned its place.

4. **It looks expensive without being flashy.** Like a luxury watch — the value
   comes from precision and restraint, not glitter.

5. **A user could open this app at 6 AM with the lights off and not be jarred.**
   Pure dark, minimal contrast where it shouldn't matter, sharp contrast only
   where it should.

6. **It doesn't look like any other productivity app.** I should be able to put
   it next to Notion, Todoist, Headspace, and Calm — and Finite should feel like
   it belongs in a different category entirely. Not a productivity tool. A
   philosophical practice.

---
