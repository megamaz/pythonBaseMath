from pathlib import Path
from setuptools import find_packages, setup

here = Path(__file__).parents[0]

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="BaseMath",
    version="1.1.0",
    license='MIT license',
    description="Allows you to do math in any base.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/megamaz/pythonBaseMath',
    author='megamaz',
    author_email="raphael.mazuel@gmail.com",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='Beat Saber, Noodle Extensions',
    packages=find_packages(),
    python_requires='>=3.8, <4',
    project_urls={
        'Bug Reports': 'https://github.com/megamaz/pythonBaseMath/issues'
    },
    install_requires=["numpy"]
)