import hashlib
import jinja2
import os
from jinja2 import Template

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

def generate_card(student,cpf):
    hash_string = str(student) + "-" + str(cpf)
    hash = str(hashlib.sha1(hash_string.encode()).hexdigest())

    card_template = latex_jinja_env.get_template("Carteirinha_Template.tex")
    card = card_template.render(
        NOME=student,
        CPF=cpf,
        HASH=hash
    )

    return card, hash
