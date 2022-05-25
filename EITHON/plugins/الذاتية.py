from DRAGON import DRAGON
from telethon import events

@DRAGON.on(events.NewMessage(outgoing=True, pattern="^.ذاتية$"))
async def roz(bakar):
    if not bakar.is_reply:
        return await bakar.edit(
            "**❃ يجب عليك الرد على صورة ذاتيه التدمير او صورة مؤقته**"
        )
    rr9r7 = await bakar.get_reply_message()
    pic = await rr9r7.download_media()
    await DRAGON.send_file(
        "me", pic, caption=f"**⪼@EITHON1 عزيزي هذه هي الصورة او الفيديو التي تم حفظه هنا**"
    )
    await bakar.delete()
