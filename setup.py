from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="0.1.0",
    description="A CLI Task Tracker",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="NguyenDong",
    author_email="doannguyendong1808@gmail.com",
    url="https://github.com/ndongdoan/task_trackerCLI",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "task=task_tracker.cli:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)