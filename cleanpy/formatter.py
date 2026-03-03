import re

def simple_format(code: str) -> str:
    code = re.sub(', (\\S)', ', \\1', code)
    code = re.sub('(\\S) = (\\S)', '\\1 = \\2', code)
    code = re.sub('(\\S)\\ + (\\S)', '\\1 + \\2', code)
    return code