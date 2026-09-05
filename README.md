# Something Wonderful Studios site

Marketing site for Something Wonderful Studios, served at somethingwonderfulstudios.com.

## Structure

- Repo root — the deployable static site (`index.html` and the hero media)
- `bloom/` — the Bloom first-look media: five H.264 films (760x1172, on paper) with JPEG posters, two home-screen captures and the app icon, all exported from `_build/Bloom/` in the workspace
- `assets/` — source imagery (excluded from deploys via `.vercelignore`)
- `tools/` — wordmark generation (excluded from deploys). `wordmark.svg` and `bloom.svg` are Apple Garamond Light outlines produced with `wordmark.py`; the font itself is never served

## Page

One file, no build step, no dependencies. The hero is unchanged; below it a "first look" section presents Bloom as an accordion whose stage changes with the selected item (films, screenshots, the icon), then a footer with the Instagram link. Inline script only: it switches items, plays the active film, chains the four performance films, and pauses everything off-screen or when the tab is hidden. Reduced motion shows posters and stills.

## Deploy

Pushes to `main` deploy to production via the Vercel GitHub integration. Manual deploys: `vercel --prod` from the repo root.

Secrets live in `.env.local` and are never committed. Project context lives in the workspace front door (`1 Projects/Something Wonderful Studios Site/PROJECT.md`).
