import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="mfreport",
    author="Nobuhiro MIKI",
    author_email="nob@bobuhiro11.net",
    license="MIT",
    description="mfreport",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobuhiro11/mfreport",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "mfreport = mfreport.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    use_scm_version=True,
    install_requires=required,
    setup_requires=["setuptools_scm"],
)
