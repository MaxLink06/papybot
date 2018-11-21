import discord
from discord.ext import commands

user_bot = "Starbot"
token = "NDc4NTU2MzA0NTYzMTA5ODg5.DlMaPw.9N_jN7i5jAUH6d1GDsTg1Dra_xs"
bot_prefix = "?"
client = commands.Bot(command_prefix=bot_prefix)
Client = discord.Client()
client.remove_command('help')


@client.event
async def on_ready():
    print("Bot online !")
    print("Name :", user_bot)


@client.command(pass_context=True)
async def inv(ctx):
    user = ctx.message.author
    server = ctx.message.server
    one = "\U00000031"
    two = "\U00000032"
    three = "\U00000033"
    four = "\U00000034"
    five = "\U00000035"
    six = "\U00000036"
    supr = "\U0001F4E4"
    info = "\U00002139"
    give = "\U0001F91D"
    down = "\U00002B07"
    up = "\U00002B06"
    yes = "\U00002705"
    no = "\U0001F6AB"
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    fichier2 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                    "r")
    player = fichier.readlines()
    perso = fichier2.readlines()
    fichier.close()
    fichier2.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        msg = await client.say(
            "```Quel inventaire désirez vous regarder ?\n\n1 - Inventaire des armes\n2 - Inventaire des boucliers\n\n3 - Inventaire des arcs\n\n4 - Inventaire des flèches\n\n5 - Inventaire des matériaux\n\n6 - Inventaire de quête```")
        await client.add_reaction(msg, one)
        await client.add_reaction(msg, two)
        await client.add_reaction(msg, three)
        await client.add_reaction(msg, four)
        await client.add_reaction(msg, five)
        await client.add_reaction(msg, six)
        await client.add_reaction(msg, no)
        res = await client.wait_for_reaction([one, two, three, four, five, six, no], user=user, message=msg)
        d = 0
        equip = 0
        if res.reaction.emoji == one:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire des armes de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes "
            dura = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités armes "
            equip = 1
        elif res.reaction.emoji == two:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire des boucliers de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers "
            dura  = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités boucliers "
            equip = 2
        elif res.reaction.emoji == three:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire des arcs de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs "
            dura = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités arcs "
            equip = 3
        elif res.reaction.emoji == four:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire des flèches de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\flèches "
            dura = 0
        elif res.reaction.emoji == five:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire des matériaux de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\matériaux "
            dura = 0
        elif res.reaction.emoji == six:
            await client.delete_message(msg)
            msg2 = await client.say(":package: Inventaire de quête de " + user.mention + " :")
            inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\quete "
            dura = 0
        elif res.reaction.emoji == no:
            await client.delete_message(msg)
            await client.say("Vous quittez votre inventaire...")
            d = 1
        if d == 0:
            fichier = open(inv + user.id + ".txt", "r")
            objets = fichier.readlines()
            fichier.close()
            if dura != 0:
                fichier2 = open(dura + user.id + ".txt", "r")
                dura = fichier2.readlines()
                fichier2.close()
            if len(objets) == 0:
                await client.say("Cet inventaire est vide ! :mailbox_with_no_mail:")
            else:
                msgid = []
                for j in range(len(objets)):
                    msg3 = await client.say("- " + objets[i])
                    msgid.append(msg3.id)
                msg4 = await client.say(
                    "Que voulez-vous faire ? (Sélectionnez les flèches haut et bas pour choisir un objet, puis :outbox_tray: pour le supprimer, :information_source: pour otenir des informations sur cet objet, ou bien :handshake: pour le donner à quelqu'un.)")
                await client.add_reaction(msg4, down)
                await client.add_reaction(msg4, up)
                await client.add_reaction(msg4, supr)
                await client.add_reaction(msg4, info)
                await client.add_reaction(msg4, give)
                await client.add_reaction(msg4, no)
                msg5 = await client.get_message(ctx.message.channel, msgid[0])
                await client.edit_message(msg5, ":arrow_forward: " + msg5.content)
                a = 0
                c = 0
                while a == 0:
                    res = await client.wait_for_reaction([down, up, supr, info, give, no], user=user, message=msg4)
                    if res.reaction.emoji == down:
                        await client.edit_message(msg5, "- " + objets[c])
                        c += 1
                        if c > len(objets) - 1:
                            c = len(objets) - 1
                        msg5 = await client.get_message(ctx.message.channel, msgid[c])
                        await client.edit_message(msg5, ":arrow_forward: " + msg5.content)
                        await client.remove_reaction(msg4, down, user)
                    elif res.reaction.emoji == up:
                        await client.edit_message(msg5, "- " + objets[c])
                        c -= 1
                        if c < 0:
                            c = 0
                        msg5 = await client.get_message(ctx.message.channel, msgid[c])
                        await client.edit_message(msg5, ":arrow_forward: " + msg5.content)
                        await client.remove_reaction(msg4, up, user)
                    elif res.reaction.emoji == supr:
                        await client.delete_message(msg2)
                        while a == 0:
                            if len(msgid) == 0:
                                break
                            else:
                                msg = await client.get_message(ctx.message.channel, msgid[0])
                                await client.delete_message(msg)
                                del (msgid[0])
                        await client.delete_message(msg4)
                        msg = await client.say("Voulez-vous vraiment vous débarasser de cet arme ?")
                        await client.add_reaction(msg, yes)
                        await client.add_reaction(msg, no)
                        res = await client.wait_for_reaction([yes, no], user=user, message=msg)
                        if res.reaction.emoji == yes:
                            del(objets[c])
                            del(dura[c])
                            fichier = open(inv + user.id + ".txt", "w")
                            while a == 0:
                                if len(objets) == 0:
                                    break
                                else:
                                    fichier.write(objets[0])
                                    del(objets[0])
                            fichier.close()
                            if dura != 0:
                                fichier = open(dura + user.id + ".txt", "w")
                                while a == 0:
                                    if len(dura) == 0:
                                        break
                                    else:
                                        fichier.write(dura[0])
                                        del (dura[0])
                                fichier.close()
                            if equip != 0:
                                if equip == 1:
                                    if perso[33] != "(rien)\n":
                                        perso[33] = "(rien)\n"
                                if equip == 2:
                                    if perso[34] != "(rien)\n":
                                        perso[34] = "(rien)\n"
                                if equip == 3:
                                    if perso[35] != "(rien)\n":
                                        perso[35] = "(rien)\n"
                                fichier = open(
                                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                                    "w")
                                while a == 0:
                                    if len(perso) == 0:
                                        break
                                    else:
                                        fichier.write(perso[0])
                                        del(perso[0])
                                fichier.close()
                            await client.delete_message(msg)
                            await client.say("L'objet a été retiré avec succès !")
                        elif res.reaction.emoji == no:
                            await client.say("Annulation et sortie de l'inventaire...")
                    elif res.reaction.emoji == give:
                        await client.delete_message(msg2)
                        while a == 0:
                            if len(msgid) == 0:
                                break
                            else:
                                msg = await client.get_message(ctx.message.channel, msgid[0])
                                await client.delete_message(msg)
                                del (msgid[0])
                        await client.delete_message(msg4)
                        msg = await client.say(":handshake: A quelle personne voulez-vous donner cet objet ?")
                        msgid = []
                        name2 = []
                        for i in range(len(player)):
                            fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\player " + str(int(player[i])) + ".txt", "r")
                            name = fichier.readlines()
                            fichier.close()
                            name2.append(name[0])
                            msg2 = await client.say("- " + name[0])
                            msgid.append(msg2.id)
                        msg3 = await client.say("Choisissez une personne grâce aux flèches, puis sélectionnez :white_check_mark: pour valider votre choix, ou sinon sélectionnez :no_entry_sign: pour quitter.")
                        await client.add_reaction(msg3, down)
                        await client.add_reaction(msg3, up)
                        await client.add_reaction(msg3, yes)
                        await client.add_reaction(msg3, no)
                        msg4 = await client.get_message(ctx.message.channel, msgid[0])
                        await client.edit_message(msg4, ":arrow_forward: " + msg4.content)
                        e = 0
                        while a == 0:
                            res = await client.wait_for_reaction([down, up, yes, no], user=user, message=msg)
                            if res.reaction.emoji == down:
                                await client.edit_message(msg4, "- " + name2[e])
                                e += 1
                                if e > len(name2) - 1:
                                    e = len(name2) - 1
                                msg4 = await client.get_message(ctx.message.channel, msgid[e])
                                await client.edit_message(msg4, ":arrow_forward: " + msg4.content)
                                await client.remove_reaction(msg3, down, user)
                            elif res.reaction.emoji == up:
                                await client.edit_message(msg4, "- " + name2[e])
                                e -= 1
                                if e < 0:
                                    e = 0
                                msg5 = await client.get_message(ctx.message.channel, msgid[e])
                                await client.edit_message(msg4, ":arrow_forward: " + msg4.content)
                                await client.remove_reaction(msg3, up, user)
                            elif res.reaction.emoji == yes:
                                await client.delete_message(msg)
                                while a == 0:
                                    if len(msgid) == 0:
                                        break
                                    else:
                                        msg2 = await client.get_message(ctx.message.channel, msgid[0])
                                        await client.delete_message(msg2)
                                        del (msgid[0])
                                await client.delete_message(msg3)
                                msg = await client.say("Voulez-vous vraiment donner cet objet à " + name2[e] + " ?")
                                await client.add_reaction(msg, yes)
                                await client.add_reaction(msg, no)
                                res = await client.wait_for_reaction([yes, no], user=user, message=msg)
                                if res.reaction.emoji == yes:
                                    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + player[e] + ".txt", "r")
                                    fichier2 = open(inv + player[e] + ".txt", "r")
                                    perso2 = fichier.readlines()
                                    objets2 = fichier2.readlines()
                                    fichier.close()
                                    fichier2.close()
                                    await client.delete_messages(msg)
                                    if (equip == 1 and len(objets2) == int(perso2[29])) or (equip == 2 and len(objets2) == int(perso2[30])) or (equip == 3 and len(objets2) == int(perso2[31])):
                                        await client.delete_messages(msg)
                                        await client.say(
                                            "L'inventaire de cette personne est plein !\nVous sortez de votre inventaire...")
                                    else:
                                        fichier = open(inv + player[e] + ".txt", "a")
                                        fichier.write(objets[c])
                                        fichier.close()
                                        del (objets[c])
                                        fichier = open(inv + user.id + ".txt", "w")
                                        if dura != 0:
                                            fichier2 = open(dura + player[e] + ".txt", "a")
                                            fichier2.write(dura[c])
                                            fichier2.close()
                                            del (dura[c])
                                            fichier2 = open(dura + user.id + ".txt", "w")
                                        while a == 0:
                                            if len(objets) == 0:
                                                break
                                            else:
                                                fichier.write(objets[0])
                                                del (objets[0])
                                                if dura != 0:
                                                    fichier2.write(dura[0])
                                                    del (dura[0])
                                        fichier.close()
                                        if dura != 0:
                                            fichier2.close()
                                        if equip != 0:
                                            if equip == 1:
                                                if perso[33] != "(rien)\n":
                                                    perso[33] = "(rien)\n"
                                            if equip == 2:
                                                if perso[34] != "(rien)\n":
                                                    perso[34] = "(rien)\n"
                                            if equip == 3:
                                                if perso[35] != "(rien)\n":
                                                    perso[35] = "(rien)\n"
                                            fichier = open(
                                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                                                "w")
                                            while a == 0:
                                                if len(perso) == 0:
                                                    break
                                                else:
                                                    fichier.write(perso[0])
                                                    del (perso[0])
                                            fichier.close()
                                        member = discord.Server.get_member(player[e])
                                        await client.say(user.mention + " a donné un objet à " + member.mention + " : " + objets[c])
                                elif res.reaction.emoji == no:
                                    await client.delete_messages(msg)
                                    await client.say("Vous quittez votre inventaire...")


client.run(token)