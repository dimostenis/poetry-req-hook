from pathlib import Path

import pytest

from pre_commit_hooks.check_req_is_synced import main
from testing.util import get_resource_path


def test_using_custom_pyproject():
    """ This FAILS with AssertionError, coz only "pyproject.toml" is allowed. """

    directory = "pass_custom_reqs"
    with pytest.raises(AssertionError):
        main(
            [
                "--pyproject-path",
                get_resource_path(f"{directory}/custom-pyproject.toml"),
            ]
        )


def test_using_custom_requirements():
    directory = "pass_custom_reqs"
    ret = main(
        [
            "--without-hashes",
            "--dev",
            "--pyproject-path",
            get_resource_path(f"{directory}/pyproject.toml"),
            "--requirements-path",
            get_resource_path(f"{directory}/requirements-dev.txt"),
        ]
    )
    assert ret == 0


def test_using_default_requirements():
    directory = "pass_default_reqs"
    ret = main(
        [
            "--without-hashes",
            "--dev",
            "--pyproject-path",
            get_resource_path(f"{directory}/pyproject.toml"),
            "--requirements-path",
            get_resource_path(f"{directory}/requirements.txt"),
        ]
    )
    assert ret == 0


def test_missing_requirements():
    """ This test fails coz there is no requirements.txt file - must be generated. """
    directory = "fail_no_reqs"
    try:
        ret = main(
            [
                "--without-hashes",
                "--pyproject-path",
                get_resource_path(f"{directory}/pyproject.toml"),
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
