from distutils.core import setup

setup(
    name = 'mmx_legacy_info',
    packages = ['mmx_legacy_info'],
    version = '0.1',
    description = 'Data extraction utility for Might and Magic X - Legacy',
    author='David Zerrenner',
    author_email='dazer@bluenode.de',
    url='https://github.com/dzerrenner/mmx_legacy_info',
    requires=[
        'xmldict (>=0.8.6)',
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "Environment :: Other Environment",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Games/Entertainment",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],


)