from distutils.core import setup

setup(
    name = 'CreditChecker',
    version = '0.1',
    description = """The aim of this python library is to be able to return the
        available credit of a mobile carrier that has a website providing this information.""",
    author = 'Andrea Grandi',
    author_email = 'a.grandi@gmail.com',
    url = 'http://code.google.com/p/creditchecker',
    license = 'LGPL',
    packages = ['creditchecker', ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: by End-User Class :: Advanced End Users",
        "Programming Language :: Python",
        ],
    )
