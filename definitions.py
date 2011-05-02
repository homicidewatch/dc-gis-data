"""
Configuration describing the shapefiles to be loaded.
"""
import re
from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

def district_normalizer(name):
    """
    Police district names are formatted like as "Third_District",
    so we need to get just the first part of that.
    """
    if "_" in name:
        return name.split('_')[0]
    else:
        return name

# This SHAPEFILES dictionary is a sample. You should delete (or comment out)
# the first entry if you don't care about neighborhoods in Chicago.
SHAPEFILES = {

    'Wards': {
        'file': 'Ward02Ply/Ward02Ply.shp',
        'singular': 'Ward',
        'kind_first': True,
        'ider': utils.simple_namer(['WARD_ID']),
        'namer': utils.simple_namer(['WARD_ID']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=126',
        'notes': '',
        'encoding': '',
    },
    
    'Neighborhood Clusters': {
        'file': 'NbhClusPly/NbhClusPly.shp',
        'singular': 'Neighborhood Cluster',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NBH_NAMES']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=163',
        'notes': '',
        'encoding': '',
    },
    
    'ANC Districts': {
        'file': 'ANC02Ply/ANC02Ply.shp',
        'singular': 'ANC District',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['ANC_ID']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=148',
        'notes': '',
        'encoding': '',
    },
    
    'Quadrants': {
        'file': 'DcQuadPly/DcQuadPly.shp',
        'singular': 'Quadrant',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=83',
        'notes': '',
        'encoding': '',
    },
    
    'Census Block Groups': {
        'file': 'BlockGroupPly/BlockGroupPly.shp',
        'singular': 'Census Block Group',
        'kind_first': True,
        'ider': utils.simple_namer(['BLKGRP']),
        'namer': utils.simple_namer(['BLKGRP']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=302',
        'notes': '',
        'encoding': '',
    },
    
    'Census Tracts': {
        'file': 'TractPly/TractPly.shp',
        'singular': 'Census Tract',
        'kind_first': True,
        'ider': utils.simple_namer(['TRACT']),
        'namer': utils.simple_namer(['TRACT']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=119',
        'notes': '',
        'encoding': '',
    },
    
    'Elementary School Attendance Zones': {
        'file': 'ESBndyPly/ESBndyPly.shp',
        'singular': 'Elementary School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=180',
        'notes': '',
        'encoding': '',
    },
    
    'Middle School Attendance Zones': {
        'file': 'MSBndyPly/MSBndyPly.shp',
        'singular': 'Middle School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=181',
        'notes': '',
        'encoding': '',
    },
    
    'Senior High School Attendance Zones': {
        'file': 'SHSBndyPly/SHSBndyPly.shp',
        'singular': 'Senior High School Attendance Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOLNAME']),
        'namer': utils.simple_namer(['SCHOOLNAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 28),
        'href': 'http://data.dc.gov/Metadata.aspx?id=63',
        'notes': '',
        'encoding': '',
    },
    
    'Police Districts': {
        'file': 'PolDistPly/PolDistPly.shp',
        'singular': 'District',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME'], normalizer=district_normalizer),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=187',
        'notes': '',
        'encoding': '',
    },
    
    'Police Service Areas': {
        'file': 'PolSAPly/PolSAPly.shp',
        'singular': 'Police Service Area',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=120',
        'notes': '',
        'encoding': '',
    },
    
    'Zip Codes': {
        'file': 'ZipCodePly/ZipCodePly.shp',
        'singular': 'Zip Code',
        'kind_first': True,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['ZIPCODE']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 3, 1),
        'href': 'http://data.dc.gov/Metadata.aspx?id=130',
        'notes': '',
        'encoding': '',
    }
    
}
