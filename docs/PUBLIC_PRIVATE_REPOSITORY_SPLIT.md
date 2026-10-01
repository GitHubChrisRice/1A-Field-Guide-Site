# Public/Private Repository Split

This document records the repository architecture selected for the 1A Field Guide publication system.

## Decision

The project will **not** make the existing `GitHubChrisRice/1A-Field-Guide` repository public merely to obtain free branch-protection features.

Instead:

| Repository / branch | Visibility | Purpose |
| --- | --- | --- |
| `GitHubChrisRice/1A-Field-Guide` | Private | Internal research/workspace, investigations, raw or unpublished evidence, requester/member-sensitive material, Coalition administration, pre-publication work |
| `GitHubChrisRice/1A-Field-Guide-Site/main` | Public | Authoritative reviewed public source for the Field Guide, public Registry, approved public methodology/research, licensing/origin notices, and site build configuration |
| `GitHubChrisRice/1A-Field-Guide-Site/gh-pages` | Public generated output | Built MkDocs website served through GitHub Pages |

The public repository is therefore both the canonical public-source repository and the host for generated Pages output, but source and generated output occupy separate branches and have separate authority paths.

## Why this split

The private repository contains material that should not become public merely to obtain repository protections.

The public repository can use GitHub's public-repository branch/ruleset protections without requiring a paid plan. This lets the future Coalition exporter prepare draft pull requests against protected public `main` while preserving a separate human merge gate.

The split also makes publication intentional. Internal existence does not imply public release.

## Publication boundary

```text
PRIVATE 1A-Field-Guide
internal research / evidence / review
        |
        | approved immutable PublicationCandidateRevision
        v
controlled export
        |
        v
PUBLIC 1A-Field-Guide-Site
protected main
        |
        | draft PR + checks + human merge
        v
authoritative public source
        |
        | deterministic MkDocs build
        v
gh-pages
        |
        v
public website
```

## Public-source inclusion rule

A file belongs in public-source `main` only when it is deliberately appropriate for public inspection and publication.

Likely public-source categories include:

- national and state Field Guide doctrine;
- public jurisdiction status and qualification summaries;
- approved public Registry entries and public-safe structured Registry data;
- public methodology and source-provenance material intended for readers;
- approved public research/evidence derivatives;
- MkDocs configuration and public build tooling;
- README, license, contribution guidance, project-origin notice, and other public governance needed to understand the published project.

A file does **not** become public merely because it currently exists under `docs/` in the private repository or because the current MkDocs build happens to render it.

## Private-workspace retention rule

The following remain private by default unless an exact derived publication artifact later passes the publication workflow:

- investigations and investigation dashboard data;
- requester identity/contact information;
- member/authentication/private attribution information;
- raw records productions or unpublished evidence;
- sensitive attachments and metadata;
- internal review discussion not intended for publication;
- administrative audit/security records;
- credentials/secrets;
- draft or rejected material;
- pre-publication research whose release has not been deliberately approved.

Where public material depends on a private source, publish an approved derivative, citation, excerpt, summary, or sanitized evidence artifact rather than copying the private working record wholesale.

## Project origin and license

The public source repository should contain, at minimum:

- `LICENSE.md`;
- `PROJECT_ORIGIN.md`;
- a README identifying the canonical repository/site; and
- a site footer or equivalent public notice identifying the canonical project.

The existing handbook/documentation license is CC BY-SA 4.0. The project-origin notice is intended to make canonical provenance clear; it is not represented as an undeletable file in third-party clones.

The canonical repository should protect origin/license files through normal branch protections and, where useful, CODEOWNERS/review rules. A signed release/tag may additionally provide tamper-evident historical evidence of the public launch state.

Executable software/build tooling should receive an appropriate software license rather than relying silently on the documentation license.

## Migration safety rule

Do not replace the current public repository `main` until the current generated site has first been preserved and GitHub Pages has been pointed at the intended deployment branch/workflow.

The migration sequence is:

1. Audit current private source into **public / private / needs-review** categories.
2. Create `gh-pages` from the current generated public-site state.
3. Configure GitHub Pages/deployment to serve `gh-pages` or an equivalent Pages deployment target.
4. Verify the existing public URL still renders correctly.
5. Prepare a new public-source `main` containing only approved public material.
6. Add `PROJECT_ORIGIN.md`, license notices, README, build configuration, and public-source contribution guidance.
7. Configure public `main` branch protection/rulesets:
   - pull requests required;
   - required validation/build checks;
   - no force push;
   - no branch deletion;
   - Coalition export integration is not a bypass actor;
   - final merge remains with separately authorized human repository operators.
8. Change the site build workflow to build from public `main` and deploy generated output to `gh-pages`.
9. Remove the old private-repository workflow that overwrites public `main`.
10. Verify source build, deployment, public URL, branch protection, and rollback path.
11. Only then enable Phase 2 Coalition branch/draft-PR export.

## Current operational status

At the time this decision was recorded:

- `GitHubChrisRice/1A-Field-Guide` is private and remains the active source/workspace;
- `GitHubChrisRice/1A-Field-Guide-Site` is public, but its `main` currently contains generated website output rather than authoritative source;
- the existing private-repository Actions workflow publishes generated output by replacing the public site's `main`;
- the current ChatGPT GitHub integration can read the public site repository but cannot create refs there, so it cannot perform the branch migration itself from this connection;
- no live-site branch or Pages setting should be changed until a repository operator performs the preservation/configuration steps above.

## Rollback

Before changing the public repository's default/source branch behavior, preserve the current generated-site commit on a dedicated branch/tag. If the new source/build/deployment path fails, Pages can be pointed back to the preserved generated branch while the migration is corrected.

## Success criteria

The split is complete when:

- the live site remains reachable at its existing public URL;
- public `main` contains human-readable authoritative source rather than generated HTML;
- generated site output is isolated to the Pages deployment branch/workflow;
- public `main` is technically protected;
- the private workspace is no longer the publication target;
- private-only material cannot enter public source without the publication-candidate process;
- the public build is reproducible from public `main`;
- project-origin and licensing notices are present;
- the old workflow that overwrites public `main` is retired; and
- Phase 2 export can create draft PRs without any integration authority to merge protected `main`.
