from invoke import task


@task
def clean(context):
    context.run('rm -rf build/')
    context.run('rm -rf dist/')
    context.run('rm -rf *.egg-info/')


@task
def build(context, clean=False):
    context.run('python setup.py sdist')
    context.run('python setup.py bdist_wheel')


@task(pre=[build])
def register(context):
    name = '{{ cookiecutter.package_name }}-{{ cookiecutter.version }}'
    context.run('twine register dist/{0}.tar.gz'.format(name))
    context.run('twine register dist/{0}-py3-none-any.whl'.format(name))


@task
def upload(context):
    context.run('twine upload dist/*')
