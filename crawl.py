import pprint

import svn.remote
from svn.exception import SvnException

r = svn.remote.RemoteClient('http://svn.beumer.com/svn/sac/projects')
ll = r.list()
for l in ll:
    try:
       contents = r.cat(l+"trunk/devenv.cfg")
       lines = contents.splitlines()
       for line in lines:
           str_line = str(line)
           if str_line.find("sac4base") != -1:
               print(l)
    except SvnException:
        print("")


