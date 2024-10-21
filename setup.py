from setuptools import setup, find_packages

setup(
    name='telegram-log-sender',
    version='0.1.0',
    author='Denis Ustinov',
    author_email='revers-06-checkup@icloud.com',
    description='A Python package for sending logs to a Telegram bot with filtering capabilities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DenisUstinov/telegram-log-sender',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests', 'retry'],
    python_requires='>=3.11',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)