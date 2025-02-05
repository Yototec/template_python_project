# Copyright (c) 2018-2025 Yototec Ltd

import sys
import platform
from setuptools import find_packages, setup


if platform.system() != "Windows" and (
    not hasattr(sys, "base_prefix") or sys.base_prefix == sys.prefix
):
    print("ERROR: This is not production software, install inside a venv")
    sys.exit(1)

install_requires = [
    "numpy==1.24.3",
    "pandas==1.4.2",
    "matplotlib==3.5.1",
    "matplotlib-inline==0.1.3",
]

extras_require = {
    "tests": ["coverage", "papermill==2.3.4"],
    "notebooks": [
        "ipykernel==6.7.0",
        "notebook==6.4.7",
        "jupyterlab==3.2.8",
        "nbconvert==6.5.0",
        "ipython-autotime==0.3.1",
    ],
    "dev-tools": [
        "isort==5.9.1",
        "pylint==2.9.0",
        "flake8==4.0.1",
        "mypy==1.2",
    ],
}

extras_require["dev"] = list(
    {req for _, reqs in extras_require.items() for req in reqs}
)

setup(
    name="project_name",
    version="0.1",
    description="Project Name",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
)
