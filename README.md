# Something Wonderful Studios site

Marketing site for Something Wonderful Studios, served at somethingwonderfulstudios.com.

## Structure

- Repo root — the deployable static site (`index.html` and media)
- `assets/` — source imagery (excluded from deploys via `.vercelignore`)
- `tools/` — wordmark generation (excluded from deploys)

## Deploy

Pushes to `main` deploy to production via the Vercel GitHub integration. Manual deploys: `vercel --prod` from the repo root.

Secrets live in `.env.local` and are never committed. Project context lives in the workspace front door (`1 Projects/Something Wonderful Studios Site/PROJECT.md`).
