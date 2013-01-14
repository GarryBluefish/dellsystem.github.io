from fabric.api import local, run, env

env.hosts = ['waldo@dellsystem.me']

def less():
    local('lessc css/styles.less -x > css/styles.css')

def prepare():
    less()
    local('jekyll')

def up():
    less()
    local('jekyll --server --auto')

def archive():
	local('rm _site/design.svg _site/fabfile* _site/css/*.less')
	local('tar czf site.tar.gz _site')

def transfer():
	local('scp site.tar.gz %s:' % env.hosts[0])
	local('rm site.tar.gz')

def unpack():
	run('tar xzf site.tar.gz')

def deploy():
	prepare()
	archive()
	transfer()
	unpack()
