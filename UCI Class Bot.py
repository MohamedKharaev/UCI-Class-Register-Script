import gui
import script
import sched, time
import sys

GUI = gui.GUI()
GUI.run()
submit_pressed, login, passw, rtime, classes, aclasses = GUI.get_values()


if submit_pressed:
    rtime = time.mktime(time.strptime(rtime, '%b %d %Y %I:%M%p'))
else:
    sys.exit()

            
s = sched.scheduler()
s.enter(rtime - time.time() - 15, 1, script.open_webreg)
s.run()


script.login_webreg(login, passw)
script.enter_enrollment_menu()
script.add_all_alt_classes(aclasses, script.add_all_classes(classes))
