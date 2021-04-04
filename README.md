# WIP: Sync `poetry` & `requirements` hook

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Keep `pyproject.toml` and `requirements.txt` in sync, whenever `pyproject.toml` changes.

## Arguments

- same as in https://python-poetry.org/docs/cli/#export
- `--requirements-path`
    - use custom `requirements.txt` instead of top level `./requirements.txt`
    - arg can be used to change name or dir. Or both
        - `--requirements-path reqs-dev.txt`
        - `--requirements-path docker/requirements.txt`
        - ...

## Examples

Basic usage

```yaml
- repo: https://github.com/dimostenis/poetry-req-hook
    rev: 0.2.1
    hooks:
      - id: check-req-is-synced
```

Include dev deps under `requirements-dev.txt`

```yaml
- repo: https://github.com/dimostenis/poetry-req-hook
    rev: 0.2.1
    hooks:
      - id: check-req-is-synced
        args: [
            "--requirements-path", "requirements-dev.txt",
            "--dev"
            ]
```

Use custom location under `/app` dir.

```yaml
- repo: https://github.com/dimostenis/poetry-req-hook
    rev: 0.2.1
    hooks:
      - id: check-req-is-synced
        args: [
            "--requirements-path", "app/requirements.txt",
            "--dev"
            ]
```

## Note I.

Originaly forked from https://github.com/Diaoul/pre-commit-hooks-poetry.

## Note II.

`setup.cfg` along `pyproject.toml` in repo? Yes.

- `setup.cfg` is for `pre-commit` to correctly install executable.
- `pyproject.toml` for dev
