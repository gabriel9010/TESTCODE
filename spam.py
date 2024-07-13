import os, json, asyncio
from telethon import TelegramClient, events, Button
from telethon.sync import TelegramClient as Testc
from telethon.errors import PhoneNumberFloodError, SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetDialogsRequest, SendInlineBotResultRequest, GetInlineBotResultsRequest
from telethon.sessions import StringSession
from telethon.tl.functions.messages import GetDialogsRequest

import time
import random
import pickle
devices = {0: {"m_name": "Iphone 13", "s_name": "15.1.1", "s_app": "8.1.2"},
           1: {"m_name": "Iphone 12", "s_name": "15.1.1", "s_app": "8.3.1"},
           2: {"m_name": "Iphone 7", "s_name": "14.5.1", "s_app": "6.2.1"},
           3: {"m_name": "Iphone 7", "s_name": "14.5.1", "s_app": "6.0.1"},
           4: {"m_name": "Iphone 6", "s_name": "14.4.2", "s_app": "7.6"}}
if os.path.exists("device.pk"):
    with open("device.pk", "rb") as rrrr:
        try:
            c = pickle.load(rrrr)
            if len(c) < 1:
                actualdevice = random.choice(devices)
            else:
                actualdevice = c
        except:
            actualdevice = random.choice(devices)
            with open("device.pk", "wb") as pkw:
                pickle.dump(actualdevice, pkw)
else:
    actualdevice = random.choice(devices)
    with open("device.pk", "wb") as pkw:
        pickle.dump(actualdevice, pkw)
increment = 40
actual_increment = 0
ADMIN = 5492201619

API_KEY = 26483422
API_HASH = "2677c9bb89c72714322e46e23ce8da0d"
Values = {}
proxyact = True
if proxyact:
    with open("C:/Users/CHERRY-PC/Desktop/bottelegram/SpammerBot/tgceo/proxylist.txt", "r") as f:
        Values["proxyes"] = f.readlines()
        Values["proxy"] = 0
Getter = None
Number = None
TempClient = None
SpamEnabled = False
countgruppi = 0
Time = None
Message2 = None
markup = None
Message = None
pvtspam = False
timen = 0
temp =None
Joinbool = True
privatespam = False
if os.path.exists("admins.json"):
    with open("admins.json", "r+") as f:
        admins = json.load(f)
else:
    admins = {}
    with open("admins.json", "w+") as f:
        json.dump(admins, f)
if os.path.exists("SSs.json"):
    with open("SSs.json", "r+") as f:
        SSs = json.load(f)
else:
    SSs = {}
    with open("SSs.json", "w+") as f:
        json.dump(SSs, f)

if os.path.exists("ArchSSs.json"):
    with open("ArchSSs.json", "r+") as f:
        ArchSSs = json.load(f)
else:
    ArchSSs = {}
    with open("ArchSSs.json", "w+") as f:
        json.dump(ArchSSs, f)


def saveSS():
    global SSs
    with open("SSs.json", "w+") as f:
        json.dump(SSs, f)


def saveadmins():
    global admins
    with open("admins.json", "w+") as f:
        json.dump(admins, f)


def saveArchSS():
    global ArchSSs
    with open("ArchSSs.json", "w+") as f:
        json.dump(ArchSSs, f)


async def getAllChats(chats):
    global VARS, countgruppi

    groups = []
    for i in chats:
        if type(i).__name__ == "Channel":
            if i.megagroup and not i.left:
                countgruppi = countgruppi + 1
                groups.append(i.id)
        elif type(i).__name__ == "Chat":
            if not i.left:
                countgruppi = countgruppi + 1
                groups.append(i.id)
    return groups


contactedusers = []
groupbanned = []

async def doSpam(t):
    global ADMIN, SSs, API_KEY, API_HASH, markup, usernameofbot, contactedusers, tempn2, Values, proxyact,bot, privatespam, groupbanned, actualdevice, increment, actual_increment, incremento_active
    banned = []
    contactedusers = []
    for SS in SSs:
        tempn2 = SS
        CClient = None

        try:
            if proxyact:
                proxy = None
                try:
                    if temp not in proxyforvoips:
                        proxyforvoips[SS] = Values["proxyes"][
                            Values["proxy"]]
                        if len(Values["proxyes"]) - 2 < Values["proxy"]:
                            Values["proxy"] = 0
                        Values["proxy"] += 1
                    proxy = proxyforvoips[SS].split(":")
                except:
                    pass
                if proxy is not None:
                    CClient = Testc(StringSession(SSs[SS]),
                                    API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                    proxy=("socks5", proxy[0],
                                           int(proxy[1])))
            else:
                CClient = Testc(StringSession(SSs[SS]), API_KEY,
                                API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
            await CClient.connect()
        except:
            pass
        try:
            if await CClient.get_me():
                try:
                    result = await CClient(GetDialogsRequest(
                        offset_date=None,
                        offset_id=0,
                        offset_peer=InputPeerEmpty(),
                        limit=100,
                        hash=0))
                    entities = result.chats
                    groups = await getAllChats(entities)

                    i7 = 0
                    for group in groups:
                        if group not in groupbanned:
                            try:
                                try:
                                    if "markup" in voipMessages[SS]:
                                        if voipMessages[SS]["markup"] is not None:
                                            results = await CClient.inline_query(usernameofbot, "option")
                                            ent = await CClient.get_entity(group)
                                            message = await results[0].click(ent)
                                            await asyncio.sleep(45)
                                    else:
                                        await CClient.send_message(group, voipMessages[SS]["Message"][0],
                                                                   file=voipMessages[SS]["Message"][1],
                                                                   link_preview=voipMessages[SS]["Message"][2])
                                        await asyncio.sleep(22)
                                    i7 += 1
                                except FloodWaitError as err:
                                    await bot.send_message(ADMIN, "FloodWait, aspettare " + str(
                                        err.seconds + 330) + f" per continuare a spammare.\n\nho spammato già: {i7} volte!",
                                                           buttons=[[Button.inline("❌ INDIETRO ❌",
                                                                                   "back")], [
                                                                        Button.inline(
                                                                            "🔄AGGIORNA🔄",
                                                                            "updatetime")]])

                                    await asyncio.sleep(err.seconds + 330)
                                except:
                                    actual_increment += increment
                                    groupbanned.append(group)
                                if privatespam:
                                    try:
                                        ent = await CClient.get_entity(group)
                                        utenti = CClient.iter_participants(ent.id, aggressive=True)
                                        async for utente in utenti:
                                            if "markup" in voipMessages[SS]:
                                                if voipMessages[SS]["markup"] is not None:
                                                    results = await CClient.inline_query(usernameofbot, "option")
                                                    ent = await CClient.get_entity(ent)
                                                    message = await results[0].click(ent)
                                                    await asyncio.sleep(50)
                                            else:
                                                await CClient.send_message(utente, voipMessages[SS]["Message"][0],
                                                                           file=voipMessages[SS]["Message"][1],
                                                                           link_preview=voipMessages[SS]["Message"][
                                                                               2])
                                                await asyncio.sleep(22)
                                        i7 += 1
                                    except FloodWaitError as err:
                                        await bot.send_message(ADMIN, "FloodWait, aspettare " + str(
                                            err.seconds + 22) + f" per continuare a spammare.\n\nho spammato già: {i7} volte!",
                                                               buttons=[[Button.inline("❌ INDIETRO ❌",
                                                                                       "back")], [
                                                                            Button.inline(
                                                                                "🔄AGGIORNA🔄",
                                                                                "updatetime")]])

                                        await asyncio.sleep(err.seconds + 22)
                                    except Exception as e5:
                                        actual_increment += increment
                                        print(str(e5))
                            except Exception as E:
                                actual_increment += increment * 2
                        await asyncio.sleep(actual_increment)
                except Exception as E:
                    print(E)
                    banned.append(SS)
                    actual_increment += increment *3
                    await bot.send_message(ADMIN,
                                           f"**⚠️ »** __Il VoIP__ `{SS}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")


            else:
                banned.append(SS)
                await bot.send_message(ADMIN,
                                       f"**⚠️ »** __Il VoIP__ `{SS}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")
        except Exception as EE:
            print(EE)
            banned.append(SS)
            await bot.send_message(ADMIN,
                                   f"**⚠️ »** __Il VoIP__ `{SS}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")

    if len(banned) > 0:
        for n in banned:
            if n in SSs:
                del (SSs[n])
        saveSS()


users = []
userschats = {}
bot = TelegramClient('bot3', API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"]).start()
usernameofbot = bot.get_me().username
voipMessages = {}
tempn2 = None
tempn = None
proxyforvoips = {}
incremento_active = False

@bot.on(events.NewMessage(incoming=True))
async def MessagesManager(e):
    global ADMIN, Getter, Number, TempClient, API_KEY, API_HASH, ArchSSs, SSs, SpamEnabled, Time, Message, Joinbool, timen, admins, userschats, Benvenuto, Message2, markup, users, pvtspam, tempn, proxyact, Values, voipMessages, temp, proxyforvoips, groupbanned, actualdevice, actual_increment
    if e.chat_id == ADMIN or e.chat_id in admins:
        if e.text == "/start":
            if SpamEnabled:
                await e.respond(
                    f"**🤖 Spammer Bot**\n\n__ \n Gruppi problematici : {len(groupbanned)}\n\nincremento attuale (se non abilitato sarà sempre 0): {actual_increment}\nPrivate Spammer: {pvtspam}\nℹ️ Stato Spam»__  **Attivo ✅**",
                    buttons=[[Button.inline("❌ Stoppa", "stop"), Button.inline("Spammer 📞", "voip")],
                             [Button.inline("⏱ Tempo", "timer"),
                              Button.inline("Messaggio 💬", "messaggio")],
                             [Button.inline("👥 Entra nei Gruppi 👥", "join")],
                             [Button.url("Gruppi Problematici (?)", "https://telegra.ph/gruppi-problematici-02-27")],
                             [Button.inline("IMPOSTA BOTTONI", "impostabtn")]])
            else:
                await e.respond(f"**🤖 Spammer Bot**\n\n__ \n Gruppi problematici : {len(groupbanned)}\n\nincremento attuale (se non abilitato sarà sempre 0): {actual_increment}\nPrivate Spammer: {pvtspam}\nℹ️ Stato Spam»__  **Non Attivo ❌**",
                    buttons=[[Button.inline("✅ Avvia", "start"), Button.inline("Spammer 📞", "voip")],
                             [Button.inline("⏱ Tempo", "timer"),
                              Button.inline("Messaggio 💬", "messaggio")],
                             [Button.inline("👥 Entra nei Gruppi 👥", "join")],
                             [Button.url("Gruppi Problematici (?)", "https://telegra.ph/gruppi-problematici-02-27")],
                             [Button.inline("IMPOSTA BOTTONI", "impostabtn")]])

        elif Getter is not None:

            if Getter == 0:
                Getter = None
                if e.text not in SSs:
                    if e.text not in ArchSSs:
                        try:
                            if proxyact:
                                proxy = None
                                try:
                                    proxy = Values["proxyes"][Values["proxy"]].split(":")
                                except:
                                    await e.respond(
                                        "I proxy devono essere SERVER:PORTA\n\nproxy non valido!" +
                                        Values["proxyes"][
                                            Values["proxy"]],
                                        buttons=[[Button.inline("🔙 indietro", "back")]])
                                TempClient = Testc(StringSession(), API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                                               proxy=("socks5", proxy[0], int(proxy[1])))
                            else:
                                TempClient = Testc(StringSession(), API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                            await TempClient.connect()
                            try:
                                await TempClient.send_code_request(phone=e.text, force_sms=False)
                                Number = e.raw_text.replace('+', "").replace(" ", "")
                                if Number.isnumeric():
                                    Getter = 1
                                    await e.respond("**📩 Inserisci Il Codice 📩**",
                                                buttons=[[Button.inline("❌ Annulla", "voip")]])
                                else:
                                    await e.respond("Numero non valido! non è un numero associabile (riprova)..", buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                            except PhoneNumberFloodError:
                                await e.respond("**❌ Troppi tentativi! Prova con un altro numero. ❌**",
                                                buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                                await TempClient.disconnect()
                            except:
                                await e.respond("**❌ Numero non Valido ❌**",
                                                buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                                await TempClient.disconnect()
                        except:
                            await e.respond("Numero non valido! non è un numero associabile (riprova)..",
                                            buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                    else:
                        await e.respond("**❌ VoIP Archiviato! Riaggiungilo. ❌**",
                                        buttons=[[Button.inline("📁 VoIP Archiviati 📁", "arch")],
                                                 [Button.inline("🔄 Riprova 🔄", "addvoip")]])
                else:
                    await e.respond("**❌ VoIP già aggiunto ❌**", buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])

            elif Getter == 1:
                try:
                    await TempClient.sign_in(phone=Number, code=e.text)
                    SSs[Number] = TempClient.session.save()
                    Getter, Number = None, None
                    saveSS()
                    await e.respond("**✅ VoIP Aggiunto Correttamente ✅**",
                                    buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                except SessionPasswordNeededError:
                    Getter = 2
                    await e.respond("**🔑 Inserisci la Password (2FA) 🔑**",
                                    buttons=[[Button.inline("❌ Annulla ❌", "voip")]])
                except:
                    Getter, Number = None, None
                    await e.respond("**❌ Codice Errato ❌**", buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                    await TempClient.disconnect()
            elif Getter == 2:
                try:
                    await TempClient.sign_in(phone=Number, password=e.text)
                    SSs[Number] = TempClient.session.save()
                    Getter, Number = None, None
                    saveSS()
                    await e.respond("**✅ VoIP Aggiunto Correttamente ✅**",
                                    buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                except:
                    Getter, Number = None, None
                    await e.respond("**❌ Password Errata ❌**", buttons=[[Button.inline("🔄 Riprova 🔄", "addvoip")]])
                    await TempClient.disconnect()
            elif Getter == 3:
                Getter = None
                if e.text in SSs:
                    await e.respond(f"**🔧 Gestione »** `{e.text}`",
                                    buttons=[[Button.inline("🔧 Messaggio SET🔧 ", "msg;" + e.text)],
                                             [Button.inline("🔧 Messaggio BTN SET🔧 ", "msgbtn;" + e.text)],
                                             [Button.inline("📁 Archivia", "arch;" + e.text),
                                              Button.inline("Rimuovi ➖", "del;" + e.text)], [Button.inline("Join 👥 ", "join;" + e.text)],
                                             [Button.inline("🔙 Indietro 🔙", "voip")]])
                else:
                    await e.respond("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔄 Riprova 🔄", "voips")]])
            elif Getter == 4:
                Getter = None
                if e.text in ArchSSs:
                    await e.respond(f"**🔧 Gestione »** `{e.text}`", buttons=[
                        [Button.inline("➕ Riaggiungi", "add;" + e.text),
                         Button.inline("Rimuovi ➖", "delarch;" + e.text)], [Button.inline("Join 👥 ", "join;" + e.text)],[Button.inline("🔙 Indietro 🔙", "voip")]])
                else:
                    await e.respond("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔄 Riprova 🔄", "voips")]])
            elif Getter == 5:
                if e.text.isnumeric():
                    num = int(e.text)
                    if num > 4 and num < 501:
                        Getter = None
                        Time = num
                        await e.respond("**✅ Tempo impostato correttamente ✅**",
                                        buttons=[[Button.inline("🔙 Indietro 🔙", "timer")]])
                    else:
                        await e.respond("**❌ Tempo non valido! (minimo 5 minuti e massimo 500) ❌\n\n🔄 Riprovare 🔄**",
                                        buttons=[[Button.inline("❌ Annulla ❌", "back")]])
                else:
                    await e.respond(
                        "**❌ Formato tempo non valido! (usare la sintassi a numeri: es. 5) ❌\n\n🔄 Riprovare 🔄**",
                        buttons=[[Button.inline("❌ Annulla ❌", "back")]])
            elif Getter == 6:
                Getter = None
                if e.media != None and type(e.media).__name__ != "MessageMediaWebPage" and type(
                        e.media).__name__ != "MessageMediaUnsupported":
                    media = e.media
                else:
                    media = None
                if e.web_preview != None:
                    lp = True
                else:
                    lp = False
                Message = [e.text, media, lp]
                for Ss in SSs:
                    if Ss not in voipMessages:
                        voipMessages[Ss] = {}
                    voipMessages[Ss]["Message"] = Message
                await e.respond("**✅ Messaggio Impostato Correttamente ✅**",
                                buttons=[[Button.inline("🔙 Indietro 🔙", "messaggio")]])
            elif Getter == 11:
                Getter = None
                if e.media is not None and type(e.media).__name__ != "MessageMediaWebPage" and type(
                        e.media).__name__ != "MessageMediaUnsupported":
                    media = e.media
                else:
                    media = None
                if e.web_preview is not None:
                    lp = True
                else:
                    lp = False
                Message2 = [e.text, media, lp]
                await e.respond("benvenuto settato!", buttons=[[Button.inline("INDIETRO ", "back")]])
            elif Getter == 12:
                Getter = None
                if e.text == "None":
                    for Ss in SSs:
                        if not Ss in voipMessages:
                            voipMessages[Ss] = {}
                        voipMessages[Ss]["markup"] = None
                    await e.respond("senza bottoni: settato!", buttons=[[Button.inline("INDIETRO ", "back")]])
                else:
                    markup = []
                    for a1 in e.text.split("\n"):
                        a2 = a1.split("-")
                        markup.append([Button.url(a2[0], a2[1].replace(" ", ""))])
                    for Ss in SSs:
                        if not Ss in voipMessages:
                            voipMessages[Ss] = {}
                        voipMessages[Ss]["markup"] = markup
                    await e.respond("bottoni settati!", buttons=[[Button.inline("INDIETRO ", "back")]])
            elif Getter == 19:
                Getter = None
                if tempn is not None:
                    if e.text == "None":
                        for Ss in SSs:
                            if Ss not in voipMessages:
                                voipMessages[Ss] = {}
                        voipMessages[tempn]["markup"] = None
                        await e.respond("senza bottoni: settato!", buttons=[[Button.inline("INDIETRO ", "back")]])
                    else:
                        markup = []
                        for a1 in e.text.split("\n"):
                            a2 = a1.split("-")
                            markup.append([Button.url(a2[0], a2[1].replace(" ", ""))])
                        for Ss in SSs:
                            if Ss not in voipMessages:
                                voipMessages[Ss] = {}
                        voipMessages[tempn]["markup"] = markup
                        await e.respond("bottoni settati!", buttons=[[Button.inline("INDIETRO ", "back")]])
            elif Getter == 18:
                Getter = None
                if e.media != None and type(e.media).__name__ != "MessageMediaWebPage" and type(
                        e.media).__name__ != "MessageMediaUnsupported":
                    media = e.media
                else:
                    media = None
                if e.web_preview != None:
                    lp = True
                else:
                    lp = False
                Message = [e.text, media, lp]
                if tempn is not None:
                    for Ss in SSs:
                        if Ss not in voipMessages:
                            voipMessages[Ss] = {}
                    voipMessages[tempn]["Message"] = Message
                    await e.respond("**✅ Messaggio Impostato Correttamente ✅**",
                                    buttons=[[Button.inline("INDIETRO ", "back")]])
            elif Getter == 7:
                Getter = None
                if e.text is not None and e.text != "":
                    groups = e.text.split("\n")
                    Joinbool = True
                    msg = await e.respond(
                        "__⛈ » Accesso ai Gruppi in corso...__\n\n**⚠️ » Questa operazione è pesante e lunga, potrebbero richiedere ore (o giorni)**",
                        buttons=[[Button.inline("❌ STOP ❌", "stopjoin")]])

                    cannotify = True
                    banned = []
                    if SSs.__len__() > 0:
                        for group in groups:
                            if "t.me/" in group or "telegram.me/" in group or group.startswith("@"):
                                if not " " in group:
                                    if Joinbool:
                                        for SS in SSs:
                                            try:
                                                if Joinbool:
                                                    CClient = None
                                                    try:
                                                        if proxyact:
                                                            proxy = None
                                                            try:
                                                                if temp not in proxyforvoips:
                                                                    proxyforvoips[SS] = Values["proxyes"][
                                                                        Values["proxy"]]
                                                                    if len(Values["proxyes"]) - 2 < Values["proxy"]:
                                                                        Values["proxy"] = 0
                                                                    Values["proxy"] += 1
                                                                proxy = proxyforvoips[SS].split(":")
                                                            except:
                                                                await e.respond(
                                                                    "I proxy devono essere SERVER:PORTA\n\nproxy non valido!" +
                                                                    Values["proxyes"][Values["proxy"]]
                                                                )
                                                            if proxy is not None:
                                                                CClient = Testc(StringSession(SSs[SS]),
                                                                                            API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                                                                            proxy=("socks5", proxy[0],
                                                                                                   int(proxy[1])))
                                                        else:
                                                            CClient = Testc(StringSession(SSs[SS]), API_KEY,
                                                                                        API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                                                        await CClient.connect()
                                                    except:
                                                        pass
                                                    if await CClient.get_me():
                                                        if Joinbool:
                                                            i8 = 0
                                                            try:
                                                                await CClient(JoinChannelRequest(group))
                                                                i8 += 1
                                                                await asyncio.sleep(247)
                                                            except FloodWaitError as err:
                                                                timen = time.time() + err.seconds +200
                                                                await msg.edit("FloodWait, aspettare " + str(
                                                                    err.seconds +200) + f" per continuare ad usare il bot.\n\nsono entrato in {i8} gruppi. ",
                                                                               buttons=[
                                                                                   [Button.inline("❌ INDIETRO ❌",
                                                                                                  "back")], [
                                                                                       Button.inline(
                                                                                           "🔄AGGIORNA🔄",
                                                                                           "updatetime")]])
                                                                await asyncio.sleep(err.seconds + 200)
                                                                try:
                                                                    await CClient(JoinChannelRequest(group))
                                                                    i8 += 1
                                                                except:
                                                                    pass
                                                            except Exception as err:
                                                                print(str(err))
                                                                pass
                                                    else:
                                                        await bot.send_message(ADMIN,
                                                                               f"**⚠️ »** __Il VoIP__ `{SS}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")
                                                        banned.append(SS)
                                                    await CClient.disconnect()
                                                else:
                                                    break
                                            except:
                                                await bot.send_message(ADMIN,
                                                                       f"**⚠️ »** __Il VoIP__ `{SS}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")
                                                banned.append(SS)
                                        if len(banned) > 0:
                                            for n in banned:
                                                if n in SSs:
                                                    del (SSs[n])
                                            saveSS()
                                    else:
                                        break
                                else:
                                    await e.edit(
                                        "**❌ un gruppo inserito contiene uno spazio all'interno! (usare la sintassi con l'username o link (ps: puoi dare una lista al bot e entrerà in automatico))**")
                            else:
                                await e.edit(
                                    "**❌ Formato di un gruppo non valido! (usare la sintassi con l'username o con i link (ps: puoi dare una lista al bot e entrerà in automatico)) **")
                    else:
                        cannotify = False
                        await msg.edit("**❌ Non hai aggiunto nessun VoIP ❌**",
                                       buttons=[[Button.inline("➕ Aggiungi ➕", "addvoip")],
                                                [Button.inline("🔙 Indietro 🔙", "back")]])
                    if cannotify:
                        await msg.edit("**✅ Accesso ai Gruppi Terminato✅**",
                                       buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
                else:
                    await e.respond(
                        "**❌ Gruppi non inseriti come testo valido! (usare la sintassi con l'username o con i link (ps: puoi dare una lista al bot e entrerà in automatico)) ❌\n\n🔄 Riprovare 🔄**",
                        buttons=[[Button.inline("❌ Annulla ❌", "back")]])
            elif Getter == 60:
                if e.text is not None and e.text != "":
                    groups = e.text.split("\n")
                    Joinbool = True
                    msg = await e.respond(
                        "__⛈ » Accesso ai Gruppi in corso...__\n\n**⚠️ » Questa operazione è pesante e lunga, potrebbero richiedere ore (o giorni)**",
                        buttons=[[Button.inline("❌ STOP ❌", "stopjoin")]])

                    cannotify = True
                    banned = []
                    if proxyact:
                        proxy = None
                        try:
                            if temp not in proxyforvoips:
                                proxyforvoips[temp] = Values["proxyes"][Values["proxy"]]
                                if len(Values["proxyes"]) - 2 < Values["proxy"]:
                                    Values["proxy"] = 0
                                Values["proxy"] += 1
                            proxy = proxyforvoips[temp].split(":")
                        except:
                            await e.respond(
                                "I proxy devono essere SERVER:PORTA\n\nproxy non valido!" +
                                Values["proxyes"][Values["proxy"]]
                            )
                        if proxy is not None:
                            TempClient = Testc(StringSession(SSs[temp]), API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                                        proxy=("socks5", proxy[0], int(proxy[1])))
                    else:
                        TempClient = Testc(StringSession(SSs[temp]), API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                    await TempClient.connect()
                    for group in groups:
                        if "t.me/" in group or "telegram.me/" in group or group.startswith("@"):
                            if not " " in group:
                                if Joinbool:
                                        try:
                                            if await TempClient.get_me():
                                                if Joinbool:
                                                    i8 = 0
                                                    try:
                                                        await TempClient(JoinChannelRequest(group))
                                                        i8 += 1
                                                        await asyncio.sleep(470)
                                                    except FloodWaitError as err:
                                                        timen = time.time() + err.seconds +230
                                                        await msg.edit("FloodWait, aspettare " + str(
                                                            err.seconds +230) + f" per continuare ad usare il bot.\n\nsono entrato in {i8} gruppi. ",
                                                                       buttons=[
                                                                            [Button.inline("❌ INDIETRO ❌",
                                                                                       "back")], [
                                                                           Button.inline(
                                                                                   "🔄AGGIORNA🔄",
                                                                                   "updatetime")]])
                                                        await asyncio.sleep(err.seconds + 230)
                                                        try:
                                                            await TempClient(JoinChannelRequest(group))
                                                            i8 += 1
                                                        except:
                                                            pass
                                                    except Exception as err:
                                                        print(str(err))
                                                        pass
                                            else:
                                                await bot.send_message(ADMIN,
                                                               f"**⚠️ »** __Il VoIP__ `{temp}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")
                                                banned.append(temp)
                                                await TempClient.disconnect()
                                        except Exception as EE:
                                            print(EE)
                                            await bot.send_message(ADMIN,
                                                            f"**⚠️ »** __Il VoIP__ `{temp}` __potrebbe essere stato bannato da Telegram! Se l'hai solo disconnesso o cambiato proxy, riaggiungilo.__")
                                            banned.append(temp)
                                else:
                                    break
                            else:
                                await e.edit(
                                    "**❌ un gruppo inserito contiene uno spazio all'interno! (usare la sintassi con l'username o link (ps: puoi dare una lista al bot e entrerà in automatico))**")
                        else:
                            await e.edit(
                                "**❌ Formato di un gruppo non valido! (usare la sintassi con l'username o con i link (ps: puoi dare una lista al bot e entrerà in automatico)) **")
                    if len(banned) > 0:
                        for n in banned:
                            if n in SSs:
                                del (SSs[n])
                        saveSS()
                    if cannotify:
                        await msg.edit("**✅ Accesso ai Gruppi Terminato✅**",
                                       buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
                else:
                    await e.respond(
                        "**❌ Gruppi non inseriti come testo valido! (usare la sintassi con l'username o con i link (ps: puoi dare una lista al bot e entrerà in automatico)) ❌\n\n🔄 Riprovare 🔄**",
                        buttons=[[Button.inline("❌ Annulla ❌", "back")]])
        else:
            text1 = e.text.split(" ")
            try:
                if "/admin" in text1[0] and e.chat_id == ADMIN:
                    admins[int(text1[1])] = "admin"
                    saveadmins()
                    await e.respond("reso admin " + text1[1])
                elif "/unadmin" in text1[0] and e.chat_id == ADMIN:
                    del (admins[int(text1[1])])
                    saveadmins()
                    await e.respond("rimosso admin " + text1[1])
            except Exception as e4:
                print(str(e4))


@bot.on(events.CallbackQuery())
async def callbackAIAQuery(e):
    global ADMIN, Getter, Number, TempClient, API_KEY, API_HASH, ArchSSs, SSs, SpamEnabled, Time, Message, Joinbool, timen, admins, Benvenuto, Message2, users, userschats, countgruppi, pvtspam, Values, proxyact, tempn, privatespam, temp, proxyforvoips, groupbanned, actual_increment,incremento_active
    if e.is_private:
        if e.sender_id == ADMIN or e.sender_id in admins:

            if e.data == b"back":
                Getter = None
                if SpamEnabled:
                    await e.edit(
                        f"**🤖 Spammer Bot**\n\n__ \n Gruppi problematici : {len(groupbanned)}\n\nincremento attuale (se non abilitato sarà sempre 0): {actual_increment}\nPrivate Spammer: {pvtspam}\nℹ️ Stato Spam»__  **Attivo ✅**",
                        buttons=[[Button.inline("❌ Stoppa", "stop"), Button.inline("Spammer 📞", "voip")],
                                 [Button.inline("⏱ Tempo", "timer"),
                                  Button.inline("Messaggio 💬", "messaggio")],
                                 [Button.inline("👥 Entra nei Gruppi 👥", "join")],
                                 [Button.url("Gruppi Problematici (?)",
                                             "https://telegra.ph/gruppi-problematici-02-27")],
                                 [Button.inline("IMPOSTA BOTTONI", "impostabtn")]])
                else:
                    await e.edit(
                        f"**🤖 Spammer Bot**\n\n__ \n Gruppi problematici : {len(groupbanned)}\n\nincremento attuale (se non abilitato sarà sempre 0): {actual_increment}\nPrivate Spammer: {pvtspam}\nℹ️ Stato Spam»__  **Non Attivo ❌**",
                        buttons=[[Button.inline("✅ Avvia", "start"), Button.inline("Spammer 📞", "voip")],
                                 [Button.inline("⏱ Tempo", "timer"),
                                  Button.inline("Messaggio 💬", "messaggio")],
                                 [Button.inline("👥 Entra nei Gruppi 👥", "join")],
                                 [Button.url("Gruppi Problematici (?)",
                                             "https://telegra.ph/gruppi-problematici-02-27")],
                                 [Button.inline("IMPOSTA BOTTONI", "impostabtn")]])

            if e.data == b"stopjoin":
                Joinbool = False

            elif e.data == b"updatetime":
                if (timen - time.time()) > -1:
                    await e.edit("FloodWait, aspettare " + str(
                        "%.2f" % (timen - time.time())) + " per il termine/continuo entrata nei gruppi.",
                                 buttons=[[Button.inline("❌ INDIETRO ❌", "back")],
                                          [Button.inline("🔄AGGIORNA🔄", "updatetime")]])
                else:
                    await e.edit("FloodWait terminato!\npuoi usare il bot!",
                                 buttons=[[Button.inline("❌ INDIETRO ❌", "back")],
                                          [Button.inline("🔄AGGIORNA🔄", "updatetime")]])
            if e.data == b"voip":
                try:
                    try:
                        await TempClient.disconnect()
                    except:
                        pass
                    butns = [[Button.inline("➕ Aggiungi ➕ ", "addvoip"), Button.inline("Gestisci 🔧", "voips")],
                                     [Button.inline("📁 Archiviati 📁", "arch")],
                             [Button.inline("📱 Cambia dispositivo 📱", "changedevice")],
                             [Button.inline("🧠 Incremento intelligente 🧠", "incremento")],
                                     [Button.inline("PRIVATE SPAMMER", "privatespam")]]
                    Getter, Number, TempClient = None, None, None
                    if proxyact:
                        butns.append([Button.inline("🌐 Cambia Proxy 🌐", "changeproxy")])
                    butns.append([Button.inline("🔙 Indietro 🔙", "back")])
                    await e.edit(f"__📞 VoIP Aggiunti »__ **{len(SSs)}**",
                                 buttons=butns)
                except Exception as e5:
                    print(str(e5))
            elif e.data == b"privatespam":
                privatespam = not privatespam
                await e.answer("private spammer è: "+ str(privatespam), alert= True)
            elif e.data == b"incremento":
                incremento_active = not incremento_active
                await e.answer(f"🧠incremento intelligente è: {incremento_active}")
            elif e.data == b"addvoip":
                Getter = 0
                await e.edit("**☎️ Inserisci il numero del VoIP che desideri aggiungere ☎️**",
                             buttons=[[Button.inline("❌ Annulla ❌", "voip")]])
            elif e.data == b"changedevice":
                actualdevice = random.choice(devices)
                with open("device.pk", "wb") as pkw:
                    pickle.dump(actualdevice, pkw)
                await e.answer(
                    f"Dispositivo cambiato!\n\nDispositivo: {actualdevice['m_name']}\n Versione sistema: {actualdevice['s_name']}\nVersione TG: {actualdevice['s_app']}",
                    alert=True)

            elif e.data == b"voips":
                if SSs.__len__() > 0:
                    Getter = 3
                    msg = "__☎️ Invia il numero del VoIP che vuoi gestire__\n\n**LISTA VOIP**"
                    for n in SSs:
                        msg += f"\n`{n}`"
                    await e.edit(msg, buttons=[[Button.inline("❌ Annulla ❌", "voip")]])
                else:
                    await e.edit("**❌ Non hai aggiunto nessun VoIP ❌**",
                                 buttons=[[Button.inline("➕ Aggiungi ➕", "addvoip")],
                                          [Button.inline("🔙 Indietro 🔙", "voip")]])
            elif e.data == b"impostabtn":
                Getter = 12
                await e.edit(
                    "IMPOSTA I BOTTONI PER TUTTI I VOIP DA QUI!\n\nimposta i bottoni con i link in questo formato\ntesto - https://google.com\n\n se un link risulta malfunzionante, il bot non funzionerà!\n\nscrivi None per non inviare bottoni!\n\nnota: alcune chat potrebbero non permettere bottoni!",
                    buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
            elif e.data == b"changeproxy":
                if Values["proxy"] > len(Values["proxyes"]) - 2:
                    Values["proxy"] = 0
                else:
                    Values["proxy"] += 1
                await e.answer("Proxy cambiato!", alert=True)
            elif e.data == b"arch":
                if ArchSSs.__len__() > 0:
                    Getter = 4
                    msg = f"__📁 Voip Archiviati »__ **{ArchSSs.__len__()}**\n\n__☎️ Invia il numero del VoIP archiviato che vuoi gestire__\n\n**LISTA VOIP ARCHIVIATI**"
                    for n in ArchSSs:
                        msg += f"\n`{n}`"
                    await e.edit(msg, buttons=[[Button.inline("❌ Annulla ❌", "voip")]])
                else:
                    await e.edit("**❌ Non hai archiviato nessun VoIP ❌**",
                                 buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
            elif e.data == b"start":
                if not SpamEnabled:
                    if SSs.__len__() > 0:
                        if Time is not None:
                            SpamEnabled = True
                            actual_increment = 0
                            await e.edit("**✅ Spam Avviato Correttamente ✅\nIncremento attuale impostato a : 0**",
                                         buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
                            while SpamEnabled:
                                await asyncio.wait([doSpam(e.client)])
                                for i in range(Time * 60):
                                    if SpamEnabled:
                                        await asyncio.sleep(1)
                                    else:
                                        break
                        else:
                            await e.edit("**❌ Tempo non Impostato ❌**",
                                         buttons=[[Button.inline("✍🏻 Imposta ✍🏻", "gettime")],
                                                  [Button.inline("🔙 Indietro 🔙", "back")]])
                    else:
                        await e.edit("**❌ Non hai aggiunto nessun VoIP ❌**",
                                     buttons=[[Button.inline("➕ Aggiungi ➕", "addvoip")],
                                              [Button.inline("🔙 Indietro 🔙", "voip")]])
                else:
                    await e.answer("❌ Lo Spam è già attivo!", alert=True)
            elif e.data == b"stop":
                if SpamEnabled:
                    SpamEnabled = False
                    groupbanned = []
                    await e.edit("**❌ Spam Stoppato Correttamente ❌**",
                                 buttons=[[Button.inline("🔙 Indietro 🔙", "back")]])
                else:
                    await e.answer("❌ Lo Spam non è attivo!", alert=True)
            elif e.data == b"timer":
                if Time == None:
                    await e.edit("**❌ Tempo non impostato ❌\n\nℹ️ Puoi impostarlo con il tasto qui sotto!**",
                                 buttons=[[Button.inline("✍🏻 Imposta ✍🏻", "gettime")],
                                          [Button.inline("🔙 Indietro 🔙", "back")]])
                else:
                    await e.edit(f"__⏱ Tempo »__ **{Time} Minuti**",
                                 buttons=[[Button.inline("✍🏻 Modifica ✍🏻", "gettime")],
                                          [Button.inline("🔙 Indietro 🔙", "back")]])
            elif e.data == b"messaggio":
                await e.edit(f"**vuoi modificare il messaggio di tutti i voip??**",
                             buttons=[[Button.inline("✍🏻 Modifica ✍🏻", "getmsg")],
                                      [Button.inline("🔙 Indietro 🔙", "back")]])
            elif e.data == b"utenticount":
                await e.edit("**numero utenti: " + str(len(users)),
                             buttons=[[Button.inline("🔙INDIETRO", "back")]])
            elif e.data == b"gettime":
                Getter = 5
                await e.edit("__⏱ Inviare il tempo in minuti da impostare!__",
                             buttons=[[Button.inline("❌ Annulla ❌", "back")]])
            elif e.data == b"getmsg":
                Getter = 6
                await e.edit("__💬 Inviare il messaggio da impostare!__",
                             buttons=[[Button.inline("❌ Annulla ❌", "back")]])
            elif e.data == b"join":
                Getter = 7
                await e.edit("__👥 Inviare la lista di gruppi in cui entrare!__",
                             buttons=[[Button.inline("❌ Annulla ❌", "back")]])

            else:
                st = e.data.decode().split(";")

                if st[0] == "arch":
                    if st[1] in SSs:
                        if not st[1] in ArchSSs:
                            ArchSSs[st[1]] = SSs[st[1]]
                            saveArchSS()
                        del (SSs[st[1]])
                        saveSS()
                        await e.edit("**✅ VoIP Archiviato Correttamente ✅**",
                                     buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                elif st[0] == "join":
                    if st[1] in SSs:
                        Getter = 60
                        temp = st[1]
                        await e.edit("**Inserisci la tag (la @) del gruppo in cui entrare**", buttons=[Button.inline("❌ Annulla", "voip")])

                elif st[0] == "msg":
                    if st[1] in SSs:
                        tempn = st[1]
                        Getter = 18
                        await e.edit("__💬 Inviare il messaggio da impostare!__ \nper: " + tempn,
                                     buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                elif st[0] == "msgbtn":
                    if st[1] in SSs:
                        tempn = st[1]
                        Getter = 19
                        await e.edit(
                            "imposta i bottoni con i link in questo formato\ntesto - https://google.com\n\n se un link risulta malfunzionante, il bot non funzionerà!\n\nscrivi None per non inviare bottoni!\n\nnota: alcune chat potrebbero non permettere bottoni \n\n\nper: " +
                            tempn,
                            buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                elif st[0] == "add":
                    if st[1] in ArchSSs:
                        SSs[st[1]] = ArchSSs[st[1]]
                        saveSS()
                        del (ArchSSs[st[1]])
                        saveArchSS()
                        await e.edit("**✅ VoIP Riaggiunto Correttamente ✅**",
                                     buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ VoIP non Trovato ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                elif st[0] == "del":
                    if st[1] in SSs:
                        CClient = None
                        try:
                            if proxyact:
                                proxy = None
                                try:
                                    if temp not in proxyforvoips:
                                        proxyforvoips[st[1]] = Values["proxyes"][
                                            Values["proxy"]]
                                        if len(Values["proxyes"]) - 2 < Values["proxy"]:
                                            Values["proxy"] = 0
                                        Values["proxy"] += 1
                                    proxy = proxyforvoips[st[1]].split(":")
                                except:
                                    await e.respond(
                                        "I proxy devono essere SERVER:PORTA\n\nproxy non valido!" +
                                        Values["proxyes"][Values["proxy"]]
                                    )
                                if proxy is not None:
                                    CClient = Testc(StringSession(SSs[st[1]]),
                                                    API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                                    proxy=("socks5", proxy[0],
                                                           int(proxy[1])))
                            else:
                                CClient = Testc(StringSession(SSs[st[1]]), API_KEY,
                                                API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                            await CClient.connect()
                            await CClient.log_out()
                        except:
                            pass
                        try:
                            await CClient.disconnect()
                        except:
                            pass
                        del (SSs[st[1]])
                        saveSS()
                        await e.edit("**✅ VoIP Rimosso Correttamente ✅**",
                                     buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ VoIP già Rimosso ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                elif st[0] == "delarch":
                    if st[1] in ArchSSs:
                        CClient = None
                        try:
                            if proxyact:
                                proxy = None
                                try:
                                    if temp not in proxyforvoips:
                                        proxyforvoips[st[1]] = Values["proxyes"][
                                            Values["proxy"]]
                                        if len(Values["proxyes"]) - 2 < Values["proxy"]:
                                            Values["proxy"] = 0
                                        Values["proxy"] += 1
                                    proxy = proxyforvoips[st[1]].split(":")
                                except:
                                    await e.respond(
                                        "I proxy devono essere SERVER:PORTA\n\nproxy non valido!" +
                                        Values["proxyes"][Values["proxy"]]
                                    )
                                if proxy is not None:
                                    CClient = Testc(StringSession(ArchSSs[st[1]]),
                                                    API_KEY, API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"],
                                                    proxy=("socks5", proxy[0],
                                                           int(proxy[1])))
                            else:
                                CClient = Testc(StringSession(ArchSSs[st[1]]), API_KEY,
                                                API_HASH,
                                                               device_model=actualdevice["m_name"],
                                                               system_version=actualdevice["s_name"],
                                                               app_version=actualdevice["s_app"])
                            await CClient.connect()
                            await CClient.log_out()
                        except:
                            pass
                        try:
                            await CClient.disconnect()
                        except:
                            pass
                        del (ArchSSs[st[1]])
                        saveArchSS()
                        await e.edit("**✅ VoIP Rimosso Correttamente ✅**",
                                     buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])
                    else:
                        await e.edit("**❌ Voip già Rimosso ❌**", buttons=[[Button.inline("🔙 Indietro 🔙", "voip")]])


@bot.on(events.InlineQuery)
async def h3(event):
    global voipMessages, markup, tempn2
    try:
        builder = event.builder
        if voipMessages[tempn2] != None:
            if voipMessages[tempn2]["Message"][1] is not None:
                await event.answer([
                    builder.photo(file=voipMessages[tempn2]["Message"][1], text=voipMessages[tempn2]["Message"][0],
                                  buttons=voipMessages[tempn2]["markup"],
                                  link_preview=voipMessages[tempn2]["Message"][2])
                ])
            else:
                try:
                    await event.answer([
                        builder.article(title='option', text=voipMessages[tempn2]["Message"][0],
                                        buttons=voipMessages[tempn2]["markup"],
                                        link_preview=voipMessages[tempn2]["Message"][2])
                    ])
                except Exception as e5:
                    print(str(e5))

    except Exception as e6:
        print(str(e6))


bot.run_until_disconnected()
