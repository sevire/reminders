from functools import reduce
import htmlmin as htmlmin


def minimise_html(html_string):
    """
    To help in comparing actual and expected html strings, this function removes all whitespace and newlines
    from an html string.

    :param html_string:
    :return:
    """
    minified = htmlmin.minify(html_string, remove_all_empty_space=True)
    return minified


def table(headings, records):
    """
    Creates a table with a row of headings and then one row for each database record passed in.

    :param headings: List of field names to use as headers
    :param records: Iterable of database records with fields corresponding to field names in headers
    :return:
    """

    heading_html = '<tr>' + reduce(lambda header_html, item: header_html + f'<th>{item}</th>', headings, '') + '</tr>'

    html = '<table>'
    html += heading_html

    for record in records:
        row = '<tr>'
        for field_name in headings:
            field_value = getattr(record, field_name)
            field_html = f'<td>{field_value}</td>'
            row += field_html
        row += '</tr>'
        html += row

    html += '</table>'

    return html
