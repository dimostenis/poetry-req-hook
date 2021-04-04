from setuptools import find_packages, setup

setup(
    name="pyproject-to-requirements-hook",
    version="0.2.4",
    install_requires=["poetry"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyproject-to-requirements = pre_commit_hooks.check_req_is_synced:main"
        ]
    },
)
