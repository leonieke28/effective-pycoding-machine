import textwrap
import itertools

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""
    paragraphs = text.split("\n\n")
    columns = [textwrap.wrap(paragraph, COL_WIDTH) for paragraph in paragraphs]
    lines = list(itertools.zip_longest(*columns, fillvalue=""))
    formatted_lines = ["\t".join([f"{column:20}" for column in line]) for line in lines]
    result = "\n".join(formatted_lines)
    return result
