# Field Guide preview

The same MkDocs configuration supports both local review and the public GitHub Pages reading preview. The Markdown files under `docs/` remain the source of truth.

## Windows

From the repository root, run:

```powershell
.\preview\preview.ps1
```

Or double-click `preview\preview.cmd`.

The first run creates `.venv-preview`, installs the preview dependencies, and opens the guide at:

```
http://127.0.0.1:8000/
```

MkDocs watches the Markdown files. Saving a chapter normally refreshes the browser automatically, so the preview stays useful while the guide is being written.

## macOS / Linux

From the repository root:

```bash
./preview/preview.sh
```

## Hosted preview

The private source repository builds the MkDocs site and publishes only the generated static files to the separate public repository:

```
GitHubChrisRice/1A-Field-Guide-Site
```

Expected public URL:

```
https://githubchrisrice.github.io/1A-Field-Guide-Site/
```

The public repository should use **Settings → Pages → Deploy from a branch → main / (root)**.

The private source repository also needs one Actions secret named `FIELD_GUIDE_SITE_TOKEN`. Use a fine-grained personal access token restricted to `GitHubChrisRice/1A-Field-Guide-Site` with **Contents: Read and write** permission. The workflow uses that token only to replace the generated site files and push the resulting commit.

The site is a presentation layer only. The private research repository remains private.

## Build a static copy

After the preview environment exists:

```powershell
.\.venv-preview\Scripts\python.exe -m mkdocs build
```

The generated static site is written to `site-preview/`. That folder is disposable output and should not be committed.

## Design intent

The preview is a reading layer over the existing Markdown source. The legal chapters remain the source of truth. Branding, colors, and eventual public hosting can change later without rewriting the research files.
