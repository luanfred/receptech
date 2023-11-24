from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os

template_dir = Path(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
template_dir = os.path.join(template_dir.parent, 'templates')
env = Environment(loader=FileSystemLoader(f'{template_dir}/relatorio'))
confing = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.50in',
    'margin-bottom': '0.75in',
    'margin-left': '0.50in',
    'encoding': 'UTF-8',
    # 'orientation': 'Landscape',
}