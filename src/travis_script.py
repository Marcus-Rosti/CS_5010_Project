# file for continuous integration
# please don't try to run this on your own
import os

os.chdir(os.getcwd()+'/src')

file = "../logs/controller.log"
empty_file = open(file, 'w')
empty_file.write("First Post!")
empty_file.close()

import controller as cont
import user_interface as ui

cont.run_update_process("../data/SampleCSV.csv")
ui.initalize_library()
