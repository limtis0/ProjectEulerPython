from pathlib import Path
from fileinput import FileInput
from re import search


''' Script, that recursively traverses through folders and stylizes .py scripts, according to config (View main) '''


class Style:
    """
    :param int dir_parent: from how many parent libraries start to traverse. (0 for this folder)
    :param bool quote_inverse: changes single-quotes to double- if set to True, else otherwise
    :param bool rm_end_spaces: whether to remove spaces from the end of the line
    :param bool inline_doc_spaces: whether to place spaces before and after triple quotes in inline documentation
    """
    def __init__(
            self, dir_parent: int,
            quote_inverse: bool,
            rm_end_spaces: bool,
            inline_doc_spaces: bool,
    ):
        # public
        self.parent_dir = self._get_nth_parent(dir_parent)

        # private
        self._quote_a, self._quote_b = ('\"', '\'') if not quote_inverse else ('\'', '\"')
        self._rm_end_spaces = rm_end_spaces
        self.inline_doc_spaces = inline_doc_spaces

    def format(self, line: str):
        line = line.replace(self._quote_a, self._quote_b)

        if self._rm_end_spaces:
            line = line.rstrip(' ')

        if self.inline_doc_spaces:
            triple_quote = self._quote_b*3
            if line.count(triple_quote) == 2:
                line = self._format_doc_spaces(triple_quote, line)

        return line

    @staticmethod
    def _format_doc_spaces(triple_quote, line):
        new_line = '\n' in line
        doc = search(triple_quote + r'(.*)' + triple_quote, line).group(1).strip(' ')
        line = f'{triple_quote} {doc} {triple_quote}'
        if new_line:
            line += '\n'
        return line

    @staticmethod
    def _get_nth_parent(n: int) -> Path:
        return Path(__file__).parents[n]


def traverse_folders(style: Style):
    file_path = Path(__file__)
    for script_path in style.parent_dir.rglob('*.py'):
        if script_path != file_path:
            for line in FileInput(script_path, inplace=True):
                line = style.format(line)
                print(line, end='')


if __name__ == '__main__':
    config = Style(
        dir_parent=1,
        quote_inverse=False,
        rm_end_spaces=True,
        inline_doc_spaces=True,
    )

    print('Executing...')
    traverse_folders(config)
    print('Script executed successfully')
