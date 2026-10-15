# Member portal backend configuration

The public source tree intentionally contains **no active Supabase project URL or publishable key** for the member dashboard/community pages.

`docs/member-pilot.html` and `docs/member-community.html` contain inert placeholders:

- `__COALITION_SUPABASE_URL__`
- `__COALITION_SUPABASE_PUBLISHABLE_KEY__`

The Pages deployment renders those placeholders only in the generated `site-preview/` output by running `render_config.py render site-preview`.

The official repository must define these GitHub Actions repository variables:

- `COALITION_SUPABASE_URL`
- `COALITION_SUPABASE_PUBLISHABLE_KEY`

A fork or clone does not inherit repository variables, so its member pages remain unconfigured and cannot accidentally use the Coalition's live Supabase backend.

The pull-request build runs `render_config.py check docs` and fails if a live `*.supabase.co` URL or `sb_publishable__...` key is committed back into either member page.

The publishable key is not a secret credential, but keeping operational configuration out of source prevents accidental cross-environment use. Supabase authorization, RLS, JWT verification, and Edge Function origin checks remain the actual security boundaries.
