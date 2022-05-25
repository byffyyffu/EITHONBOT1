import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from DRAGON import DRAGON, LOGGER
from telethon.tl.functions.channels import JoinChannelRequest
from DRAGON.plugins import *

async def saves():
    try:
        os.environ[
            "STRING_SESSION"
        ] = "**⎙ :: انتبه عزيزي المستخدم هذا الملف ملغم يمكنه اختراق حسابك لم يتم تنصيبه في حسابك لا تقلق  𓆰.**"
    except Exception as e:
        print(str(e))
    try:
        await DRAGON(JoinChannelRequest("@EITHON1"))
    except BaseException:
        pass
    try:
        await DRAGON(JoinChannelRequest("@eithonsupport"))
    except BaseException:
        pass

def load_plugins(plugin_name):
    path = Path(f"DRAGON/plugins/{plugin_name}.py")
    name = "DRAGON.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["DRAGON.plugins." + plugin_name] = load

path = "DRAGON/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

DRAGON.start()

DRAGON.loop.create_task(saves())

print("- تم بنجاح تنصيب سورس ايــثــون  @EITHON1")

DRAGON.run_until_disconnected()
