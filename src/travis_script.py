# file for continuous integration
# please don't try to run this on your own
import os

os.chdir(os.getcwd()+'/src')

file = "../logs/controller.log"
basedir = os.path.dirname("../logs")
if not os.path.exists("../logs"):
    os.makedirs("../logs")
open(file, 'a').close()

import controller as cont
import user_interface as ui

cont.run_update_process("../data/SampleCSV.csv")
ui.initalize_library()
