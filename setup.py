import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Questrade-API-Wrapper',
    version='1.0.0',
    description='Questrade API Wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vashista1/Questrade_API_wrapper',
    author='Vashista Gande',
    author_email='',
    license='MIT',
    packages=setuptools.find_packages(),
    package_data={
        'src': ['questrade-api.cfg'],
    },
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)