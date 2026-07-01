import pytest
from dash import Dash
import dash.html as html
import dash.dcc as dcc
from pink_sales_chart import app   # Import your main app

def test_app_can_be_imported():
    """Test 1: The app can be imported"""
    assert isinstance(app, Dash)


def test_header_is_present():
    """Test 2: Header (H1) is present"""
    assert any(
        isinstance(child, html.H1) or 
        (hasattr(child, 'children') and any(isinstance(c, html.H1) for c in child.children if hasattr(child, 'children')))
        for child in app.layout.children
    )


def test_visualisation_is_present():
    """Test 3: The graph is present"""
    graph_found = False
    for child in app.layout.children:
        if hasattr(child, 'children'):
            children = child.children if isinstance(child.children, list) else [child.children]
            for sub in children:
                if isinstance(sub, dcc.Graph):
                    graph_found = True
    assert graph_found, "Graph component not found in layout"


def test_region_picker_is_present():
    """Test 4: Region filter (RadioItems) is present"""
    picker_found = False
    for child in app.layout.children:
        if hasattr(child, 'children'):
            children = child.children if isinstance(child.children, list) else [child.children]
            for sub in children:
                if hasattr(sub, 'id') and sub.id == 'region_filter':
                    picker_found = True
    assert picker_found, "Region picker not found"

