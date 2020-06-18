import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="dns-catalog-hash-illallangi", # Replace with your own username
  version="0.0.1",
  author="Andrew Cole",
  author_email="andrew.cole@illallangi.com",
  description="A utility to calculate hashes for use in DNS Catalog Zones",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/illallangi/DNSCatalogHash",
  packages=setuptools.find_packages(),
  classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  entry_points = {
    'console_scripts': ['dns-catalog-hash=dns_catalog.dns_catalog_hash:main'],
  }
)