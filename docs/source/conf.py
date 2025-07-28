# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RosettaMPNN'
copyright = '2025, Justas Dauparas, Ivan Anishchenko, Nate Bennett, Hua Bai, Robert Ragotte, Lukas F. Miles, Basile I. M. Wicky, Alexis Courbet, Robbert Jan de Haas, Neville Bethel, Phlip J. Y. Leung, Timothy F. Huddy, Sam Pellock, Doug Tischer, Federick Chan, Hannah Nguyen, Alex Kang, Banumathi Sankaran, Brian Koepnick, Asim Bera, Neil King, David Baker, Gyu Rie Lee, Robert Pecoraro, Linna An, Cameron Glasscock, Moritz Ertelt, Phillip Schlegel, Max Beining, Leonard Kaysser, Jens Meiler, Clara T. Schoeder'
author = 'Justas Dauparas, Ivan Anishchenko, Nate Bennett, Hua Bai, Robert Ragotte, Lukas F. Miles, Basile I. M. Wicky, Alexis Courbet, Robbert Jan de Haas, Neville Bethel, Phlip J. Y. Leung, Timothy F. Huddy, Sam Pellock, Doug Tischer, Federick Chan, Hannah Nguyen, Alex Kang, Banumathi Sankaran, Brian Koepnick, Asim Bera, Neil King, David Baker, Gyu Rie Lee, Robert Pecoraro, Linna An, Cameron Glasscock, Moritz Ertelt, Phillip Schlegel, Max Beining, Leonard Kaysser, Jens Meiler, Clara T. Schoeder'
release = 'v1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    "sidebar_hide_name":True,
    "top_of_page_buttons": ["edit"],
    ""
    "announcement": "<em>THIS DOCUMENTATION IS CURRENTLY UNDER CONSTRUCTION</em>",
    "light_css_variables": {
        "color-brand-primary": "#F68A33", # Rosetta Teal
        "color-brand-content": "#37939B", # Rosetta Orange
        "color-admonition-background": "#FB35D6", # Rosetta light orange
        "font-stack": "Open Sans, sans-serif",
        "font-stack--headings": "Open Sans, sans-serif",
        "color-background-hover": "#DCE8E8ff",
        "color-announcement-background" : "#F68A33dd",
        "color-announcement-text": "#070707",
        "color-brand-visited": "#37939B",
        },
    "dark_css_variables": {
        "color-brand-primary": "#37939B", # Rosetta teal
        "color-brand-content": "#F68A33", # Rosetta orange
        "color-admonition-background": "#FB35D6", # Rosetta light orange
        "font-stack": "Open Sans, sans-serif",
        "font-stack--headings": "Open Sans, sans-serif",
        "color-brand-visited": "#37939B",
        }
    }
html_static_path = ['_static']
#html_css_files = ['custom.css']
