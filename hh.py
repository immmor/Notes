from tools import claudeAI, get_json_data, write_json_data
import ast

content = get_json_data('hh.txt')
eval(content)
# code = ast.literal_eval(content)
# exec(compile(code, filename='', mode='exec'))