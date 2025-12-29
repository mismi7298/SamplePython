from setuptools import setup, find_packages

setup(
    name='sample_python',
    version='0.1.0',
    description='A sample python project for eicar test',
    author='Naresh Kumar',
    packages=["pkg"],
    include_package_data=True,
    package_data={
        "pkg": ["hello.txt"],
    },
    # Add other metadata like license, install_requires, etc. as needed
)
