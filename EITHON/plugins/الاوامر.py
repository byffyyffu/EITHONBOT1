from EITHON import EITHON
from telethon import events

@EITHON.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""اوامر سورس ايــثــون المؤقت: 

`.فحص`
- لتجربه السورس

`.مؤقت` + وقت بالثواني  + عدد تكرار + نص
- يقوم بعمل تكرار مؤقت للكلام 

`.تكرار`  + كلام
- يقوم بتكرار الكلام

`.ضيف` + رابط مجموعه عامه
- ارسل الامر في مجموعتك واكتب الامر مع رابط مجموعه عامه ليقوم بسرقه لاعضاء متها

`.للخاص` + كلام
- اكتب الامر مع كلام لعمل اذاعه للكلام للخاص

`.للكروبات` + كلام
- اكتب الامر مع كلام لعمل اذاعه للكلام للكروبات 

`.اسم وقتي`
- يبدأ اسم وقتي

`.بايو وقتي`
- يبدأ بايو وقتي

`.ذاتية`
- بالرد على صورة ذاتية التدمير لحفظها في الرسائل المحفوظه

`.فك المحظورين`
- لالغاء جميع المستخدمين الذي حظرتهم في الخاص
( ممكن يعلق الامر بسبب الضغط وما يفك كل الحظرتهم فالحل تستخدمه مره ثانيه بوقت ثاني ) 

`.اعادة تشغيل`
- لايقاف الاسم الوقتي و البايو الوقتي و التكرار
""")
      
