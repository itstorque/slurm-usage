from setuptools import setup

setup(
    name="slurm-usage",
    version="0.1",
    description="Command to list the current cluster usage per user.",
    url="https://github.com/basnijholt/slurm-usage",
    author="Bas Nijholt",
    license="MIT",
    py_modules=["slurm-usage"],
    entry_points={"console_scripts": ["slurm-usage=slurm-usage:main", "stats=slurm-usage:main"]},
)
