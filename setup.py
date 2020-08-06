# Use this command for deploy.
#   python3 setup.py sdist bdist_wheel
#   python3 -m twine upload --skip-existing dist/*

from setuptools import find_packages, setup

setup(name='dynamo_dictionary',
      version='0.1',
      description='Easily Use DynamoDB as a key-value format.',
      long_description="Please refer to the https://github.com/da-huin/dynamo_dictionary",
      long_description_content_type="text/markdown",
      url='https://github.com/da-huin/dynamo_dictionary',
      download_url= 'https://github.com/da-huin/dynamo_dictionary/archive/master.zip',
      author='JunYeong Park',
      author_email='dahuin000@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
    ]
)
