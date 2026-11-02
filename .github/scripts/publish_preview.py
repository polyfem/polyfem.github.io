"""Publish only the fixed preview subtree; never force-push the Pages branch."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess


PREFIX = "previews/polyfem-user-guide"


def git(repository, *args):
    return subprocess.check_output(
        ["git", "-C", str(repository), *args], stderr=subprocess.STDOUT
    ).decode().strip()


def stage_preview(site, repository, source_sha):
    site, repository = Path(site).resolve(), Path(repository).resolve()
    if not (site / "index.html").is_file():
        raise RuntimeError("Preview must contain index.html")
    if any(path.is_symlink() for path in site.rglob("*")):
        raise RuntimeError("Preview must not contain symlinks")
    if git(repository, "status", "--porcelain", "--untracked-files=all"):
        raise RuntimeError("Pages checkout must be clean")
    if not (repository / "index.html").is_file():
        raise RuntimeError("Refusing to initialize or replace the production site")
    target = repository / PREFIX
    for path in (repository / "previews", target):
        if path.is_symlink() or (path.exists() and not path.is_dir()):
            raise RuntimeError("Preview destination must be a real directory")
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(exist_ok=True)
    shutil.copytree(site, target)
    (target / "preview.json").write_text(json.dumps({"source_sha": source_sha}) + "\n")
    git(repository, "add", "--all", "--", PREFIX)
    # Check all staged changes, including deletions, before making a commit.
    changed = git(repository, "diff", "--cached", "--name-only", "-z").split("\0")
    if any(name and not name.startswith(PREFIX + "/") for name in changed):
        raise RuntimeError("Refusing a change outside the preview directory")
    return any(changed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path)
    parser.add_argument("repository", type=Path)
    args = parser.parse_args()
    if os.environ.get("GITHUB_REF") != "refs/heads/polyfem-user-guide":
        raise RuntimeError("Only polyfem-user-guide may publish this preview")
    if os.environ.get("GITHUB_EVENT_NAME") not in {"push", "workflow_dispatch"}:
        raise RuntimeError("Pull requests must never publish previews")
    source_sha = os.environ["GITHUB_SHA"]
    if stage_preview(args.site, args.repository, source_sha):
        git(args.repository, "config", "user.name", "github-actions[bot]")
        git(args.repository, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        git(args.repository, "commit", "-m", f"Preview polyfem-user-guide at {source_sha[:12]}")
        # A concurrent production deployment causes rejection, never a force-push.
        git(args.repository, "push", "origin", "HEAD:refs/heads/main")
    print(f"Published {PREFIX} from {source_sha}")


if __name__ == "__main__":
    main()
