from setuptools import setup, find_packages


VERSION = __import__('input_mask').__version__


setup(
    name='django-input-mask',
    version=VERSION,
    url='http://github.com/caioariede/django-input-mask',
    author='Caio Ariede',
    author_email='caio.ariede@gmail.com',
    description='JavaScript input masks for Django',
    license='MIT',
    platforms=['any'],
    packages=find_packages(),
    package_data={'input_mask': [
        'static/input_mask/js/*',
    ]},
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
    include_package_data=True,
    install_requires=[
        'Django>=1.6,<1.9',
        'six',
    ],
    test_suite="runtests.runtests",
)
