from setuptools import setup, find_packages

VERSION = '0.4.0'


setup(
    name="mkdocs-bootswatch",
    version=VERSION,
    url='http://www.mkdocs.org',
    license='BSD',
    description='Bootswatch themes for MkDocs',
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'cerulean = mkdocs_bootswatch.cerulean',
            'cosmo = mkdocs_bootswatch.cosmo',
            'cyborg = mkdocs_bootswatch.cyborg',
            'darkly = mkdocs_bootswatch.darkly',
            'flatly = mkdocs_bootswatch.flatly',
            'journal = mkdocs_bootswatch.journal',
            'lumen = mkdocs_bootswatch.lumen',
            'paper = mkdocs_bootswatch.paper',
            'readable = mkdocs_bootswatch.readable',
            'sandstone = mkdocs_bootswatch.sandstone',
            'simplex = mkdocs_bootswatch.simplex',
            'slate = mkdocs_bootswatch.slate',
            'spacelab = mkdocs_bootswatch.spacelab',
            'superhero = mkdocs_bootswatch.superhero',
            'united = mkdocs_bootswatch.united',
            'yeti = mkdocs_bootswatch.yeti',
        ]
    },
    zip_safe=False
)
