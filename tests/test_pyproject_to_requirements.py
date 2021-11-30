from pathlib import Path

import pytest

from pre_commit_hooks.pyproject_to_requirements import main
from testing.util import get_resource_path


def test_using_multiple_pyprojects():
    """This FAILS with AssertionError, coz only 1 "pyproject.toml" is allowed."""

    with pytest.raises(AssertionError):
        main(
            [
                get_resource_path("foo/pyproject.toml"),
                get_resource_path("bar/pyproject.toml"),
            ]
        )


def test_using_custom_requirements():
    directory = "pass_custom_reqs"
    ret = main(
        [
            get_resource_path(f"{directory}/pyproject.toml"),
            "--without-hashes",
            "--dev",
            "--requirements-path",
            get_resource_path(f"{directory}/requirements-dev.txt"),
        ]
    )
    assert ret == 0


def test_using_default_requirements():
    directory = "pass_default_reqs"
    ret = main(
        [
            get_resource_path(f"{directory}/pyproject.toml"),
            "--without-hashes",
            "--dev",
            "--requirements-path",
            get_resource_path(f"{directory}/requirements.txt"),
        ]
    )
    assert ret == 0


def test_missing_requirements():
    """This test fails coz there is no requirements.txt file - must be generated."""
    directory = "fail_no_reqs"
    try:
        ret = main(
            [
                get_resource_path(f"{directory}/pyproject.toml"),
                "--without-hashes",
                "--requirements-path",
                get_resource_path(f"{directory}/requirements.txt"),
            ]
        )
    finally:
        # cleanup
        p = Path(directory) / "requirements.txt"
        p = Path(get_resource_path(str(p)))
        if p.exists():
            p.unlink()
    assert ret == 1
