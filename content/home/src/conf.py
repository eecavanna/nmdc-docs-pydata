# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# -- Project information -----------------------------------------------------

# The name of the _documented_ project.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-project
project = 'NMDC'

copyright = '2025, National Microbiome Data Collaborative'
author = 'National Microbiome Data Collaborative'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_markdown_tables',
    'sphinx_reredirects',
    'notfound.extension',
    'sphinxcontrib.googleanalytics',
]

# source_suffix = '.rst'
source_suffix = ['.rst', '.md']
# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# The string you want Sphinx to append to the HTML `<title> tag of each page.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_title
html_title = 'NMDC Documentation'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# The path to the logo we want to use for the documentation website.
# Note: This path is relative to the directory containing the `conf.py` file.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_logo
html_logo = "_static/images/nmdc-logo-bg-white.png"

# Register a custom favicon for the website.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_favicon
html_favicon = "_static/favicon.ico"

# Register a custom JavaScript script for the website to load.
# Note: These paths are relative to the `{html_static_path}` directory.
# Reference: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files
html_js_files = [
    "js/index.js"
]

# -- Redirects ------------------------------------------

# Redirect old schema documentation URLs to the schema documentation
# that is automatically kept in sync with the schema. Also, redirect
# some specific local HTML file paths to subdirectory paths (in order
# to work around a limitation of Sphinx regarding `toctree` links).
# Also, redirect URLs of obsolete pages to the URLs of their modern
# counterparts.
# Reference: https://pypi.org/project/sphinx-reredirects/
redirects = {
    "runtime.html": "/runtime/",
    "workflows.html": "/workflows/",
    "reference/combined_workflow_docs": "/workflows/",
    "reference/metadata/xylene": "https://w3id.org/nmdc/xylene",  # the latter redirects to: https://microbiomedata.github.io/nmdc-schema/xylene/
    "reference/metadata/*": "https://w3id.org/nmdc/nmdc",
}

# -- Sphinx Not Found Page extension --------------------
#
# Reference: https://sphinx-notfound-page.readthedocs.io/en/latest/configuration.html
#
notfound_urls_prefix = None
notfound_context = {
    "title": "Page Not Found",
    "body": "<h1>Page Not Found</h1>\n\nWe failed to find a page at that address.",
}

# -- Sphinx Read The Docs Theme -------------------------
#
# Configure "Edit on GitHub" links.
# Reference: https://docs.readthedocs.io/en/stable/guides/edit-source-links-sphinx.html#github
html_context = {
    "display_github": True,
    "github_user": "microbiomedata",
    "github_repo": "docs",
    "github_version": "main",
    "conf_py_path": "/content/home/src/",  # path to directory containing `conf.py` file
}

# -- Sphinx Google Analytics extension --------------------
#
# Reference: https://pypi.org/project/sphinxcontrib-googleanalytics/
#
googleanalytics_id: str = "G-VH6HKVLCWN"
googleanalytics_enabled: bool = True

# -- PyData theme for Sphinx ------------------------------
#
# References:
# - https://pydata-sphinx-theme.readthedocs.io
# - https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#built-in-components-to-insert-into-sections
#
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/microbiomedata",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
        # {
        #     # Note: The FontAwesome website does list an icon called `fa-square-bluesky`,
        #     #       but this PyData website does not render it. I suspect the FontAwesome version
        #     #       being used by the PyData website is slightly out of date.
        #     #       Reference: https://fontawesome.com/icons/square-bluesky?f=brands&s=solid
        #     "name": "Bluesky",
        #     "url": "https://bsky.app/profile/microbiomedata.org",
        #     "icon": "_static/images/square-bluesky-brands-solid.svg",
        #     "type": "local",
        # },
        {
            "name": "Instagram",
            "url": "https://www.instagram.com/microbiomedata",
            "icon": "fa-brands fa-square-instagram",
            "type": "fontawesome",
        },
        {
            "name": "YouTube",
            "url": "https://www.youtube.com/channel/UCyBqKc46NQZ_YgZlKGYegIw/featured",
            "icon": "fa-brands fa-square-youtube",
            "type": "fontawesome",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/company/microbiomedata/",
            "icon": "fa-brands fa-linkedin",
            "type": "fontawesome",
        },
        {
            "name": "Twitter/X",
            "url": "https://twitter.com/microbiomedata",
            "icon": "fa-brands fa-square-x-twitter",
            "type": "fontawesome",
        },
    ],
    "external_links": [
        {"name": "NMDC Website", "url": "https://microbiomedata.org"},
    ],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "use_edit_page_button": True,
    "navigation_depth": 3,
    "show_nav_level": 3,
}
html_sidebars = {
    "**": ["sidebar-nav-bs"],
    # "index": ["navbar-nav"],
}
