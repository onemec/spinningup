import sys
from os.path import join

from setuptools import setup

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, (
    "The Spinning Up repo is designed to work with Python 3.6 and greater."
    + "Please install it before proceeding."
)

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name="spinup",
    py_modules=["spinup"],
    version=__version__,
    install_requires=[
        "cloudpickle",
        "gymnasium[atari,box2d,classic_control]",
        "ipython",
        "joblib",
        "matplotlib",
        "mpi4py",
        "numpy",
        "pandas",
        "pytest",
        "pyglet",
        "psutil",
        "scipy",
        "seaborn",
        "tensorflow-macos",
        "tensorflow-metal",
        "torch",
        "tqdm",
    ],
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
