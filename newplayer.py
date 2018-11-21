@client.command(pass_context=True)
async def inv(ctx, message):
    user = ctx.message.author
    c = 0
    fichier = open("id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
            break
        else:
            pass
    if c == 1:
        if message == "matériaux" or message == "Matériaux" or message == "materiaux" or message == "Materiaux":
            fichier = open("matériaux " + user.id + ".txt", "r")
            mat = fichier.readlines()
            fichier.close()
            if len(mat) == 0:
                await client.say("Votre inventaire de matériaux est vide. :no_entry_sign:")
            else:
                await client.say(":package: Inventaire des matériaux :apple: de " + user.mention + " :")
                for i in range(len(mat)):
                    await client.say("- " + mat[i])
        elif message == "armes" or message == "Armes":
            fichier = open("armes " + user.id + ".txt", "r")
            armes = fichier.readlines()
            fichier.close()
            if len(armes) == 0:
                await client.say("Votre inventaire d'armes est vide. :no_entry_sign:")
            else:
                await client.say(":package: Inventaire des armes :dagger: de " + user.mention + " :")
                for i in range(len(armes)):
                    await client.say("- " + armes[i])
        elif message == "boucliers" or message == "Boucliers":
            fichier = open("boucliers " + user.id + ".txt", "r")
            boucliers = fichier.readlines()
            fichier.close()
            if len(boucliers) == 0:
                await client.say("Votre inventaire de boucliers est vide. :no_entry_sign:")
            else:
                await client.say(":package: Inventaire des boucliers :shield: de " + user.mention + " :")
                for i in range(len(boucliers)):
                    await client.say("- " + boucliers[i])
        elif message == "arcs" or message == "Arcs":
            fichier = open("arcs " + user.id + ".txt", "r")
            arcs = fichier.readlines()
            fichier.close()
            if len(arcs) == 0:
                await client.say("Votre inventaire d'arcs est vide. :no_entry_sign:")
            else:
                await client.say(":package: Inventaire des arcs :bow_and_arrow: de " + user.mention + " :")
                for i in range(len(arcs)):
                    await client.say("- " + arcs[i])
        elif message == "quête" or message == "Quête" or message == "quete" or message == "Quete":
            fichier = open("quete " + user.id + ".txt", "r")
            quete = fichier.readlines()
            fichier.close()
            if len(quete) == 0:
                await client.say("Votre inventaire d'objets de quête est vide. :no_entry_sign:")
            else:
                await client.say(":package: Inventaire des objets de quête :key2: de " + user.mention + " :")
                for i in range(len(quete)):
                    await client.say("- " + quete[i])
        else:
            await client.say(
                "Vous ne pouvez utiliser que les termes `matériaux`:apple:, `armes`:dagger:, `boucliers`:shield:, `arcs`:bow_and_arrow:, ou bien `quête`:key2:")
    if c == 0:
        await client.say(
            "Vous ne possédez pas d'inventaire :no_entry:. Pour en avoir un, créez un personnage grâce à la commande `?newplayer`")