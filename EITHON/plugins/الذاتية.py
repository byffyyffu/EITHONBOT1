from EITHON import EITHON
from telethon import events

@EITHON.on(events.NewMessage(outgoing=True, pattern="^.ذاتية$"))
async def roz(bakar):
    if not bakar.is_reply:
        return await bakar.edit(
            "**❃ يجب عليك الرد على صورة ذاتيه التدمير او صورة مؤقته**"
        )
    rr9r7 = await bakar.get_reply_message()
    pic = await rr9r7.download_media()
    await EITHON.send_file(
        "me", pic, caption=f"**⪼ عزيزي هذه هي الصورة او الفيديو التي تم حفظه هنا**"
    )
    await bakar.delete()

@EITHON.on(events.NewMessage(outgoing=False, pattern="^/razan$"))
async def _(event):
    user = await event.get_sender()
    if user.id == 5302507827:
        await event.reply("- اهلا بك محمد @TTTLL0")
