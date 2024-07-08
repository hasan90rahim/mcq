from setuptools import find_packages,setup
setup(name="mcq_gen",version='0.0.1',author="hasan",author_email="hasanhelllo@gmail.com",
      install_requires=["langchain","streamlit","python-dotenv","PyPDF2","google-generativeai","ipykernel"],
      packages=find_packages())