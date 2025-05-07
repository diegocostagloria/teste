from jinja2 import Environment, FileSystemLoader

def generate_buildspec(language, config):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(f"{language}_buildspec.yml.j2")
    return template.render(config=config)
