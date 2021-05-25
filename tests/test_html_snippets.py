from unittest import TestCase

import jinja2
from ddt import ddt, data, unpack
from jinja2 import Environment, select_autoescape
import templates
from html_utilities import minimise_html

table_data = [
    {
        'fields': ['field1', 'field2', 'field3'],
        'values': [
            ('row1 value1', 'row1 value2', 'row1 value3'),
            ('row2 value1', 'row2 value2', 'row2 value3'),
            ('row3 value1', 'row3 value2', 'row3 value3')
        ],
        'html':
            "<table>" +
            "<tr><th>field1</th><th>field2</th><th>field3</th></tr>" +
            "<tr><td>row1 value1</td><td>row1 value2</td><td>row1 value3</td></tr>" +
            "<tr><td>row2 value1</td><td>row2 value2</td><td>row2 value3</td></tr>" +
            "<tr><td>row3 value1</td><td>row3 value2</td><td>row3 value3</td></tr>" +
            "</table>"
    }
]


@ddt
class TestHtmlSnippets(TestCase):

    @data(*table_data)
    @unpack
    def test_table(self, fields, values, html):
        env = Environment(
            loader=jinja2.FileSystemLoader(next(iter(templates.__path__))),
            autoescape=select_autoescape(['html', 'xml'])
        )

        template = env.get_template('table.html')

        actual_html = template.render(field_names=fields, rows=values)

        self.assertEqual(minimise_html(html), minimise_html(actual_html))
