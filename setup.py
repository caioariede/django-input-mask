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
    zip_safe=False,
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
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7,<1.9',
        'six',
    ],
    test_suite="runtests.runtests",
)
