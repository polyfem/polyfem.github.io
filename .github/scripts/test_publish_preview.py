import tempfile
from pathlib import Path
import subprocess
import unittest

from publish_preview import PREFIX, git, stage_preview


class PreviewSafetyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repository = self.root / "published"
        self.repository.mkdir()
        git(self.repository, "init", "-b", "main")
        git(self.repository, "config", "user.name", "Test")
        git(self.repository, "config", "user.email", "test@example.com")
        (self.repository / "index.html").write_text("Production home")
        (self.repository / "CNAME").write_text("example.com")
        (self.repository / ".nojekyll").touch()
        (self.repository / "other-docs").mkdir()
        (self.repository / "other-docs/index.html").write_text("Other docs")
        (self.repository / PREFIX).mkdir(parents=True)
        (self.repository / PREFIX / "stale.html").write_text("Old preview")
        git(self.repository, "add", ".")
        git(self.repository, "commit", "-m", "Initial production")
        self.site = self.root / "site"
        self.site.mkdir()
        (self.site / "index.html").write_text("New preview")

    def test_replaces_only_preview_and_preserves_production(self):
        before = git(self.repository, "ls-tree", "-r", "HEAD").splitlines()
        self.assertTrue(stage_preview(self.site, self.repository, "abc123"))
        git(self.repository, "commit", "-m", "Preview")
        after = git(self.repository, "ls-tree", "-r", "HEAD").splitlines()
        outside_preview = lambda rows: [row for row in rows if "\t" + PREFIX + "/" not in row]
        self.assertEqual(outside_preview(before), outside_preview(after))
        self.assertFalse((self.repository / PREFIX / "stale.html").exists())
        self.assertIn("abc123", (self.repository / PREFIX / "preview.json").read_text())
        self.assertFalse(stage_preview(self.site, self.repository, "abc123"))

    def test_rejects_dirty_checkout(self):
        (self.repository / "index.html").write_text("Unexpected change")
        with self.assertRaisesRegex(RuntimeError, "clean"):
            stage_preview(self.site, self.repository, "abc123")

    def test_rejects_destination_symlink(self):
        git(self.repository, "rm", "-r", PREFIX)
        (self.repository / PREFIX).parent.mkdir(exist_ok=True)
        (self.repository / PREFIX).symlink_to(self.site, target_is_directory=True)
        git(self.repository, "add", ".")
        git(self.repository, "commit", "-m", "Symlink fixture")
        with self.assertRaisesRegex(RuntimeError, "real directory"):
            stage_preview(self.site, self.repository, "abc123")

    def test_rejects_source_symlink(self):
        (self.site / "link").symlink_to(self.repository / "index.html")
        with self.assertRaisesRegex(RuntimeError, "symlinks"):
            stage_preview(self.site, self.repository, "abc123")

    def test_non_fast_forward_push_preserves_newer_production(self):
        remote = self.root / "remote.git"
        git(self.repository, "clone", "--bare", str(self.repository), str(remote))
        git(self.repository, "remote", "add", "origin", str(remote))
        concurrent = self.root / "concurrent"
        git(self.repository, "clone", str(remote), str(concurrent))
        git(concurrent, "config", "user.name", "Test")
        git(concurrent, "config", "user.email", "test@example.com")
        (concurrent / "index.html").write_text("New production")
        git(concurrent, "commit", "-am", "Concurrent production")
        git(concurrent, "push", "origin", "main")
        stage_preview(self.site, self.repository, "abc123")
        git(self.repository, "commit", "-m", "Preview")
        with self.assertRaises(subprocess.CalledProcessError):
            git(self.repository, "push", "origin", "HEAD:refs/heads/main")
        self.assertEqual(git(remote, "show", "main:index.html"), "New production")


if __name__ == "__main__":
    unittest.main()
