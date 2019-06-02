from setuptools import setup

from sec_edgar_downloader import __version__

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="sec-edgar-downloader",
    version=__version__,
    license="MIT",
    author="Jad Chaar",
    author_email="jad.chaar@gmail.com",
    description="Python package for downloading company filings from the SEC EDGAR database.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jadchaar/sec-edgar-downloader",
    packages=["sec_edgar_downloader"],
    zip_safe=False,
    install_requires=["lxml", "requests"],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sec edgar filing financial finance sec.gov",
    project_urls={
        "Bug Reports": "https://github.com/jadchaar/sec-edgar-downloader/issues",
        "Repository": "https://github.com/jadchaar/sec-edgar-downloader",
    },
)
