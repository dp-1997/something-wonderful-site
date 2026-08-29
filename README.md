# Something Wonderful Studios site

Marketing site for Something Wonderful Studios, served at somethingwonderfulstudios.com.

## Structure

- `site/` — the deployable static site (deployed to Vercel via the CLI)
- `assets/` — source imagery
- `tools/` — wordmark generation

## Deploy

From `site/`:

```
vercel --prod
```

Secrets live in `.env.local` and are never committed. Project context lives in the workspace front door (`1 Projects/Something Wonderful Studios Site/PROJECT.md`).
