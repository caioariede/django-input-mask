from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES


VERSION = '1.3.6'


# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-input-mask',
    version=VERSION,
    description="JavaScript input masks for Django",
    long_description=open('README.rst', 'r').read(),
    author="Caio Ariede",
    author_email="caio.ariede@gmail.com",
    url="http://github.com/caioariede/django-input-mask",
    license="MIT",
    platforms=["any"],
    packages=[
        'input_mask',
        'input_mask.contrib',
        'input_mask.contrib.localflavor',
        'input_mask.contrib.localflavor.br',
        'input_mask.contrib.localflavor.us',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Framework :: Django",
        "Topic :: Utilities",
    ],
)
