import asyncio
from telethon import events
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest
from EITHON import EITHON

@EITHON.on(events.NewMessage(outgoing=True, pattern="^.ضيف$"))
async def get_users(event):
    legen_ = event.text[10:]
    EITHON_chat = legen_.lower
    restricted = ["@eithonsupport", "@eithonsupport"]
    EITHON = await event.edit(f"**جارِ اضأفه الاعضاء من  ** {legen_}")
    if EITHON_chat in restricted:
        return await EITHON.edit(
            event, "**- لا يمكنك اخذ الاعضاء من مجموعه السورس العب بعيد ابني  :)**"
        )
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        await EITHON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    else:
        await EITHON.edit("**▾∮ تتم العملية انتظر قليلا ...**")
    if event.is_private:
        return await EITHON.edit("- لا يمكنك اضافه الاعضاء هنا")
    s = 0
    f = 0
    error = "None"
    await EITHON.edit(
        "**▾∮ حالة الأضافة:**\n\n**▾∮ تتم جمع معلومات المستخدمين 🔄 ...⏣**"
    )
    async for user in event.client.iter_participants(event.pattern_match.group(1)):
        try:
            if error.startswith("Too"):
                return await EITHON.edit(
                    f"**حالة الأضافة انتهت مع الأخطاء**\n- (**ربما هنالك ضغط على الأمر حاول مجددا لاحقا **) \n**الخطأ** : \n`{error}`\n\n• اضافة `{s}` \n• خطأ بأضافة `{f}`"
                )
            tol = f"@{user.username}"
            lol = tol.split("`")
            await EITHON(InviteToChannelRequest(channel=event.chat_id, users=lol))
            s = s + 1
            await EITHON.edit(
                f"**▾∮تتم الأضافة **\n\n• اضيف `{s}` \n•  خطأ بأضافة `{f}` \n\n**× اخر خطأ:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await EITHON.edit(
        f"**▾∮اڪتملت الأضافة ✅** \n\n• تم بنجاح اضافة `{s}` \n• خطأ بأضافة `{f}`"
    )
