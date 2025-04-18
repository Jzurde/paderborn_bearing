import setuptools

from os import path

setuptools.setup(
    name="paderborn_bearing",
    version="0.2.1",
    author="Jurgen van den Hoogen",
    author_email="jurgenvandenhoogen@hotmail.com",
    description='Preprocessed Paderborn Bearing Dataset for analysing multivariate motor current signals combined with a vibration signal. Please notice that this version is only suited for computers running on Mac OS.',
    long_description_content_type='text/markdown',
    url='https://github.com/JvdHoogen/paderborn_bearing',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.9',
    include_package_data=True
)




