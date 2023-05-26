from setuptools import setup, find_packages
import pathlib
import numpy as np

cwd = pathlib.Path("./")
src = cwd / "src"
packages = find_packages(str(src))
modules = sorted([str(f.relative_to(f.parts[0])) for f in src.glob("**/[:alpha:]*.py")])

setup(
    name="tobac-flow",
    version="1.7.5",
    description="Detection and tracking of deep convective clouds in high time resolution geostationary satellite imagery",
    url="",
    author="William Jones",
    author_email="william.jones@physics.ox.ac.uk",
    license="BSD-3",
    packages=packages,
    package_dir={"": "src"},
    # py_modules=modules,
    include_package_data=True,
    install_requires=[],
    include_dirs=[np.get_include()],
    zip_safe=False,
)
