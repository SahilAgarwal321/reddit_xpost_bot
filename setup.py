from setuptools import setup


setup(name='reddit_xpost_bot',
      version='1.0',
      description='Checks if crossposts exist and tells',
      author='Sahil Agarwal',
      author_email='sahil.agarwal94@gmail.com',
      keywords='reddit xpost crosspost bot',
      # url='',
      license='MIT',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Logging Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],

      packages=find_packages(),
      )
