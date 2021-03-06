"""Function creates an astropy table containing information that is useful to
generate postage stamp images with appropriate distributions of shapes, colors,
fluxes, etc.
TODO:
1) Add script to load DC2 catalog
2) Add option to load multiple catlogs(eg star , galaxy)
"""
import os
import astropy.table


def load_catlog(Args):
    """Returns astropy table with catalog name from input class"""
    name, ext = os.path.splitext(Args.catalog_name)
    if ext == '.fits':
        table = astropy.table.Table.read(Args.catalog_name,
                                         format='fits')
    else:
        table = astropy.table.Table.read(Args.catalog_name,
                                         format='ascii.basic')
    if Args.verbose:
        print("Catalog loaded")
    return table
