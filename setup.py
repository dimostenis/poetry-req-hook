from setuptools import find_packages, setup

setup(
    name="pyproject-to-requirements-hook",
    version="1.1.0",
    install_requires=["poetry<1.2.0"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pyproject-to-requirements = pre_commit_hooks.pyproject_to_requirements:main"
        ]
    },
)
