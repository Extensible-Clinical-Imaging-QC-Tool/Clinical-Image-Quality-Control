#
# ciqc setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the pkmodel module.
    """
    from ciqc.version_info import VERSION as version
    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='ciqc',

    # Version
    version=get_version(),

    description='Clinical Image Quality Control Tool',

    long_description=get_readme(),

    license='MIT license',

    author=("Elliot Barbeary, "
            "Mona Furukawa, "
            "Hazel Wee Ling, "
            "Ian McFarlane, "
            "Oliver Turnbull"),

    author_email=("elliot.barbeary@dtc.ox.ac.uk, "
                  "mona.furukawa@dtc.ox.ac.uk, "
                  "hazel.wee@dtc.ox.ac.uk, "
                  "ian.mcfarlane@dtc.ox.ac.uk, "
                  "oliver.turnbull@dtc.ox.ac.uk"),

    maintainer='Elliot Barbeary',

    maintainer_email='elliot.barbeary@dtc.ox.ac.uk',

    url='https://github.com/ebarbeary/Clinical-Image-Quality-Control',

    # Packages to include
    packages=find_packages(include=('ciqc', 'ciqc.*')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
        'opencv-python',
        'pytesseract'
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3', 
            # Unittest for testing main codes: testsolution, testprotocol, testmodel.
            'unittest'
        ],
    },
)
