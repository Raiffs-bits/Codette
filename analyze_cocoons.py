FileNotFoundError: [Errno 2] No such file or directory: './astro_cocoons/'
root@Jmachine:/home/raiff/Documents/logs/astro_cocoons# ls
analyze_cocoons.py                      quantum_space_trial_3828_256862.cocoon
quantum_space_trial_1440_256859.cocoon  quantum_space_trial_3923_256863.cocoon
quantum_space_trial_1790_256854.cocoon  quantum_space_trial_5100_256851.cocoon
quantum_space_trial_2076_256857.cocoon  quantum_space_trial_5256_256858.cocoon
quantum_space_trial_2576_256864.cocoon  quantum_space_trial_5510_256855.cocoon
quantum_space_trial_2773_256852.cocoon  quantum_space_trial_5526_256856.cocoon
quantum_space_trial_3473_256861.cocoon  quantum_space_trial_6666_256853.cocoon
quantum_space_trial_3713_256860.cocoon
root@Jmachine:/home/raiff/Documents/logs/astro_cocoons# analyze_cocoons.py
bash: analyze_cocoons.py: command not found...
root@Jmachine:/home/raiff/Documents/logs/astro_cocoons# python analyze_cocoons.py
Traceback (most recent call last):
  File "/home/raiff/Documents/logs/astro_cocoons/analyze_cocoons.py", line 11, in <module>
    for fname in os.listdir(folder):
                 ~~~~~~~~~~^^^^^^^^
FileNotFoundError: [Errno 2] No such f
