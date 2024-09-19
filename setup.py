from setuptools import setup,find_packages

with open("README.md", "r", encoding="UTF-8") as f:
    
    readme_content = f.read()
    
    
    __version__="0.0.0"
    
    REPO_Name="Covid19_classiciation"
    AUTHOR_USER_NAME="peetlasriram"
    AUTHOR_email="peetlasriramulu40@gmail.com"
    SRC_PEPO="Classification"
    
setup(
    name=SRC_PEPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_email,
    description="A small python package for NLP app",
    long_description=readme_content,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
  )