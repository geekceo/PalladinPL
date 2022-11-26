import libs.iostream

class Throw:
    def __init__(self, file: str, line_num: str, line_content:str):
        self.file = file
        self.line_num = line_num
        self.line_content = line_content

    def exception(self, namespace:str, exc_type=str):
        libs.iostream.output('Error occurred:')
        libs.iostream.output(f'{" "*4}File \'{self.file}\', line {self.line_num} in {namespace}')
        libs.iostream.output(f'{" "*8}{self.line_content}')
        libs.iostream.output(f'{exc_type}')
