# Sync `poetry` & `requirements` hook

---

**[?? OBSOLETE ??]**

Since `poetry` update `1.2.0`, there is a [built-in support for pre-commit export hook](https://python-poetry.org/docs/pre-commit-hooks/).


```yaml
# (copy from official docs)

repos:
  - repo: https://github.com/python-poetry/poetry
    rev: ''  # add version here
    hooks:
      - id: poetry-check
      - id: poetry-lock
      - id: poetry-export
        args: ["-f", "requirements.txt", "-o", "requirements.txt"]
```

However, theres an advantage of using our *old* hook, because `poetry`s native hook **depends on change of `poetry.lock`**, so if you have it in `.gitignore`, native hook will never work for you.

**Our hook depends on change of `pyproject.toml`**

So if you want same funcionality, add "files" to hook as follows and its done.

```yaml
repos:
  - repo: https://github.com/python-poetry/poetry
    rev: ''  # add version here
    hooks:
      - id: poetry-check
      - id: poetry-lock
      - id: poetry-export
        args: ["-f", "requirements.txt", "-o", "requirements.txt"]
        files: ^pyproject.toml$  # <------------------------------
```

---

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
    rev: 1.1.0
    hooks:
      - id: pyproject-to-requirements
```

Include dev deps under `requirements-dev.txt`

```yaml
- repo: https://github.com/dimostenis/poetry-req-hook
    rev: 1.1.0
    hooks:
      - id: pyproject-to-requirements
        args: [
            "--requirements-path", "requirements-dev.txt",
            "--dev"
            ]
```

Use custom location under `/app` dir.

```yaml
- repo: https://github.com/dimostenis/poetry-req-hook
    rev: 1.1.0
    hooks:
      - id: pyproject-to-requirements
        args: [
            "--requirements-path", "app/requirements.txt",
            "--dev"
            ]
```

## Note I.

Originaly forked from https://github.com/Diaoul/pre-commit-hooks-poetry.

## Note II.

`setup.py` along `pyproject.toml` in repo? Yes.

- `setup.py` is for `pre-commit` to correctly install executable.
- `pyproject.toml` for dev.
