import hashlib
import jinja2
import os

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

def generate_card(curso,student,matricula):
    hash_string = str(curso) + str(student) + str(matricula)
    hash = str(hashlib.sha1(hash_string.encode()).hexdigest())

    card_template = latex_jinja_env.get_template("Template_Carteirinha.tex")
    card = card_template.render(
        CURSO=curso,
        NOME=student,
        MATRICULA=matricula,
        HASH=hash
    )

    return card, hash
