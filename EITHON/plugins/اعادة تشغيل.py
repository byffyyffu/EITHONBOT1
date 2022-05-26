import sys
from os import execl
from telethon import events
from EITHON import EITHON

@EITHON.on(events.NewMessage(outgoing=True, pattern="^.اعادة تشغيل$"))
async def _(event):
    await event.edit("جار أعادة التشغيل انتظر دقيقه")
    await EITHON.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)
