import os

os.chdir(os.getcwd()+'/src')

import controller as cont
import user_interface as ui

cont.run_update_process("../data/SampleCSV.csv")
ui.initalize_library()
