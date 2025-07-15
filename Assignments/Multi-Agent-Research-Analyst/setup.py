from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:
    """
    Returns a list of requirements from requirements.txt,
    ignoring empty lines and editable installs.
    """
    try:
        with open('requirements.txt', 'r') as file:
            # Use a list comprehension for concise filtering and stripping
            return [
                line.strip()
                for line in file
                if line.strip() and line.strip() != '-e .'
            ]
    except FileNotFoundError:
        print("requirements.txt file not found.")
        return []

setup(
    name="Multi-Agent-2-Agent_Analyst",
    version="0.0.1",
    author="V Ratn",
    author_email="vratn@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)