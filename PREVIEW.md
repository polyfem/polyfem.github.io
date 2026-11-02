# User guide preview

Browse **https://polyfem.github.io/previews/polyfem-user-guide/**.

`Check Website` builds the normal site for pull requests and other branches.
For pushes or manual runs on `polyfem-user-guide`, it builds `mkdocs-preview.yml`, uploads
the `user-guide-preview` artifact, and publishes only
`previews/polyfem-user-guide/` on the existing Pages source branch, `main`.
Pull requests cannot run the publishing job. No new repository, secret, hosting
service, or Pages configuration change is required.

The preview configuration inherits the normal site configuration but gives it a
separate title, canonical URL, sitemap, and edit links. Internal navigation,
assets, and search are built for the preview path. The explicitly external C++
API documentation link continues to point to the published API documentation.

The publisher requires a clean checkout with an existing production homepage,
replaces only the fixed preview directory, rejects symlinks, and checks every
staged path before committing. It uses an ordinary fast-forward push, never
`mkdocs gh-deploy --force`. If production changes while publishing, the push
fails safely; rerun the workflow after production finishes. Safety tests cover
unchanged production files, stale preview removal, symlinks, dirty checkouts,
and a concurrent production update.

Because pushes made with `GITHUB_TOKEN` do not themselves trigger Pages builds,
the publishing job explicitly requests a Pages build with `pages: write`. It
first checks that Pages is still configured to serve `main` at `/`. It then
waits for the preview's source-commit marker and checks the homepage, a nested
tutorial, local assets, canonical URLs, and search. The workflow summary links
to the preview; `preview.json` records which source commit is live.

## Production deployment limitation

The existing production workflow on `docs` uses `mkdocs gh-deploy --force` to
replace all of `main`. A later production deployment can therefore remove the
preview. After production finishes, rerun the latest successful `Check Website`
run on `polyfem-user-guide` (or push to that branch) to restore it. This change
does not alter the production workflow on `docs` or the Pages settings. The
production workflow in this branch also has an explicit `docs` branch guard,
so manually running it on the preview branch cannot publish over production.

Download the `user-guide-preview` artifact from a successful build if you need a
snapshot even when publication fails or production has removed the preview.
Serve the extracted files with `python -m http.server` and open the local URL.

Run the publisher safety tests locally with:

```sh
python -m unittest discover -s .github/scripts -p 'test_*.py' -v
```
