import setuptools


with open('README.md') as f:
    README = f.read()

REQUIREMENTS = ['numpy', 'pandas', 'beautifulsoup4', 'imdbpy', 'lxml', 'tweepy', 'kafka',
                'pymongo', 'pprint', 'contractions', 'inflect', 'ntlk', 'google-cloud-language',
                'html5lib']

setuptools.setup(
    author="Federico De Servi, Alessandro Pontini",
    author_email="federico@federicodeservi.com",
    name='mtsb-analyzer',
    license="MIT",
    description='Python library that collects tweets about movies, performs a sentiment analysis and correlates it with the boxoffice result of the week after the movie release.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/federicodeservi/mtsb-analyzer',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires= REQUIREMENTS,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)