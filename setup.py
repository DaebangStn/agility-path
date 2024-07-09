from setuptools import find_packages, setup

setup(
    name="agility_path",
    version="0.1",
    description="Dog Agility Path Planning Environment.",
    author="Geonho Leem",
    author_email="geonholeem@imo.snu.ac.kr",
    install_requires=[
        "matplotlib",
    ],
    packages=find_packages(include=["agility_path*"], exclude=[]),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
