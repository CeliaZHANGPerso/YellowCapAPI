import setuptools

setuptools.setup(
    name='yellowcab',
    version='1.0.0',
    author='my_email@email.com',
    description='yellowcab prediction with API',
    packages=setuptools.find_packages(),
    install_requires=[
        "scikit-learn",
        "pandas",
        "fastapi",
        "uvicorn",
        "pydantic",
    ]
)