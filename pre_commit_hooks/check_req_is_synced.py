import argparse
import io
from pathlib import Path
from typing import Optional
from typing import Sequence

from poetry.factory import Factory
from poetry.utils.exporter import Exporter


def main(argv: Optional[Sequence[str]] = None) -> int:

    # args mimic poetry export
    # https://python-poetry.org/docs/cli/#export

    REQUIREMENTS_DEFAULT = "requirements.txt"

    parser = argparse.ArgumentParser()
    parser.add_argument("pyprojects", nargs="*")  # pyproject.toml
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Include development dependencies.",
    )
    parser.add_argument(
        "-e",
        "--extras",
        action="append",
        help="Extra sets of dependencies to include.",
    )
    parser.add_argument(
        "--without-hashes",
        action="store_true",
        help="Exclude hashes from the exported file.",
    )
    parser.add_argument(
        "--with-credentials",
        action="store_true",
        help="Include credentials for extra indices.",
    )
    parser.add_argument(
        "--requirements-path",
        help="Path to requirements.txt.",
        nargs="?",
        default=REQUIREMENTS_DEFAULT,
    )
    args = parser.parse_args(argv)

    msg = f"Exactly 1 pyproject.toml is allowed. Found {args.pyprojects}. Exit."
    assert len(args.pyprojects) == 1, msg

    homedir: str = str(Path(args.pyprojects[0]).absolute().parent)
    p = Path(args.requirements_path)

    poetry = Factory().create_poetry(homedir)
    exporter = Exporter(poetry)
    with io.StringIO() as req_io:
        exporter.export(
            fmt="requirements.txt",
            cwd=homedir,
            output=req_io,
            with_hashes=not args.without_hashes,
            dev=args.dev,
            extras=args.extras,
            with_credentials=args.with_credentials,
        )
        req_io.seek(0)
        new_requirements = req_io.read()

    old_requirements = ""
    if p.exists():
        old_requirements = p.read_text()

    retval = 0
    if new_requirements != old_requirements:
        p.write_text(new_requirements)
        retval = 1

    return retval


if __name__ == "__main__":
    exit(main())
