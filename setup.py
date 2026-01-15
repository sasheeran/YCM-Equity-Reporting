from setuptools import setup, find_packages

setup(
    name="ycm-equity-reporting",
    version="0.1.0",
    author="Sam",
    author_email="ssheeran@yousifcapital.com",
    description="Portfolio analysis and reporting tools for equity strategies",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=2.2.0,<3.0.0",
        "numpy>=1.26.0,<2.0.0",
        "openpyxl>=3.1.2,<4.0.0",
        "requests>=2.31.0,<3.0.0",
        "python-dotenv>=1.0.0,<2.0.0",
        "jupyter>=1.0.0,<2.0.0",
        "matplotlib>=3.8.0,<4.0.0",
        "seaborn>=0.13.0,<1.0.0",
    ],
    python_requires=">=3.9",
)