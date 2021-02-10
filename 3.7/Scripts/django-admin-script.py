#!C:\BLOG\3.7\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==3.2a1','console_scripts','django-admin'
__requires__ = 'Django==3.2a1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==3.2a1', 'console_scripts', 'django-admin')()
    )
