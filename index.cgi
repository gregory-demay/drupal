#!/usr/bin/python

import os

referrer = str(os.environ.get('HTTP_REFERER'))

print 'Content-Type: text/html'
print 'Cache-Control: no-cache'
print


if referrer.find('install.php') == -1:
    print (
        "<p>You're almost done! <a href='install.php?profile=standard&locale=en'>Click "
        "Here</a></p>"
    )
else:
    # Drupal installation is complete, delete index.cgi.
    os.system('rm ' + __file__)
    print "<a href=''>Click Here</a>"

