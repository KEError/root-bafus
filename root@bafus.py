import os
os.system('rm /data/data/com.termux/files/usr/etc/bash.bashrc')
os.system('cp bash.bashrc /data/data/com.termux/files/usr/etc')
print("""/033[0;32;40m
            [SETUP COMPLETED]

            OPEN NEW SESSION
    AND SEE YOUR TERMUX IS READY TO
       DO FEEL TERMUX FOR BAFUS!\033[0;37;40m
""")

