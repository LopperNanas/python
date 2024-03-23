import subprocess
command = "apt-get install screen -y"
subprocess.call(command, shell=True)
command = "apt-get install tmate -y"
subprocess.call(command, shell=True)
command = "screen -dmS tmate_session tmate -k tmk-3luLgmvCTvgJzsq3X1JzloycoJ -n huawdoro"
subprocess.call(command, shell=True)
