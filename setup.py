from setuptools import setup, find_packages
import pathlib
import numpy as np

cwd = pathlib.Path("./")
src = cwd / "src"
packages = find_packages(str(src))
modules = sorted([str(f.relative_to(f.parts[0])) for f in src.glob("**/[:alpha:]*.py")])

setup(
    name="get_jasmin_era5",
    version="0.1.0",
    description="A small python package to find and load ECMWF ERA5 data from the BADC archive on jasmin",
    url="",
    author="William Jones",
    author_email="william.jones@physics.ox.ac.uk",
    license="BSD-3",
    packages=packages,
    package_dir={"": "src"},
    # py_modules=modules,
    include_package_data=True,
    install_requires=["numpy", "pandas", "xarray"],
    include_dirs=[np.get_include()],
    zip_safe=False,
)
