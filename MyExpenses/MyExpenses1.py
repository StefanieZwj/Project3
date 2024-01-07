import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[0]
    d = u2.connect(avd_serial)
    d.app_start("org.totschnig.myexpenses.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.totschnig.myexpenses.debug":
            break
        time.sleep(2)
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/MANAGE_TEMPLATES_COMMAND")
    d.click()
    if not out:
        print("Success: press Template")
    wait()
    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND")
    d.click()
    if not out:
        print("Success: press FAB")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/Title")
    if not out:
        d.set_text('T')
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/TaType")
    d.click()
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/AmountEditText")
    if not out:
        d.set_text('9999999999999999')
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/Category")
    d.click()
    wait()

    out = d.click(95, 420)
    if not out:
        print("Success: press ViewExpand")
    wait()

    out = d.click(540, 546)
    if not out:
        print("Success: press Premiums")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND")
    d.click()
    wait()
    for i in range(10):
        out = d(resourceId="org.totschnig.myexpenses.debug:id/Plan")
        d.click()
        wait()

    # click the Navigation
    out = d.click(1027, 142)
    if not out:
        print("Success: press top right corner")
    wait()

    # click the Settings
    out = d.click(812, 419)
    if not out:
        print("Success: press History")
    wait()

    # scroll down the settings
    out = d.click(842, 2174)
    if not out:
        print("Success: press Try")

    wait()

    # scroll down the settings
    out = d.click(540, 1118)
    if out:
        print("Success: press green column")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)