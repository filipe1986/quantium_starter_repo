import pytest
from dash.testing.browser import Browser 

@pytest.fixture
def dash_app(dash_duo):
    return dash_duo

# test 1
def test_header_is_present(dash_duo, dash_app):
    app = import_app('pink_sales_chart')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert any(word in header.text for word in ['Pink', 'Morsel', 'Sales'])

# test 2
def test_visualization_is_present(dash_duo):
    app = import_app('pink_sales_chart')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales_line_chart", timeout=10)
    assert dash_duo.find_element("#sales_line_chart") is not None

# test 3
def test_region_picker_is_present(dash_duo):
    app = import_app('pink_sales_chart')
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_filter", timeout=10)
    assert dash_duo.find_element("#region_filter") is not None


