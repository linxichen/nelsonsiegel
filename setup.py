from setuptools import setup

setup(name='nelsonsiegel',
        version='0.1.1',
        description='Suites for Nelson-Siegel style yield curve fitting.',
        url='http://github.com/linxichen/nelsonsiegel',
        author='Linxi Chen',
        author_email='linxichen88@gmail.com',
        license='GPL v3',
        packages=['nelsonsiegel'],
        install_requires=[
            'numpy',
            'pandas',
            'scikit-learn',
            ],
        test_suite='nose.collector',
        tests_require=['nose'],
        include_package_data=True,
        zip_safe=False)

