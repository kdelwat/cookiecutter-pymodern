from invoke import task


@task
def clean(context):
    context.run('rm -rf **/*.pyc')
    context.run('rm -rf **/__pycache__/')
    context.run('rm -rf build/')
    context.run('rm -rf dist/')
    context.run('rm -rf *.egg-info/')


@task(pre=[clean])
def build(context):
    context.run('python setup.py sdist')
    context.run('python setup.py bdist_wheel')


@task(pre=[build])
def register(context):
    name = '{{ cookiecutter.package_name }}-{{ cookiecutter.version }}'
    context.run('twine register dist/{0}.tar.gz'.format(name))
    context.run('twine register dist/{0}-py3-none-any.whl'.format(name))


@task
def deploy(context):
    context.run('twine upload dist/*')
