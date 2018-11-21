import random

import discord
from discord.ext import commands

user_bot = "PAPYBOT"
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
async def deco(ctx):
    user = ctx.message.author
    if user.id == "291311214263533570":
        await client.send_message(client.get_channel('482954886682771466'),
                                  "THE GREAT PAPYRUS IS TIRED ! HE'S TAKING SOME REST !")
        await client.close()


@client.command(pass_context=True)
async def test(ctx):
    msg = await client.say("test")
    list = []
    list.append(msg.id)
    msg2 = await client.get_message(ctx.message.channel, list[0])
    await client.edit_message(msg2, "lol " + msg2.content)


@client.command(pass_context=True)
async def help(ctx):
    larme = discord.utils.get(ctx.message.server.emojis, name='Larme_de_lumiere')
    await client.say(
        "```Voici la liste des commandes : (prefix : ?)```\n**Les fiches perso :**\n`newplayer` : Permet de créer un personnage :bust_in_silhouette:\n`profile` : Permet de voir sa fiche perso :page_facing_up:\n**Les roll :**\n`roll` : Permet de lancer un dé de 20 :game_die:\n`ratt` : Permet de faire un roll pour les attaques au corps à corps :crossed_swords:\n`rblo` : Permet de faire un roll pour bloquer avec son bouclier :shield: (nécéssite un bouclier pour être utilisée)\n`ragi` Permet de faire un roll d'agilité :cartwheel:\n`rint` : Permet de faire un roll d'intélligence :bulb:\n`rtir` : Permet d'effectuer un roll d'attaque à distance :bow_and_arrow: (nécéssite un arc pour être utilisée)\n**L'inventaire :**\n`inv [type]` : Permet de voir ses inventaire d'armes, boucliers, arcs, matériaux et quête :package:\n`invadd [objet]` : Permet d'ajouter un objet dans son inventaire :inbox_tray:\n`invremove [objet]` : Permet de retirer un objet de son inventaire :outbox_tray:\n`invgive @pseudo [objet]` : Permet de donner un objet à quelqu'un :handshake::package:\n`equip [objet]` : Permet de s'équiper d'un objet se trouvant dans son inventaire :dagger::inbox_tray:\n`unequip [objet]` : Permet de déséquiper un objet :dagger::outbox_tray:\n`invequip` : Permet de voir son équipement :dagger::package:\n**L'argent :**\n`money` : Permet de voir le contenu de sa bourse :moneybag:\n`moneyspend [montant]` : Permet de se débarasser de son argent (dépenser de l'argent dans le contexte du rp) :money_with_wings:\n`moneygive @pseudo [montant]` : Permet de donner de l'argent à quelqu'un :handshake::small_orange_diamond:\n`freemoney @pseudo [montant]` : Permet de give de l'argent à quelqu'un (commande utilisable uniquement par les modérateurs) :handshake::moneybag:")
    await client.say(
        "**La vie :**\n`life` : Permet de voir la vie restante de son personnage :heart:\n`hit @pseudo [nombre]` : Permet de retirer de la vie à la personne que vous avez touché :dagger::heart:\n`regen @pseudo [nombre]` : Permet de régénérer de la vie, par exemple par l'ingéstion d'aliments :apple::heart:\n**Les compétences :**\n`skills` : Permet de voir ses compétences et de répartir ses larmes de lumière " + str(
            larme) + "\n`pcadd @pseudo` : Permet de give une larme de lumière à quelqu'un " + str(
            larme) + ":inbox_tray: (commande utilisable uniquement par les modérateurs)\n`pcremove @pseudo [larme, cac, tir, agi, blo, int]` : Permet de retirer une larme ou bien retirer un niveau de compétence à quelqu'un " + str(
            larme) + ":outbox_tray: (commande utilisable uniquement par les modérateurs)\n\nPour plus de précisions, faites la commande `?h` suivit du nom de la commande à qui vous voulez connaitre plus de détails.")


@client.command(pass_context=True)
async def h(ctx, message: str):
    if message == "newplayer":
        await client.say(
            "```Cette commande permet de créer votre personnage pour participer au rp. Il vous sera demandé le prénom, le nom, le sexe, l'âge et la race de votre personnage. Une fois votre personnage créé, vous pourrez accéder au reste des commandes.```")
    if message == "profile":
        await client.say(
            "```Cette commande permet de voir votre fiche personnage, à condition que celui-ci soit créé avec la commande [newplayer].```")
    if message == "roll":
        await client.say(
            "```Cette commande permet de lancer un dé de 20 classique, sans que la réussite ou l'échec soit affiché.```")
    if message == "ratt":
        await client.say(
            "```Attaquer un ennemi s'effectue grâce à cette commande, qui lance un dé 20. Le succès de votre attaque dépend de votre niveau en attaque au corps à corps. Par exemple, si vous avez un level 6 au corps à corps, si votre lancé est inférieur ou égal à ce niveau, vous réussissez votre attaque, sinon, vous la ratez. Chaque arme au corps à corps possède une valeur d'attaque et une durabilité, chaque coup porté, même si celui-ci est raté, vous fera perdre 1 de durabilité, sauf pour le cas d'un succès critique. La valeur d'une arme définit les dégâts que vous porterez à votre ennemi. Par exemple, si votre épée a une valeur de 5, l'ennemi perdra 5 pv, par contre, si l'ennemi possède une armure ou un bouclier, ces dégâts peuvent être réduits. Dans le cas d'un succès critique, en plus que votre arme ne perd de durabilité, l'ennemi recevra le double des dégâts que vous lui infligé.```")
    if message == "rblo":
        await client.say(
            "```Cette action est possible uniquement si vous possédez un bouclier. Lorsqu'un ennemi vous attaque, vous pouvez réaliser un blocage grâce à cette commande qui déterminera la réussite de votre blocage. Elle lancera un dé 20 où la réussite du jet sera déterminé par votre niveau de blocage. Par exemple, si vous avez un level 4 en blocage, vous réussirez votre blocage si votre résultat est inférieur ou égal à 4, sinon, vous le ratez. Chaque bouclier possède sa durabilité et sa valeur. Chaque tentative de blocage coûtera 1 de durabilité à votre bouclier, par contre, si vous effectué un succès critique, la durabilité du bouclier ne sera pas affectée. En plus de cela, un succès critique occasionne un blocage parfait, déséquilibrant l'ennemi, permettant d'effectuer une riposte (voir plus bas). Si jamais il vous arriverait de réaliser un échec critique, cela occasionnera votre déséquilibre, et donc l’impossibilité d’esquiver pendant l’attaque ennemie.```")
    if message == "ragi":
        await client.say(
            "```Lorsqu’un ennemi vous attaque et que vous ne possédez pas de bouclier pour vous protéger, vous pouvez dans ce cas là effectuer une esquive (même si vous avez un bouclier). Pour cela, lancez un roll d’agilité avec cette commande. La réussite du jet dépendra de votre niveau en agilité. Si vous réalisez un succès critique, cela occasionnera une esquive parfaite, vous permettant d’effectuer une riposte. Si jamais vous réalisez un échec critique, vous recevrez le double des dégâts. Sauter, escalader, pousser ou porter des objets, ou encore voler pour les Piafs, sont des actions nécessitant aussi des jets d’agilité.```")
    if message == "rint":
        await client.say(
            "```Résoudre des énigmes, négocier, cuisiner, apprendre, ou encore comprendre quelque chose de compliqué, sont des actions nécessitant des jets d’intelligence. Pour cela, faites cette commande dont la réussite dépendra de votre niveau en intelligence.```")
    if message == "rtir":
        await client.say(
            "```Il existe 2 types d’attaques à distance : le tir a l’arc, et le lancé d’armes. Chacune de ces deux actions devra se précéder de cette commande qui déterminera la réussite de votre tir. Cette commande lancera un dé 20 et la réussite sera déterminée par rapport à votre niveau en attaque à distance. Par exemple, si vous avez un level 5 en attaque à distance, vous réussirez votre tir si votre résultat est supérieur ou égal à 5, sinon vous le ratez. Pour effectuer un tir à l’arc, il est nécessaire de posséder un arc. Si vous en possédez pas, vous ne pourrez pas en faire. Chaque arc possède une valeur et une durabilité, à chaque fois que vous réalisez un tir, vous perdez 1 de durabilité, même si vous le ratez. Par contre, si vous réalisez un succès critique, vous ne perdez pas de durabilité, et votre flèche atterrit dans la tete de l’ennemi, occasionnant les dégâts doublés. Il est nécessaire de posséder des flèches avant de pouvoir tirer à l’arc. Lancer votre arme est un peu comme le tir à l’arc, mais ne nécessite pas d’arc. Cette attaque peut s’effectuer uniquement si vous êtes équipé d’une arme au corps à corps. Votre arme est donc lancée, et se brise au contact, même si vous ratez votre tir. Les effets sont les mêmes qu’avec le tir à l’arc, mais prend en compte la valeur de l’arme lancée plutôt que celle d’un arc.```")
    if message == "inv":
        await client.say(
            "```Chaque personnage possède son inventaire, enfin, même plusieurs inventaires. Il y a l’inventaire d’arme, qui a un nombre d’emplacements limités, et vous permet de ranger vos armes de mêlée ( #armes ). Il y a également l’inventaire d’arcs, qui a aussi un nombre d’emplacements limités, permettant de ranger vos arcs ( #arcs ). Ensuite, il y a l’inventaire de boucliers, possédant également un nombre de slots limités, vous permettant de ranger vos boucliers ( #boucliers ). Après, il y a l’inventaire d’ingrédients ou de matériaux, qui n’a pas d’emplacements limités, permettant d’entreposer toutes vos trouvailles pour cuisiner, ou bien pour d’autres choses ( #ingrédients #matériaux-de-monstres #matériaux-autres ). Et finalement, il y a l’inventaire de quêtes, gardant précieusement vos objets les plus importants. Pour accéder à ces inventaires, il vous suffit de faire cette commande suivit du nom de l’inventaire que vous voulez regarder.")
    if message == "invadd":
        await client.say(
            "```Durant votre aventure, il vous sera demandé d’ajouter ou bien de retirer des objets de votre inventaire. Pour cela, faites cette commande suivit du nom de l’objets que vous voulez ajouter. Pour les armes, arcs, ou boucliers, il faudra vous référer aux indications de noms dans #armes #arcs et #boucliers  pour les ajouter. Sinon pour le reste, il vous faudra mettre des « _ » à la place des espaces.```")
    if message == "invremove":
        await client.say(
            "```Pour retirer un objet de votre inventaire, il vous suffit de faire cette commande suivit du nom de l’objet.```")
    if message == "invgive":
        await client.say(
            "```Durant votre aventure, il vous arrivera de devoir donner un objet à un autre aventurier. Pour cela, faites cette commande suivit du pseudo et de l'objet que vous voulez lui donner. L'objet sera directement retiré de votre inventaire et ajouté dans celui de la personne désignée. L'échange ne peut s'effectuer si l'inventaire qui doit recevoir l'objet est plein.```")
    if message == "equip":
        await client.say(
            "```Il vous est possible dans votre aventure, de vous équiper des armes, arcs, ou boucliers que vous ramassez. Pour cela, faites cette commande suivit du nom de l’objet. C'est objet seront alors utilisés pour les roll les concernant.```")
    if message == "invequip":
        await client.say(
            "```Pour voir votre équipement, il vous suffit de faire cette commande. Attention, un objet équipé n'est pas retiré de l'inventaire, il gardera sa place dans l'inventaire de celui-ci, et disparaitra quand il sera cassé.```")
    if message == "unequip":
        await client.say(
            "```Pour retirer un élément de votre équipement, il vous suffit de faire cette commande suivit du nom de l'objet.```")
    if message == "money":
        await client.say(
            "```C'est grâce à cette commande que vous pourrez voir l'argent amassé durant votre aventure.```")
    if message == "moneyspend":
        await client.say(
            "```Grâce à cette commande, vous pourrez dépenser votre argent dans le cadre du rp. Il vous suffit de taper cette commande, suivit du montant que vous dépensez.```")
    if message == "moneygive":
        await client.say(
            "```Dans votre aventure, il vous arrivera de donner de l'argent à un autre aventurier. Pour cela, tapez cette commande, suivit du pseudo du joueur, et du montant.```")
    if message == "freemoney":
        await client.say(
            "```Cette commande est utilisable uniquement par les modérateur, et permet de donner de give de l'argent à un joueur (bien sur dans le cadre du rp). Pour cela, faites cette commande suivit du pseudo du joueur et du montant.```")
    if message == "life":
        await client.say(
            "```A la création de votre personnage, celui-ci de base possède 6 points de vie. Cette commande sert à voir la vie restante de son personnage. Une fois les pv tombés à 0, votre personnge meurt, et vous devrez alors en recréer un autre.```")
    if message == "hit":
        await client.say(
            "```Pendant certaines actions, il vous arrivera de perdre de la vie ou faire perdre de la vie à quelqu'un. Dans le cadre du rp, vous devrez retirer des pv en faisant cette commande, suivit du pseudo de la personne à qui retirer des pv (vous ou quelqu'un d'autre), puis du nombre de pv à retirer.```")
    if message == "regen":
        await client.say(
            "```Dans le cadre du rp, il vous arrivera de consommer quelque chose pour regagner de la vie, ou encore régénérer la vie de quelqu'un. Pour cela, faites cette commande, suivit du pseudo de la personne qui reçoit les pv (vous ou quelqu'un d'autre), puis du nombre de pv à restaurer.```")
    if message == "skills":
        await client.say(
            "```Les compétences :\nA la création de votre personnage, vous pourrez accéder à votre arbre de compétences grâce à cette commande. Vous pourrez alors dépenser vos larmes de lumière dans les compétences que vous voulez. Faites attention à bien répartir vos points, car une fois que vous aurez appuyé sur le bouton de validation, les larmes seront alors dépensées définitivement. Le niveau des compétences joue sur les réussites de rolls, si votre roll est en dessous de ce niveau, vous réussissez, sinon, vous perdez.\n\nL'XP:\nChaque compétence possède sa barre d'XP. A chaque fois que vous réaliserez un roll d'une certaine compétence, cela vous fera gagner de l'XP dans la compétence ciblée. Lorsque vous atteindrez le nombre d'XP demandé, vous augmenterez de niveau dans cette compétence et recevrez 1 point de vie. Un succès critique rapporte 2 points d'XP, un échec critique en rapporte aucun.\n\nLes larmes de lumière:\nC'est le symbole des points de compétences. Lorsque vous en recevez, vous acquérez 1 point de vie. Dépenser une larme de lumière dans une compétence la fait monter de niveau.```")
    if message == "pcadd":
        await client.say(
            "```Dans le cadre du rp, il vous arrivera de reçevoir des larmes de lumière. Pour cela, il vous faudra 4 emblèmes du triomphe et les échanger à une statue de la déesse. Cette commande sert à ce que les modos vous donne des larmes. Elle est donc utilisable que par eux. Il faudra alors rentrer cette commande suivit du pseudo de la personne qui recevra la larme de lumière```")
    if message == "pcremove":
        await client.say(
            "```A certains moments dans l'aventure, il vous arrivera de perdre des niveaux ou des larmes de lumière. Cette commande est utilisable uniquement par les modo et se rentre suivit du pseudo de la personne qui perdra une larme ou un niveau, puis ce qui va être retirer. (niveau de corps à corps, tir, blocage, agilité, intélligence, ou larme)```")


@client.command(pass_context=True)
async def newplayer(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    d = 0
    c = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        await client.say("Vous possédez déjà un personnage, voulez vous le remplacer ? (Ecrivez `oui` ou `non`)")
        while c == 0:
            msg = await client.wait_for_message(author=user, channel=ctx.message.channel)
            if msg.content == "oui" or msg.content == "Oui":
                c = 1
            elif msg.content == "non" or msg.content == "Non":
                await client.say("Vous quittez la création de personnage...")
                break
            else:
                await client.say("Veuillez choisir entre oui ou non")
    if c == 1 or b == 0:
        a = 0
        await client.say(
            "Indiquez le prénom de votre nouveau personnage :\n(Ecrivez `exit` pour quitter la création de personnage)")
        while a == 0:
            msg = await client.wait_for_message(author=user, channel=ctx.message.channel)
            if msg.content == "exit" or msg.content == "Exit":
                await client.say("Vous quittez la création de personnage...")
                d = 1
                break
            elif len(msg.content) > 20:
                await client.say("Votre prénom est trop long, veuillez le raccourcir")
            elif len(msg.content) < 3:
                await client.say("Votre prénom est trop court, veuillez le rallonger")
            else:
                break
        if d != 1:
            await client.say(
                "Indiquez le nom de famille de votre personnage :\n(Si vous ne voulez pas de nom de famille, écrivez `none`. Ecrivez `exit` pour quitter la création de personnage)")
            while a == 0:
                msg2 = await client.wait_for_message(author=user, channel=ctx.message.channel)
                if msg2.content == "exit" or msg2.content == "Exit":
                    await client.say("Vous quittez la création de personnage...")
                    d = 1
                    break
                elif len(msg2.content) > 20:
                    await client.say("Votre nom est trop long, veuillez le raccourcir")
                elif len(msg2.content) < 3:
                    await client.say("Votre nom est trop court, veuillez le raccourcir")
                else:
                    break
            if d != 1:
                await client.say(
                    "Indiquez le sexe de votre personnage :\n(Ecrivez `homme` ou `femme`, ou bien écrivez `exit` pour quitter la création de personnage)")
                while a == 0:
                    msg4 = await client.wait_for_message(author=user, channel=ctx.message.channel)
                    if msg4.content == "homme" or msg4.content == "Homme":
                        nomsexe = "Homme"
                        break
                    elif msg4.content == "femme" or msg4.content == "Femme":
                        nomsexe = "Femme"
                        break
                    elif msg4.content == "exit" or msg4.content == "Exit":
                        await client.say("Vous quittez la création de personnage...")
                        d = 1
                        break
                    else:
                        await client.say(
                            "Saisie incorrecte, veuillez saisir une nouvelle fois le sexe de votre personnage.")
                if d != 1:
                    await client.say(
                        "Indiquez l'âge de votre personnage :\n(Ecrivez un nombre, ou bien écrivez `exit` pour quitter la création de personnage)")
                    while True:
                        msg5 = await client.wait_for_message(author=user, channel=ctx.message.channel)
                        if msg5.content == "exit" or msg5.content == "Exit":
                            await client.say("Vous quittez la création de personnage...")
                            d = 1
                            break
                        else:
                            try:
                                int(msg5.content)
                                break
                            except ValueError:
                                await client.say("Veuillez saisir un nombre.")
                                continue
                    if d != 1:
                        await client.say(
                            "Indiquez la race de votre personnage :\n(Ecrivez `exit` pour quitter la création de personnage)")
                        while a == 0:
                            msg3 = await client.wait_for_message(author=user, channel=ctx.message.channel)
                            if msg3.content == "exit" or msg3.content == "Exit":
                                await client.say("Vous quittez la création de personnage...")
                                d = 1
                                break
                            else:
                                break
                        if d != 1:
                            fichier = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                                "w")
                            if msg2.content == "none" or msg2.content == "None":
                                fichier.write(msg.content + "\n")
                                nom = msg.content
                            else:
                                fichier.write(msg.content + " " + msg2.content + "\n")
                                nom = msg.content + " " + msg2.content
                            fichier.write(
                                nomsexe + "\n" + msg5.content + " ans\n" + msg3.content + "\n\n6\n6\n\n0\n\n20\n\n0\n0\n0\n0\n0\n\n0\n0\n0\n0\n0\n10\n10\n10\n10\n10\n\n3\n2\n2\n\n(rien)\n(rien)\n(rien)\n")
                            player.append(user.id + "\n")
                            fichier6 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\matériaux " + user.id + ".txt",
                                "w")
                            fichier7 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + user.id + ".txt",
                                "w")
                            fichier8 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + user.id + ".txt",
                                "w")
                            fichier9 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + user.id + ".txt",
                                "w")
                            fichier10 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\quete " + user.id + ".txt",
                                "w")
                            fichier15 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités armes " + user.id + ".txt",
                                "w")
                            fichier16 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités boucliers " + user.id + ".txt",
                                "w")
                            fichier17 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités arcs " + user.id + ".txt",
                                "w")
                            fichier23 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "w")
                            while a == 0:
                                if len(player) == 0:
                                    break
                                else:
                                    fichier23.write(player[0])
                                    del (player[0])
                            fichier.close()
                            fichier6.close()
                            fichier7.close()
                            fichier8.close()
                            fichier9.close()
                            fichier10.close()
                            fichier15.close()
                            fichier16.close()
                            fichier17.close()
                            fichier23.close()
                            await client.change_nickname(user, nom)
                            await client.say(
                                "Votre personnage a été ajouté avec succès !\n**Nom :** " + nom + "\n**Sexe :** " + nomsexe + "\n**Age :** " + msg5.content + " ans\n**Race :** " + msg3.content)
                            await client.say(
                                "Vous possédez 20 <:Larme_de_lumiere:491215229594632193>. Pour les répartir dans vos compétences, faites la commande `?skills`")


@client.command(pass_context=True)
async def profile(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    fichier2 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                    "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if str(user.id) + "\n" == player[i]:
            b = 1
            break
        else:
            pass
    if b == 1:
        perso = fichier2.readlines()
        fichier2.close()
        await client.say(
            "**Personnage de " + user.mention + " :**\n\n__**Nom :**__ " + perso[0] + "\n__**Age :**__ " + perso[
                1] + "\n__**Sexe :**__ " + perso[2] + "\n__**Race :**__ " + perso[3])
    else:
        await client.say("Vous ne possédez pas de personnage, faite `?newplayer` pour en créer un.")


@client.command(pass_context=True)
async def skills(ctx):
    user = ctx.message.author
    server = ctx.message.server
    moins = "\U00002796"
    plus = "\U00002795"
    quitter = "\U0001F6AB"
    check = "\U00002714"
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        msg = await client.say("**Arbre de compétences de " + user.mention + " :**")
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        larmes = int(perso[10])
        msg2 = await client.say("Vous possédez actuellement " + str(larmes) + "<:Larme_de_lumiere:491215229594632193>")
        cac = int(perso[12])
        tir = int(perso[13])
        agi = int(perso[14])
        blo = int(perso[15])
        sma = int(perso[16])
        msg3 = await client.say(
            ":dagger:__Attaque au corps à corps__ : lvl " + str(cac) + "     <a:xp_orb:496424585990766602>" + str(
                int(perso[18])) + "/" + str(int(perso[23])) + "<a:xp_orb:496424585990766602>")
        msg4 = await client.say(
            ":bow_and_arrow:__Attaque à distance__ : lvl " + str(tir) + "     <a:xp_orb:496424585990766602>" + str(
                int(perso[19])) + "/" + str(int(perso[24])) + "<a:xp_orb:496424585990766602>")
        msg5 = await client.say(":cartwheel:__Agilité__ : lvl " + str(agi) + "     <a:xp_orb:496424585990766602>" + str(
            int(perso[20])) + "/" + str(int(perso[25])) + "<a:xp_orb:496424585990766602>")
        msg6 = await client.say(":shield:__Défense__ : lvl " + str(blo) + "     <a:xp_orb:496424585990766602>" + str(
            int(perso[21])) + "/" + str(int(perso[26])) + "<a:xp_orb:496424585990766602>")
        msg7 = await client.say(":bulb:__Intelligence__ : lvl " + str(sma) + "     <a:xp_orb:496424585990766602>" + str(
            int(perso[22])) + "/" + str(int(perso[27])) + "<a:xp_orb:496424585990766602>")
        a = 0
        if larmes != 0:
            msg8 = await client.say("(Sélectionnez ou déselectionnez les réactions pour répartir vos larmes)")
            if cac != 20:
                await client.add_reaction(msg3, check)
                if larmes != 0:
                    await client.add_reaction(msg3, plus)
                c = 0
                while a == 0:
                    res = await client.wait_for_reaction([moins, plus, check], user=user, message=msg3)
                    if res.reaction.emoji == plus:
                        c += 1
                        larmes -= 1
                        await client.remove_reaction(msg3, plus, user)
                        await client.add_reaction(msg3, moins)
                    elif res.reaction.emoji == moins:
                        c -= 1
                        larmes += 1
                        await client.remove_reaction(msg3, moins, user)
                        await client.add_reaction(msg3, plus)
                    elif res.reaction.emoji == check:
                        await client.remove_reaction(msg3, plus, client.user)
                        await client.remove_reaction(msg3, moins, client.user)
                        await client.remove_reaction(msg3, check, client.user)
                        await client.remove_reaction(msg3, check, user)
                        perso[23] = str(int(perso[23]) + 10 * c) + "\n"
                        await client.edit_message(msg3, ":dagger:__Attaque au corps à corps__ : lvl " + str(
                            cac + c) + "     <a:xp_orb:496424585990766602>" + str(int(perso[18])) + "/" + str(
                            int(perso[23])) + "<a:xp_orb:496424585990766602>")
                        break
                    await client.edit_message(msg2, "Vous possédez actuellement " + str(
                        larmes) + "<:Larme_de_lumiere:491215229594632193>")
                    if larmes == 0:
                        await client.remove_reaction(msg3, plus, client.user)
                    if c == 0:
                        await client.remove_reaction(msg3, moins, client.user)
                        await client.edit_message(msg3, ":dagger:__Attaque au corps à corps__ : lvl " + str(
                            cac) + "     <a:xp_orb:496424585990766602>" + str(int(perso[18])) + "/" + str(
                            int(perso[23])) + "<a:xp_orb:496424585990766602>")
                    else:
                        await client.edit_message(msg3, ":dagger:__Attaque au corps à corps__ : lvl " + str(
                            cac) + " +" + str(
                            c) + "<:Larme_de_lumiere:491215229594632193>" + "     <a:xp_orb:496424585990766602>" + str(
                            int(perso[18])) + "/" + str(int(perso[23])) + "<a:xp_orb:496424585990766602>")
                perso[12] = str(cac + c) + "\n"
            if larmes != 0:
                if tir != 20:
                    await client.add_reaction(msg4, check)
                    if larmes != 0:
                        await client.add_reaction(msg4, plus)
                    c = 0
                    while a == 0:
                        res = await client.wait_for_reaction([moins, plus, check], user=user, message=msg4)
                        if res.reaction.emoji == plus:
                            c += 1
                            larmes -= 1
                            await client.remove_reaction(msg4, plus, user)
                            await client.add_reaction(msg4, moins)
                        elif res.reaction.emoji == moins:
                            c -= 1
                            larmes += 1
                            await client.remove_reaction(msg4, moins, user)
                            await client.add_reaction(msg4, plus)
                        elif res.reaction.emoji == check:
                            await client.remove_reaction(msg4, plus, client.user)
                            await client.remove_reaction(msg4, moins, client.user)
                            await client.remove_reaction(msg4, check, client.user)
                            await client.remove_reaction(msg4, check, user)
                            perso[24] = str(int(perso[24]) + 10 * c) + "\n"
                            await client.edit_message(msg4,
                                                      ":bow_and_arrow:__Attaque à distance__ : lvl " + str(
                                                          c + tir) + "     <a:xp_orb:496424585990766602>" + str(
                                                          int(perso[19])) + "/" + str(
                                                          int(perso[24])) + "<a:xp_orb:496424585990766602>")
                            break
                        await client.edit_message(msg2, "Vous possédez actuellement " + str(
                            larmes) + "<:Larme_de_lumiere:491215229594632193>")
                        if larmes == 0:
                            await client.remove_reaction(msg4, plus, client.user)
                        if c == 0:
                            await client.remove_reaction(msg4, moins, client.user)
                            await client.edit_message(msg4, ":bow_and_arrow:__Attaque à distance__ : lvl " + str(
                                tir) + "     <a:xp_orb:496424585990766602>" + str(int(perso[19])) + "/" + str(
                                int(perso[24])) + "<a:xp_orb:496424585990766602>")
                        else:
                            await client.edit_message(msg4, ":bow_and_arrow:__Attaque à distance__ : lvl " + str(
                                tir) + " +" + str(
                                c) + "<:Larme_de_lumiere:491215229594632193>" + "     <a:xp_orb:496424585990766602>" + str(
                                int(perso[19])) + "/" + str(int(perso[24])) + "<a:xp_orb:496424585990766602>")
                    perso[13] = str(c + tir) + "\n"
            if larmes != 0:
                if agi != 20:
                    await client.add_reaction(msg5, check)
                    if larmes != 0:
                        await client.add_reaction(msg5, plus)
                    c = 0
                    while a == 0:
                        res = await client.wait_for_reaction([moins, plus, check], user=user, message=msg5)
                        if res.reaction.emoji == plus:
                            c += 1
                            larmes -= 1
                            await client.remove_reaction(msg5, plus, user)
                            await client.add_reaction(msg5, moins)
                        elif res.reaction.emoji == moins:
                            c -= 1
                            larmes += 1
                            await client.remove_reaction(msg5, moins, user)
                            await client.add_reaction(msg5, plus)
                        elif res.reaction.emoji == check:
                            await client.remove_reaction(msg5, plus, client.user)
                            await client.remove_reaction(msg5, moins, client.user)
                            await client.remove_reaction(msg5, check, client.user)
                            await client.remove_reaction(msg5, check, user)
                            perso[25] = str(int(perso[25]) + 10 * c) + "\n"
                            await client.edit_message(msg5, ":cartwheel:__Agilité__ : lvl " + str(
                                c + agi) + "     <a:xp_orb:496424585990766602>" + str(int(perso[20])) + "/" + str(
                                int(perso[25])) + "<a:xp_orb:496424585990766602>")
                            break
                        await client.edit_message(msg2, "Vous possédez actuellement " + str(
                            larmes) + "<:Larme_de_lumiere:491215229594632193>")
                        if larmes == 0:
                            await client.remove_reaction(msg5, plus, client.user)
                        if c == 0:
                            await client.remove_reaction(msg5, moins, client.user)
                            await client.edit_message(msg5, ":cartwheel:__Agilité__ : lvl " + str(
                                agi) + "     <a:xp_orb:496424585990766602>" + str(int(perso[20])) + "/" + str(
                                int(perso[25])) + "<a:xp_orb:496424585990766602>")
                        else:
                            await client.edit_message(msg5,
                                                      ":cartwheel:__Agilité__ : lvl " + str(agi) + " +" + str(
                                                          c) + "<:Larme_de_lumiere:491215229594632193>" + "     <a:xp_orb:496424585990766602>" + str(
                                                          int(perso[20])) + "/" + str(
                                                          int(perso[25])) + "<a:xp_orb:496424585990766602>")
                    perso[14] = str(c + agi) + "\n"
            if larmes != 0:
                if blo != 20:
                    await client.add_reaction(msg6, check)
                    if larmes != 0:
                        await client.add_reaction(msg6, plus)
                    c = 0
                    while a == 0:
                        res = await client.wait_for_reaction([moins, plus, check], user=user, message=msg6)
                        if res.reaction.emoji == plus:
                            c += 1
                            larmes -= 1
                            await client.remove_reaction(msg6, plus, user)
                            await client.add_reaction(msg6, moins)
                        elif res.reaction.emoji == moins:
                            c -= 1
                            larmes += 1
                            await client.remove_reaction(msg6, moins, user)
                            await client.add_reaction(msg6, plus)
                        elif res.reaction.emoji == check:
                            await client.remove_reaction(msg6, plus, client.user)
                            await client.remove_reaction(msg6, moins, client.user)
                            await client.remove_reaction(msg6, check, client.user)
                            await client.remove_reaction(msg6, check, user)
                            perso[26] = str(int(perso[26]) + 10 * c) + "\n"
                            await client.edit_message(msg6, ":shield:__Défense__ : lvl " + str(
                                c + blo) + "     <a:xp_orb:496424585990766602>" + str(int(perso[21])) + "/" + str(
                                int(perso[26])) + "<a:xp_orb:496424585990766602>")
                            break
                        await client.edit_message(msg2, "Vous possédez actuellement " + str(
                            larmes) + "<:Larme_de_lumiere:491215229594632193>")
                        if larmes == 0:
                            await client.remove_reaction(msg6, plus, client.user)
                        if c == 0:
                            await client.remove_reaction(msg6, moins, client.user)
                            await client.edit_message(msg6, ":shield:__Défense__ : lvl " + str(
                                blo) + "     <a:xp_orb:496424585990766602>" + str(int(perso[21])) + "/" + str(
                                int(perso[26])) + "<a:xp_orb:496424585990766602>")
                        else:
                            await client.edit_message(msg6,
                                                      ":shield:__Défense__ : lvl " + str(blo) + " +" + str(
                                                          c) + "<:Larme_de_lumiere:491215229594632193>" + "     <a:xp_orb:496424585990766602>" + str(
                                                          int(perso[21])) + "/" + str(
                                                          int(perso[26])) + "<a:xp_orb:496424585990766602>")
                    perso[15] = str(c + blo) + "\n"
            if larmes != 0:
                if sma != 20:
                    await client.add_reaction(msg7, check)
                    if larmes != 0:
                        await client.add_reaction(msg7, plus)
                    c = 0
                    while a == 0:
                        res = await client.wait_for_reaction([moins, plus, check], user=user, message=msg7)
                        if res.reaction.emoji == plus:
                            c += 1
                            larmes -= 1
                            await client.remove_reaction(msg7, plus, user)
                            await client.add_reaction(msg7, moins)
                        elif res.reaction.emoji == moins:
                            c -= 1
                            larmes += 1
                            await client.remove_reaction(msg7, moins, user)
                            await client.add_reaction(msg7, plus)
                        elif res.reaction.emoji == check:
                            await client.remove_reaction(msg7, plus, client.user)
                            await client.remove_reaction(msg7, moins, client.user)
                            await client.remove_reaction(msg7, check, client.user)
                            await client.remove_reaction(msg7, check, user)
                            perso[27] = str(int(perso[27]) + 10 * c) + "\n"
                            await client.edit_message(msg7, ":bulb:__Intelligence__ : lvl " + str(
                                c + sma) + "     <a:xp_orb:496424585990766602>" + str(int(perso[22])) + "/" + str(
                                int(perso[27])) + "<a:xp_orb:496424585990766602>")
                            break
                        await client.edit_message(msg2, "Vous possédez actuellement " + str(
                            larmes) + "<:Larme_de_lumiere:491215229594632193>")
                        if larmes == 0:
                            await client.remove_reaction(msg7, plus, client.user)
                        if c == 0:
                            await client.remove_reaction(msg7, moins, client.user)
                            await client.edit_message(msg7, ":bulb:__Intelligence__ : lvl " + str(
                                sma) + "     <a:xp_orb:496424585990766602>" + str(int(perso[22])) + "/" + str(
                                int(perso[27])) + "<a:xp_orb:496424585990766602>")
                        else:
                            await client.edit_message(msg7, ":bulb:__Intelligence__ : lvl " + str(sma) + " +" + str(
                                c) + "<:Larme_de_lumiere:491215229594632193>" + "     <a:xp_orb:496424585990766602>" + str(
                                int(perso[22])) + "/" + str(
                                int(perso[27])) + "<a:xp_orb:496424585990766602>")
                    perso[16] = str(c + sma) + "\n"
            a = 1
        msg9 = await client.say("Sélectionnez cette réaction pour quitter l'arbre de compétences :")
        await client.add_reaction(msg9, quitter)
        await client.wait_for_reaction([quitter], user=user, message=msg9)
        await client.delete_message(msg)
        await client.delete_message(msg2)
        await client.delete_message(msg3)
        await client.delete_message(msg4)
        await client.delete_message(msg5)
        await client.delete_message(msg6)
        await client.delete_message(msg7)
        if a == 1:
            await client.delete_message(msg8)
        await client.delete_message(msg9)
        await client.say("Vous avez quitté votre arbre des compétences :arrow_right: :door:")
        perso[10] = str(larmes) + "\n"
        fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                       "w")
        a = 0
        while a == 0:
            if len(perso) == 0:
                break
            else:
                fichier.write(perso[0])
                del (perso[0])
        fichier.close()
    else:
        await client.say("Vous ne possédez pas de personnage. Pour en créer un, faites la commande `?newplayer`.")


@client.command(pass_context=True)
async def roll(ctx):
    A = int(random.uniform(1, 20))
    if A == 1:
        await client.say(":game_die::one: **REUSSITE CRITIQUE** :anger:")
    if A == 2:
        await client.say(":game_die::two:")
    if A == 3:
        await client.say(":game_die::three:")
    if A == 4:
        await client.say(":game_die::four:")
    if A == 5:
        await client.say(":game_die::five:")
    if A == 6:
        await client.say(":game_die::six:")
    if A == 7:
        await client.say(":game_die::seven:")
    if A == 8:
        await client.say(":game_die::eight:")
    if A == 9:
        await client.say(":game_die::nine:")
    if A == 10:
        await client.say(":game_die::keycap_ten: ")
    if A == 11:
        await client.say(":game_die::one::one:")
    if A == 12:
        await client.say(":game_die::one::two:")
    if A == 13:
        await client.say(":game_die::one::three:")
    if A == 14:
        await client.say(":game_die::one::four:")
    if A == 15:
        await client.say(":game_die::one::five:")
    if A == 16:
        await client.say(":game_die::one::six:")
    if A == 17:
        await client.say(":game_die::one::seven:")
    if A == 18:
        await client.say(":game_die::one::eight:")
    if A == 19:
        await client.say(":game_die::one::nine:")
    if A == 20:
        await client.say(":game_die::two::zero: **ECHEC CRITIQUE** :anger:")


@client.command(pass_context=True)
async def ratt(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        A = int(random.uniform(1, 20))
        if A == 1:
            player = ":one: : **REUSSITE CRITIQUE** :anger:"
        if A == 2:
            player = ":two:"
        if A == 3:
            player = ":three:"
        if A == 4:
            player = ":four:"
        if A == 5:
            player = ":five:"
        if A == 6:
            player = ":six:"
        if A == 7:
            player = ":seven:"
        if A == 8:
            player = ":eight:"
        if A == 9:
            player = ":nine:"
        if A == 10:
            player = ":keycap_ten: "
        if A == 11:
            player = ":one::one:"
        if A == 12:
            player = ":one::two:"
        if A == 13:
            player = ":one::three:"
        if A == 14:
            player = ":one::four:"
        if A == 15:
            player = ":one::five:"
        if A == 16:
            player = ":one::six:"
        if A == 17:
            player = ":one::seven:"
        if A == 18:
            player = ":one::eight:"
        if A == 19:
            player = ":one::nine:"
        if A == 20:
            player = ":two::zero: : **ECHEC CRITIQUE** :anger:"
        fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\valeurs armes.txt", "r")
        fichier2 = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités armes " + user.id + ".txt",
            "r")
        fichier3 = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + user.id + ".txt", "r")
        fichier4 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes.txt", "r")
        fichier5 = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        valeur = fichier.readlines()
        dura = fichier2.readlines()
        armes = fichier3.readlines()
        arme = fichier4.readlines()
        perso = fichier5.readlines()
        fichier.close()
        fichier2.close()
        fichier3.close()
        fichier4.close()
        fichier5.close()
        b = 0
        c = 0
        if perso[33] == "(rien)\n":
            phrase3 = "Vous attaquez avec vos poing, pas de durabilité perdue."
        else:
            b = 1
            for i in range(len(armes)):
                if perso[33] == armes[i]:
                    break
                else:
                    pass
            dura2 = int(dura[i])
            dura2 -= 1
            if dura2 == 0:
                phrase3 = "Votres arme s'est cassée ! :dagger::x:"
                del (dura[i])
                del (armes[i])
                perso[33] = "(rien)\n"
            else:
                phrase3 = "Durabilité de votre arme : " + str(dura2) + ":dagger:"
                dura[i] = str(dura2) + "\n"
        xp2 = int(perso[18])
        if A <= int(perso[12]):
            if b == 1:
                for j in range(len(armes)):
                    if arme[j] == perso[33]:
                        break
                    else:
                        pass
            if A == 1:
                phrase = "Coup critique ! Dégats multipliés par 2 ! :heavy_multiplication_x:**2**"
                xp2 += 2
                phrase4 = "+2<a:xp_orb:496424585990766602> au corps à corps !"
                if b == 1:
                    phrase2 = "Dégats infligés à l'ennemi : -" + str(int(valeur[j]) * 2) + "pv :broken_heart:"
                else:
                    phrase2 = "Dégats infligés à l'ennemi : -2pv :broken_heart:"
            else:
                phrase = "Attaque réussie ! :dagger::white_check_mark:"
                xp2 += 1
                phrase4 = "+1<a:xp_orb:496424585990766602> au corps à corps !"
                if b == 1:
                    phrase2 = "Dégats infligés à l'ennemi : -" + str(int(valeur[j])) + "pv :broken_heart:"
                else:
                    phrase2 = "Dégats infligés à l'ennemi : -1pv :broken_heart:"
        if A > int(perso[12]):
            phrase = "Attaque ratée ! :dagger::no_entry_sign:"
            if A == 20:
                phrase2 = "Vous êtes destabilisés et ne pouvez pas esquiver pendant le tour de l'ennemi."
                phrase4 = "+0<a:xp_orb:496424585990766602> en défense !"
            else:
                xp2 += 1
                phrase4 = "+1<a:xp_orb:496424585990766602> au corps à corps !"
        if b == 1:
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + user.id + ".txt", "w")
            fichier2 = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités armes " + user.id + ".txt",
                "w")
            a = 0
            while a == 0:
                if len(dura) == 0:
                    break
                else:
                    fichier.write(armes[0])
                    fichier2.write(dura[0])
                    del (armes[0])
                    del (dura[0])
            fichier.close()
            fichier2.close()
        if xp2 >= int(perso[23]):
            c = 1
            perso[23] = str(int(perso[23]) + 10) + "\n"
            perso[12] = str(int(perso[12]) + 1) + "\n"
            perso[18] = "0\n"
            perso[6] = str(int(perso[6]) + 1) + "\n"
            perso[5] = perso[6]
            phrase5 = "Level up ! :arrow_up: +1:heart: suplémentaire !"
        else:
            perso[18] = str(xp2) + "\n"
        if A <= int(perso[12]):
            if c == 1:
                await client.say(
                    "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4 + "\n" + phrase5)
            else:
                await client.say(
                    "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4)
        if A > int(perso[12]):
            if A == 20:
                if c == 1:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4 + "\n" + phrase5)
                else:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4)
            else:
                if c == 1:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase3 + "\n" + phrase4 + "\n" + phrase5)
                else:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase3 + "\n" + phrase4)
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
        a = 0
        while a == 0:
            if len(perso) == 0:
                break
            else:
                fichier.write(perso[0])
                del (perso[0])
        fichier.close()


@client.command(pass_context=True)
async def rblo(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        if perso[34] == "(rien)\n":
            await client.say(
                "Vous ne possédez pas de bouclier, vous ne pouuvez donc pas bloquer. Vous devez à la place faire la commande `?res` pour esquiver. :no_entry:")
        else:
            A = int(random.uniform(1, 20))
            if A == 1:
                player = ":one: : **REUSSITE CRITIQUE** :anger:"
            if A == 2:
                player = ":two:"
            if A == 3:
                player = ":three:"
            if A == 4:
                player = ":four:"
            if A == 5:
                player = ":five:"
            if A == 6:
                player = ":six:"
            if A == 7:
                player = ":seven:"
            if A == 8:
                player = ":eight:"
            if A == 9:
                player = ":nine:"
            if A == 10:
                player = ":keycap_ten: "
            if A == 11:
                player = ":one::one:"
            if A == 12:
                player = ":one::two:"
            if A == 13:
                player = ":one::three:"
            if A == 14:
                player = ":one::four:"
            if A == 15:
                player = ":one::five:"
            if A == 16:
                player = ":one::six:"
            if A == 17:
                player = ":one::seven:"
            if A == 18:
                player = ":one::eight:"
            if A == 19:
                player = ":one::nine:"
            if A == 20:
                player = ":two::zero: : **ECHEC CRITIQUE** :anger:"
            fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\valeurs boucliers.txt",
                           "r")
            fichier2 = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités boucliers " + user.id + ".txt",
                "r")
            fichier4 = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + user.id + ".txt",
                "r")
            fichier5 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers.txt", "r")
            valeur = fichier.readlines()
            dura = fichier2.readlines()
            bouclier = fichier4.readlines()
            boucliers = fichier5.readlines()
            fichier.close()
            fichier2.close()
            fichier4.close()
            fichier5.close()
            xp2 = int(perso[21])
            c = 0
            for i in range(len(bouclier)):
                if perso[34] == bouclier[i]:
                    break
                else:
                    pass
            if A != 1:
                dura[i] = str(int(dura[i]) - 1) + "\n"
                if int(dura[i]) == 0:
                    phrase3 = "Votre bouclier s'est cassé ! :shield::x:"
                    perso[34] = "(rien)\n"
                    del (bouclier[i])
                    del (dura[i])
                else:
                    phrase3 = "Durabilité de votre bouclier : " + str(int(dura[i])) + ":shield:"
                fichier = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + user.id + ".txt",
                    "w")
                fichier2 = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités boucliers " + user.id + ".txt",
                    "w")
                a = 0
                while a == 0:
                    if len(dura) == 0:
                        break
                    else:
                        fichier.write(bouclier[0])
                        fichier2.write(dura[0])
                        del (bouclier[0])
                        del (dura[0])
                fichier.close()
                fichier2.close()
            else:
                phrase3 = "Pas de durabilité perdue !"
            if A <= int(perso[15]):
                for j in range(len(boucliers)):
                    if boucliers[j] == perso[34]:
                        break
                    else:
                        pass
                if A == 1:
                    phrase = "Bloquage parfait ! Vous pouvez effectuer une riposte !"
                    phrase4 = "+2<a:xp_orb:496424585990766602> en défense !"
                    xp2 += 2
                else:
                    phrase = "Bloquage reussi ! :shield::white_check_mark:"
                    phrase4 = "+1<a:xp_orb:496424585990766602> en défense !"
                    xp2 += 1
                phrase2 = "Valeur du bouclier : `" + valeur[j] + "`"
            if A > int(perso[15]):
                if A == 20:
                    phrase = "Pas de chance... vous prenez le double des dégats en plus d'être déstabilisé. :no_entry::no_entry:"
                    phrase4 = "+0<a:xp_orb:496424585990766602> en défense !"
                else:
                    phrase = "Bloquage raté ! :shield::no_entry_sign:"
                    phrase4 = "+1<a:xp_orb:496424585990766602> en défense !"
                    xp2 += 1
            if xp2 >= int(perso[26]):
                c = 1
                perso[26] = str(int(perso[26] + 10)) + "\n"
                perso[15] = str(int(perso[15]) + 1) + "\n"
                perso[21] = "0\n"
                perso[6] = str(int(perso[6]) + 1) + "\n"
                perso[5] = perso[6]
                phrase5 = "Level up ! :arrow_up: +1:heart: suplémentaire !"
            else:
                perso[21] = str(xp2) + "\n"
            if A > int(perso[15]):
                if c == 1:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase3 + "\n" + phrase4 + "\n" + phrase5)
                else:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase3 + "\n" + phrase4)
            if A <= int(perso[15]):
                if c == 1:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4 + "\n" + phrase5)
                else:
                    await client.say(
                        "Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase4)
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(perso) == 0:
                    break
                else:
                    fichier.write(perso[0])
                    del (perso[0])
            fichier.close()


@client.command(pass_context=True)
async def ragi(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        A = int(random.uniform(1, 20))
        if A == 1:
            player = ":one: : **REUSSITE CRITIQUE** :anger:"
        if A == 2:
            player = ":two:"
        if A == 3:
            player = ":three:"
        if A == 4:
            player = ":four:"
        if A == 5:
            player = ":five:"
        if A == 6:
            player = ":six:"
        if A == 7:
            player = ":seven:"
        if A == 8:
            player = ":eight:"
        if A == 9:
            player = ":nine:"
        if A == 10:
            player = ":keycap_ten: "
        if A == 11:
            player = ":one::one:"
        if A == 12:
            player = ":one::two:"
        if A == 13:
            player = ":one::three:"
        if A == 14:
            player = ":one::four:"
        if A == 15:
            player = ":one::five:"
        if A == 16:
            player = ":one::six:"
        if A == 17:
            player = ":one::seven:"
        if A == 18:
            player = ":one::eight:"
        if A == 19:
            player = ":one::nine:"
        if A == 20:
            player = ":two::zero: : **ECHEC CRITIQUE** :anger:"
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        xp2 = int(perso[20])
        c = 0
        if A <= int(perso[14]):
            if A == 1:
                phrase2 = "+2<a:xp_orb:496424585990766602> en agilité !"
                xp2 += 2
            else:
                phrase2 = "+1<a:xp_orb:496424585990766602> en agilité !"
                xp2 += 1
            phrase = "Lancé d'agilité réussi ! :cartwheel::white_check_mark:"
        if A > int(perso[14]):
            if A == 20:
                phrase2 = "+0<a:xp_orb:496424585990766602> en agilité !"
            else:
                phrase2 = "+1<a:xp_orb:496424585990766602> en agilité !"
                xp2 += 1
            phrase = "Lancé d'agilité raté ! :cartwheel::no_entry_sign:"
        if xp2 == int(perso[25]):
            c = 1
            perso[25] = str(int(perso[25]) + 10) + "\n"
            perso[14] = str(int(perso[14]) + 1) + "\n"
            perso[20] = "0\n"
            perso[6] = str(int(perso[6]) + 1) + "\n"
            perso[5] = perso[6]
            phrase5 = "Level up ! :arrow_up: +1:heart: suplémentaire !"
        else:
            perso[20] = str(xp2) + "\n"
        if c == 1:
            await client.say("Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase5)
        else:
            await client.say("Vous avez fait " + player + "\n" + phrase + "\n" + phrase2)
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
        a = 0
        while a == 0:
            if len(perso) == 0:
                break
            else:
                fichier.write(perso[0])
                del (perso[0])
        fichier.close()


@client.command(pass_context=True)
async def rint(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        A = int(random.uniform(1, 20))
        if A == 1:
            player = ":one: : **REUSSITE CRITIQUE** :anger:"
        if A == 2:
            player = ":two:"
        if A == 3:
            player = ":three:"
        if A == 4:
            player = ":four:"
        if A == 5:
            player = ":five:"
        if A == 6:
            player = ":six:"
        if A == 7:
            player = ":seven:"
        if A == 8:
            player = ":eight:"
        if A == 9:
            player = ":nine:"
        if A == 10:
            player = ":keycap_ten: "
        if A == 11:
            player = ":one::one:"
        if A == 12:
            player = ":one::two:"
        if A == 13:
            player = ":one::three:"
        if A == 14:
            player = ":one::four:"
        if A == 15:
            player = ":one::five:"
        if A == 16:
            player = ":one::six:"
        if A == 17:
            player = ":one::seven:"
        if A == 18:
            player = ":one::eight:"
        if A == 19:
            player = ":one::nine:"
        if A == 20:
            player = ":two::zero: : **ECHEC CRITIQUE** :anger:"
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        xp2 = int(perso[22])
        c = 0
        if A <= int(perso[16]):
            if A == 1:
                phrase2 = "+2<a:xp_orb:496424585990766602> en intelligence !"
                xp2 += 2
            else:
                phrase2 = "+1<a:xp_orb:496424585990766602> en intelligence !"
                xp2 += 1
            phrase = "Lancé d'intelligence réussi ! :bulb::white_check_mark:"
        if A > int(perso[16]):
            if A == 20:
                phrase2 = "+0<a:xp_orb:496424585990766602> en intelligence !"
            else:
                phrase2 = "+1<a:xp_orb:496424585990766602> en intelligence !"
                xp2 += 1
            phrase = "Lancé d'intelligence raté ! :bulb::no_entry_sign:"
        if xp2 >= int(perso[27]):
            c = 1
            perso[27] = str(int(perso[27] + 10)) + "\n"
            perso[16] = str(int(perso[16]) + 1) + "\n"
            perso[22] = "0\n"
            perso[6] = str(int(perso[6]) + 1) + "\n"
            perso[5] = perso[6]
            phrase5 = "Level up ! :arrow_up: +1:heart: suplémentaire !"
        else:
            perso[22] = str(xp2) + "\n"
        if c == 1:
            await client.say("Vous avez fait " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase5)
        else:
            await client.say("Vous avez fait " + player + "\n" + phrase + "\n" + phrase2)
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
        a = 0
        while a == 0:
            if len(perso) == 0:
                break
            else:
                fichier.write(perso[0])
                del (perso[0])
        fichier.close()


@client.command(pass_context=True)
async def rtir(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        if perso[35] == "(rien)\n":
            await client.say("Vous n'avez pas d'arc d'équipé, vous ne pouvez donc pas tirer de flèches. :no_entry:")
        else:
            A = int(random.uniform(1, 20))
            if A == 1:
                player = ":one: : **REUSSITE CRITIQUE** :anger:"
            if A == 2:
                player = ":two:"
            if A == 3:
                player = ":three:"
            if A == 4:
                player = ":four:"
            if A == 5:
                player = ":five:"
            if A == 6:
                player = ":six:"
            if A == 7:
                player = ":seven:"
            if A == 8:
                player = ":eight:"
            if A == 9:
                player = ":nine:"
            if A == 10:
                player = ":keycap_ten: "
            if A == 11:
                player = ":one::one:"
            if A == 12:
                player = ":one::two:"
            if A == 13:
                player = ":one::three:"
            if A == 14:
                player = ":one::four:"
            if A == 15:
                player = ":one::five:"
            if A == 16:
                player = ":one::six:"
            if A == 17:
                player = ":one::seven:"
            if A == 18:
                player = ":one::eight:"
            if A == 19:
                player = ":one::nine:"
            if A == 20:
                player = ":two::zero: : **ECHEC CRITIQUE** :anger:"
            fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\valeurs arcs.txt", "r")
            fichier2 = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités arcs " + user.id + ".txt",
                "r")
            fichier3 = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + user.id + ".txt", "r")
            fichier4 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs.txt", "r")
            valeur = fichier.readlines()
            dura = fichier2.readlines()
            arc = fichier3.readlines()
            arcs = fichier4.readlines()
            fichier.close()
            fichier2.close()
            fichier3.close()
            fichier4.close()
            c = 0
            for i in range(len(arc)):
                if perso[35] == arc[i]:
                    break
                else:
                    pass
            if A == 1:
                phrase3 = "Pas de durabilité perdue !"
            else:
                dura2 = int(dura[i]) - 1
                if dura2 == 0:
                    phrase3 = "Votre arc s'est cassé ! :bow_and_arrow::x:"
                    perso[35] = "(rien)\n"
                    del (arc[i])
                    del (dura[i])
                else:
                    phrase3 = "Durabilité de votre arc : " + str(dura2) + ":bow_and_arrow:"
                    dura[i] = str(dura2) + "\n"
                fichier = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités arcs " + user.id + ".txt",
                    "w")
                fichier2 = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + user.id + ".txt",
                    "w")
                a = 0
                while a == 0:
                    if len(dura) == 0:
                        break
                    else:
                        fichier.write(dura[0])
                        fichier2.write(arc[0])
                        del (dura[0])
                        del (arc[0])
                fichier.close()
                fichier2.close()
            for j in range(len(arcs)):
                if arcs[j] == perso[35]:
                    break
                else:
                    pass
            xp2 = int(perso[19])
            if A > int(perso[13]):
                if A == 20:
                    phrase = "Vous n'arrivez pas à tirer à l'arc, votre flèche se plante dans le sol juste devant vous. :no_entry:"
                    phrase2 = "+0<a:xp_orb:496424585990766602> en tir !"
                else:
                    phrase = "Vous ratez votre tir. :bow_and_arrow::dash:"
                    phrase2 = "+1<a:xp_orb:496424585990766602> en tir !"
                    xp2 += 1
            if A <= int(perso[13]):
                if A == 1:
                    phrase = "Tir en pleine tête ! Dégats doublés ! :bow_and_arrow::skull:\nDégats infligés : -" + str(
                        int(valeur[j]) * 2) + "pv :broken_heart:"
                    phrase2 = "+2<a:xp_orb:496424585990766602> en tir !"
                    xp2 += 2
                else:
                    phrase = "Tir réussi ! :bow_and_arrow:\nFaites `?roll` si votre ennemi a un bouclier et que vous êtes en combat.\nDégats infligés : -" + str(
                        int(valeur[j])) + "pv :broken_heart:"
                    phrase2 = "+1<a:xp_orb:496424585990766602> en tir !"
                    xp2 += 1
            if xp2 == int(perso[24]):
                c = 1
                perso[24] = str(int(perso[24] + 10)) + "\n"
                perso[13] = str(int(perso[13]) + 1) + "\n"
                perso[19] = "0\n"
                perso[6] = str(int(perso[6]) + 1) + "\n"
                perso[5] = perso[6]
                phrase5 = "Level up ! :arrow_up: +1:heart: suplémentaire !"
            else:
                perso[19] = str(xp2) + "\n"
            if c == 1:
                await client.say(
                    "Vous faites un " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3 + "\n" + phrase5)
            else:
                await client.say("Vous faites un " + player + "\n" + phrase + "\n" + phrase2 + "\n" + phrase3)
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(perso) == 0:
                    break
                else:
                    fichier.write(perso[0])
                    del (perso[0])
            fichier.close()


@client.command(pass_context=True)
async def life(ctx):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        await client.say("PV restant de " + user.mention + " : :heart:" + str(int(perso[5])) + "/" + str(int(perso[6])))
    else:
        await client.say("Vous ne possédez pas de personnage, faite `?newplayer` pour en créer un. :no_entry:")


@client.command(pass_context=True)
async def pcadd(ctx, member: discord.Member):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(member.id) + "\n":
            b = 1
            break
        else:
            pass
    if user.server_permissions.administrator:
        if b == 1:
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "r")
            perso = fichier.readlines()
            fichier.close()
            perso[6] = str(int(perso[6]) + 1) + "\n"
            perso[5] = perso[6]
            perso[10] = str(int(perso[10]) + 1) + "\n"
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(perso) == 0:
                    break
                else:
                    fichier.write(perso[0])
                    del (perso[0])
            fichier.close()
            await client.say(
                member.mention + " a récupéré une larme de lumière <:Larme_de_lumiere:491215229594632193> ! +1:heart: supplémentaire")
        else:
            await client.say(
                "La personne à qui vous essayez de donner de la vitalité ne possède pas de personnage. :no_entry_sign:")
    else:
        await client.say("Vous n'avez pas l'autorisation d'utiliser cette commande. :no_entry:")


#@client.event
#async def on_command_error(error, ctx):
    #if isinstance(error, commands.MissingRequiredArgument):
        #await client.send_message(ctx.message.channel,
                                  #"Un ou plusieurs arguments sont manquant. :no_entry_sign:\nFaites `?help` si vous avez besoin d'aide, ou bien `?h` suivit du nom de la commande pour avoir plus de détails.")
    #elif isinstance(error, commands.BadArgument):
        #await client.send_message(ctx.message.channel,
                                  #"Un ou plusieurs arguments ont mal été indiqués. :no_entry_sign:\nFaites `?help` si vous avez besoin d'aide, ou bien `?h` suivit du nom de la commande pour avoir plus de détails.")
    #if isinstance(error, commands.CommandNotFound):
        #await client.send_message(ctx.message.channel,
                                  #"Cette commande n'existe pas. :no_entry_sign:\nPour voir la liste des commandes disponibles, faites `?help`.")


@client.command(pass_context=True)
async def pcremove(ctx, member: discord.Member, content: str):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    c = 0
    for i in range(len(player)):
        if player[i] == str(member.id) + "\n":
            b = 1
            break
        else:
            pass
    if user.server_permissions.administrator:
        if b == 1:
            if content == "cac" or content == "tir" or content == "blo" or content == "agi" or content == "int" or content == "larme":
                fichier = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt",
                    "r")
                perso = fichier.readlines()
                fichier.close()
                perso[6] = str(int(perso[6]) - 1) + "\n"
                if int(perso[5]) > int(perso[6]):
                    perso[5] = perso[6]
                if content == "larme":
                    perso[10] = str(int(perso[10]) - 1) + "\n"
                    phrase = member.mention + " vient de perdre une larme de lumière ! <:Larme_de_lumiere:491215229594632193> :x:"
                    await client.say(phrase + "\n1:heart: en moins :broken_heart:")
                else:
                    if content == "cac":
                        if int(perso[12]) == 0:
                            c = 1
                        else:
                            perso[12] = str(int(perso[12]) - 1) + "\n"
                            perso[23] = str(int(perso[23]) - 10) + "\n"
                            perso[18] = "0\n"
                            comp = "corps à corps :dagger:"
                    if content == "tir":
                        if int(perso[13]) == 0:
                            c = 1
                        else:
                            perso[13] = str(int(perso[13]) - 1) + "\n"
                            perso[24] = str(int(perso[24]) - 10) + "\n"
                            perso[19] = "0\n"
                            comp = "tir :bow_and_arrow:"
                    if content == "agi":
                        if int(perso[14]) == 0:
                            c = 1
                        else:
                            perso[14] = str(int(perso[14]) - 1) + "\n"
                            perso[25] = str(int(perso[25]) - 10) + "\n"
                            perso[20] = "0\n"
                            comp = "agilité :cartwheel:"
                    if content == "blo":
                        if int(perso[15]) == 0:
                            c = 1
                        else:
                            perso[15] = str(int(perso[15]) - 1) + "\n"
                            perso[26] = str(int(perso[26]) - 10) + "\n"
                            perso[21] = "0\n"
                            comp = "blocage :shield:"
                    if content == "int":
                        if int(perso[16]) == 0:
                            c = 1
                        else:
                            perso[16] = str(int(perso[16]) - 1) + "\n"
                            perso[27] = str(int(perso[27]) - 10) + "\n"
                            perso[22] = "0\n"
                            comp = "intelligence :bulb:"
                    if c == 1:
                        await client.say(
                            "Aucun point de compétence n'a été attribué dans cette aptitude, vous ne pouvez donc pas en retirer. :no_entry_sign:")
                    else:
                        phrase = member.mention + " vient de perdre un niveau en " + comp + ":arrow_down:"
                        await client.say(phrase + "\n1:heart: en moins :broken_heart:")
                fichier = open(
                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt",
                    "w")
                a = 0
                while a == 0:
                    if len(perso) == 0:
                        break
                    else:
                        fichier.write(perso[0])
                        del (perso[0])
                fichier.close()
            else:
                await client.say("Veuillez essayer les termes `cac`, `tir`, `blo`, `agi`, `int` ou `larme`")
        else:
            await client.say(
                "La personne à qui vous essayez de retirer de la vitalité ne possède pas de personnage. :no_entry_sign:")
    else:
        await client.say("Vous n'avez pas l'autorisation d'utiliser cette commande. :no_entry:")


@client.command(pass_context=True)
async def hit(ctx, member: discord.Member, nombre: int):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    c = 0
    d = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
        if player[i] == str(member.id) + "\n":
            d = 1
        if c == 1 and d == 1:
            break
        else:
            pass
    if (c == 1 and d == 1) or user.server_permissions.administrator:
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        if perso[5] == "0\n":
            await client.say(
                "Le personnage de " + member.mention + " est mort, il ne peut pas perdre plus de dégâts. :skull:")
        else:
            total = int(perso[5]) - nombre
            if total <= 0:
                phrase = "Vos pv sont arrivés à 0... C'est ici que votre aventure s'arrête :skull:"
                perso[5] = "0\n"
            else:
                phrase = "Il vous reste au total " + str(total) + "pv :heart:"
                perso[5] = str(total) + "\n"
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(perso) == 0:
                    break
                else:
                    fichier.write(perso[0])
                    del (perso[0])
            fichier.close()
            await client.say(member.mention + " s'est fait toucher. -" + str(nombre) + "pv :broken_heart:\n" + phrase)
    elif c == 1:
        await client.say("La personne à qui vous essayez de retirer de la vie ne possède pas de personnage. :no_entry:")
    elif d == 1:
        await client.say("Vous ne possédez pas de personnage, vous ne pouvez donc pas infliger de dégats. :no_entry:")
    else:
        await client.say("Aucun de vous deux ne possède de personnage. :no_entry:")


@client.command(pass_context=True)
async def regen(ctx, member: discord.Member, nombre: int):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    c = 0
    d = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
        if player[i] == str(member.id) + "\n":
            d = 1
        if c == 1 and d == 1:
            break
        else:
            pass
    if (c == 1 and d == 1) or user.server_permissions.administrator:
        fichier = open(
            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "r")
        perso = fichier.readlines()
        fichier.close()
        if perso[5] == "0\n":
            await client.say("Le personnage de " + member.mention + " est mort, il ne peut pas se régénérer. :skull:")
        elif perso[5] == perso[6]:
            await client.say("Vos pv sont déjà au maximum :no_entry_sign:")
        else:
            total = int(perso[5]) + nombre
            if total >= int(perso[6]):
                perso[5] = perso[6]
                phrase = "Pv complétement régénérés :sparkling_heart:"
            else:
                perso[5] = str(total) + "\n"
                phrase = "Vos pv : " + str(total) + "/" + str(perso[6]) + ":heart:"
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(perso) == 0:
                    break
                else:
                    fichier.write(perso[0])
                    del (perso[0])
            fichier.close()
            await client.say(member.mention + " s'est régénéré de " + str(nombre) + "pv :heart:\n" + phrase)
    elif c == 1:
        await client.say(
            "La personne à qui vous essayez de régénérer de la vie ne possède pas de personnage. :no_entry:")
    elif d == 1:
        await client.say("Vous ne possédez pas de personnage, vous ne pouvez donc pas régénérer de la vie. :no_entry:")
    else:
        await client.say("Aucun de vous deux ne possède de personnage. :no_entry:")


@client.command(pass_context=True)
async def invadd(ctx, member: discord.Member, message):
    user = ctx.message.author
    server = ctx.message.server
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(member.id) + "\n":
            b = 1
            break
        else:
            pass
    if user.server_permissions.administrator:
        if b == 1:
            await client.say(
                "Quel est le type de l'objet que vous voulez ajouter ?\n(Ecrivez `matériaux`:apple:, `arme`:dagger:, `bouclier`:shield:, `arc`:bow_and_arrow: ou `quête`:key2:, ou bien `exit` si vous voulez quitter la commande.)")
            fichier = open(
                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + member.id + ".txt", "r")
            perso = fichier.readlines()
            fichier.close()
            a = 0
            while a == 0:
                msg = await client.wait_for_message(author=user, channel=ctx.message.channel)
                if msg.content == "exit" or msg.content == "Exit":
                    await client.say("Vous quitter l'ajout d'objet...")
                    break
                if msg.content == "matériaux" or msg.content == "materiaux" or msg.content == "Matériaux" or msg.content == "Materiaux":
                    fichier = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\matériaux " + member.id + ".txt",
                        "a")
                    fichier.write(message + "\n")
                    fichier.close()
                    await client.say(
                        message + " a été ajouté à l'inventaire de " + member.mention + " avec succès ! :inbox_tray:")
                    break
                if msg.content == "quete" or msg.content == "quête" or msg.content == "Quete" or msg.content == "Quête":
                    fichier = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\quete " + member.id + ".txt",
                        "a")
                    fichier.write(message + "\n")
                    fichier.close()
                    await client.say(
                        message + " a été ajouté à l'inventaire de " + member.mention + " avec succès ! :inbox_tray:")
                    break
                if msg.content == "arme" or msg.content == "Arme":
                    fichier = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + member.id + ".txt",
                        "r")
                    fichier2 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes.txt",
                                    "r")
                    armes = fichier.readlines()
                    arme = fichier2.readlines()
                    fichier.close()
                    fichier2.close()
                    c = 0
                    for j in range(len(arme)):
                        if arme[j] == message + "\n":
                            c = 1
                            break
                        else:
                            pass
                    if c == 0:
                        await client.say("Cette arme n'existe pas. :no_entry_sign:")
                        break
                    else:
                        if len(armes) == int(perso[29]):
                            await client.say(
                                "Vous ne pouvez pas transporter plus d'armes ! :no_entry_sign: Libérez de la place pour ramasser cette arme.\n(Faites la commande `?invrem` pour vous débarasser d'un objet)")
                        else:
                            fichier = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + member.id + ".txt",
                                "a")
                            fichier2 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités armes " + member.id + ".txt",
                                "a")
                            fichier3 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités armes.txt",
                                "r")
                            dura = fichier3.readlines()
                            fichier.write(arme[j])
                            fichier2.write(dura[j])
                            fichier.close()
                            fichier2.close()
                            fichier3.close()
                            await client.say(
                                message + " a été ajouté à l'inventaire de " + member.mention + " avec succès ! :inbox_tray:")
                        break
                if msg.content == "bouclier" or msg.content == "Bouclier":
                    fichier = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + member.id + ".txt",
                        "r")
                    fichier2 = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers.txt", "r")
                    boucliers = fichier.readlines()
                    bouclier = fichier2.readlines()
                    fichier.close()
                    fichier2.close()
                    c = 0
                    for j in range(len(bouclier)):
                        if bouclier[j] == message + "\n":
                            c = 1
                            break
                        else:
                            pass
                    if c == 0:
                        await client.say("Ce bouclier n'existe pas. :no_entry_sign:")
                        break
                    else:
                        if len(boucliers) == int(perso[30]):
                            await client.say(
                                "Vous ne pouvez pas transporter plus de boucliers ! :no_entry_sign: Libérez de la place pour ramasser ce bouclier.\n(Faites la commande `?invrem` pour vous débarasser d'un objet)")
                        else:
                            fichier = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + member.id + ".txt",
                                "a")
                            fichier2 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités boucliers " + member.id + ".txt",
                                "a")
                            fichier3 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités boucliers.txt",
                                "r")
                            dura = fichier3.readlines()
                            fichier.write(bouclier[j])
                            fichier2.write(dura[j])
                            fichier.close()
                            fichier2.close()
                            fichier3.close()
                            await client.say(
                                message + " a été ajouté à l'inventaire de " + member.mention + " avec succès ! :inbox_tray:")
                        break
                if msg.content == "arc" or msg.content == "Arc":
                    fichier = open(
                        "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + member.id + ".txt",
                        "r")
                    fichier2 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs.txt",
                                    "r")
                    arcs = fichier.readlines()
                    arc = fichier2.readlines()
                    fichier.close()
                    fichier2.close()
                    c = 0
                    for j in range(len(arc)):
                        if arc[j] == message + "\n":
                            c = 1
                            break
                        else:
                            pass
                    if c == 0:
                        await client.say("Cet arc n'existe pas. :no_entry_sign:")
                        break
                    else:
                        if len(arcs) == int(perso[31]):
                            await client.say(
                                "Vous ne pouvez pas transporter plus d'armes ! :no_entry_sign: Libérez de la place pour ramasser cette arme.\n(Faites la commande `?invrem` pour vous débarasser d'un objet)")
                        else:
                            fichier = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + member.id + ".txt",
                                "a")
                            fichier2 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités arcs " + member.id + ".txt",
                                "a")
                            fichier3 = open(
                                "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\durabilités arcs.txt",
                                "r")
                            dura = fichier3.readlines()
                            fichier.write(arc[j])
                            fichier2.write(dura[j])
                            fichier.close()
                            fichier2.close()
                            fichier3.close()
                            await client.say(
                                message + " a été ajouté à l'inventaire de " + member.mention + " avec succès ! :inbox_tray:")
                        break
                else:
                    await client.say("Saisie inccorecte, veuillez entrer une nouvelle fois le type d'objet. :no_entry:")
        if b == 0:
            await client.say(
                "Vous ne possédez pas d'inventaire :no_entry:, créez tout d'abord un personnage avec `?newplayer` pour ensuite pouvoir ajouter ou retirer des objets.")
    else:
        await client.say("Vous n'avez pas l'autorisation d'utiliser cette commande. :no_entry:")


@client.command(pass_context=True)
async def equip(ctx, message):
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
        fichier = open("armes " + user.id + ".txt", "r")
        fichier2 = open("boucliers " + user.id + ".txt", "r")
        fichier3 = open("arcs " + user.id + ".txt", "r")
        armes = fichier.readlines()
        boucliers = fichier2.readlines()
        arcs = fichier3.readlines()
        fichier.close()
        fichier2.close()
        fichier3.close()
        b = 0
        for i in range(len(armes)):
            if message + "\n" == armes[i]:
                objet = armes[i]
                b = 1
                place = 0
                break
            else:
                pass
        for i in range(len(boucliers)):
            if message + "\n" == boucliers[i]:
                objet = boucliers[i]
                b = 1
                place = 1
                break
            else:
                pass
        for i in range(len(arcs)):
            if message + "\n" == arcs[i]:
                objet = arcs[i]
                b = 1
                place = 2
                break
            else:
                pass
        if b == 1:
            fichier = open("équipement " + user.id + ".txt", "r")
            equip = fichier.readlines()
            fichier.close()
            if equip[place] == objet:
                await client.say("Vous êtes déjà équipé de cet objet. :no_entry_sign:")
            else:
                if equip[place] == "(rien)\n":
                    phrase = user.mention + " s'est équipé de son " + message + " :dagger::inbox_tray:"
                else:
                    phrase = user.mention + " s'est déséquipé de son " + equip[
                        place] + "Puis s'équipe de son " + message + " :dagger::inbox_tray:"
                equip[place] = objet
                fichier = open("équipement " + user.id + ".txt", "w")
                a = 0
                while a == 0:
                    if len(equip) == 0:
                        break
                    else:
                        fichier.write(equip[0])
                        del (equip[0])
                fichier.close()
                await client.say(phrase)
        else:
            await client.say("Vous ne possédez pas cet objet. :no_entry_sign:")
    else:
        await client.say(
            "Pour vous équiper d'objet, vous devez tout d'abord créer un personnage avec la commande `?newplayer`. :no_entry:")


@client.command(pass_context=True)
async def unequip(ctx, message):
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
        fichier = open("équipement " + user.id + ".txt", "r")
        equip = fichier.readlines()
        fichier.close()
        b = 0
        for j in range(len(equip)):
            if message + "\n" == equip[j]:
                b = 1
                break
            else:
                pass
        if b == 1:
            equip[j] = "(rien)\n"
            fichier = open("équipement " + user.id + ".txt", "w")
            a = 0
            while a == 0:
                if len(equip) == 0:
                    break
                else:
                    fichier.write(equip[0])
                    del (equip[0])
            fichier.close()
            await client.say(user.mention + " a remit son " + message + " dans son sac. :dagger::outbox_tray:")
        else:
            await client.say("Vous n'avez pas cet objet d'équipé sur vous. :no_entry_sign:")
    else:
        await client.say(
            "Pour gérer votre équipement, il est nécéssaire de créer un personnage grâce à la commande `?newplayer`. :no_entry:")


@client.command(pass_context=True)
async def invequip(ctx):
    user = ctx.message.author
    server = ctx.message.server
    c = 0
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
            break
        else:
            pass
    if c == 1:
        fichier = open("équipement " + user.id + ".txt", "r")
        equip = fichier.readlines()
        fichier.close()
        if equip[0] == "(rien)\n" and equip[1] == "(rien)\n" and equip[2] == "(rien)\n":
            await client.say("Vous avez aucun objet d'équipé. :no_entry_sign:")
        else:
            await client.say(
                "**:dagger: Equipement de " + user.mention + " :**\n__Arme__ : " + equip[0] + "__Bouclier__ : " + equip[
                    1] + "__Arc__ : " + equip[2])
    else:
        await client.say(
            "Pour posséder un équipement, il est nécessaire pour vous de créer un personnage avec la commande `?newplayer`. :no_entry:")


@client.command(pass_context=True)
async def moneygive(ctx, member: discord.Member, nombre: int):
    user = ctx.message.author
    c = 0
    d = 0
    fichier = open("id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            n = i
            c = 1
        if player[i] == str(member.id) + "\n":
            m = i
            d = 1
        if c == 1 and d == 1:
            break
        else:
            pass
    if user.id == member.id:
        await client.say("Vous ne pouvez pas vous donner de l'argent à vous même. :no_entry_sign:")
    elif c == 1 and d == 1:
        fichier = open("bourse.txt", "r")
        bourse = fichier.readlines()
        fichier.close()
        if int(bourse[n]) < nombre:
            await client.say(
                "Vous n'avez pas assez de rubis dans votre bourse pour donner à la personne ce montant. :no_entry_sign:")
        else:
            total1 = int(bourse[n]) - nombre
            total2 = int(bourse[m]) + nombre
            bourse[n] = str(total1) + "\n"
            bourse[m] = str(total2) + "\n"
            fichier = open("bourse.txt", "w")
            a = 0
            while a == 0:
                if len(bourse) == 0:
                    break
                else:
                    fichier.write(bourse[0])
                    del (bourse[0])
            fichier.close()
            await client.say(
                user.mention + " a donné " + str(
                    nombre) + "<:Rubis_Vert:489369798849855498> à " + member.mention + " :handshake:")
    elif c == 1:
        await client.say(
            "La personne à qui vous essayez de donner de l'argent ne possède pas de personnage. :no_entry:")
    elif d == 1:
        await client.say(
            "Vous ne possédez pas de bourse. Pour en obtenir une, créez un personnage grâce à la commande `?newplayer` :no_entry:")
    else:
        await client.say(
            "Vous et la personne à qui vous essayez de donner de l'argent ne possédez pas de personnages. Faites la commande `?newplayer` pour en créer un. :no_entry:")


@client.command(pass_context=True)
async def freemoney(ctx, member: discord.Member, nombre: int):
    user = ctx.message.author
    role_names = [role.name for role in user.roles]
    c = 0
    fichier = open("id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    for i in range(len(player)):
        if player[i] == str(member.id) + "\n":
            c = 1
            break
        else:
            pass
    if "Moderateur" in role_names or "Createur" in role_names:
        if c == 1:
            fichier = open("bourse.txt", "r")
            bourse = fichier.readlines()
            fichier.close()
            total = int(bourse[i]) + nombre
            bourse[i] = str(total) + "\n"
            fichier = open("bourse.txt", "w")
            a = 0
            while a == 0:
                if len(bourse) == 0:
                    break
                else:
                    fichier.write(bourse[0])
                    del (bourse[0])
            fichier.close()
            if nombre == 1:
                await client.say(
                    str(nombre) + "<:Rubis_Vert:489369798849855498> a été ajouté à la bourse de " + member.mention)
            else:
                await client.say(
                    str(nombre) + "<:Rubis_Vert:489369798849855498> ont été ajouté à la bourse de " + member.mention)
        else:
            await client.say(
                "La personne à qui vous essayez de donner de l'argent ne possède pas de personnage. :no_entry:")
    else:
        await client.say("Vous n'avez pas l'autorisation d'utiliser cette commande. :no_entry_sign:")


@client.command(pass_context=True)
async def moneyspend(ctx, nombre: int):
    user = ctx.message.author
    fichier = open("id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    c = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
            break
        else:
            pass
    if c == 1:
        fichier = open("bourse.txt", "r")
        argent = "de rubis"
        bourse = fichier.readlines()
        fichier.close()
        if int(bourse[i]) < nombre:
            await client.say("Vous n'avez pas assez " + argent + " pour dépenser cette somme là. :no_entry_sign:")
        else:
            total = int(bourse[i]) - nombre
            bourse[i] = str(total) + "\n"
            fichier = open("bourse.txt", "w")
            a = 0
            while a == 0:
                if len(bourse) == 0:
                    break
                else:
                    fichier.write(bourse[0])
                    del (bourse[0])
            fichier.close()
            await client.say(user.mention + " a dépensé " + str(nombre) + "<:Rubis_Vert:489369798849855498>")
    else:
        await client.say(
            "Vous ne possédez pas de personnage. Faites `?newplayer` pour en créer un et obtenir une bourse. :no_entry:")


@client.command(pass_context=True)
async def money(ctx):
    user = ctx.message.author
    fichier = open("id.txt", "r")
    player = fichier.readlines()
    fichier.close()
    c = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            c = 1
            break
        else:
            pass
    if c == 1:
        fichier = open("bourse.txt", "r")
        bourse = fichier.readlines()
        fichier.close()
        money = int(bourse[i])
        money = str(money)
        if bourse[i] == "0\n":
            await client.say("Votre bourse est vide :no_entry_sign:")
        else:
            await client.say("Bourse de " + user.mention + " :\n" + money + "<:Rubis_Vert:489369798849855498>")
    else:
        await client.say(
            "Vous ne possédez pas de bourse. Pour en obtenir une, créez un personnage avec la commande `?newplayer`. :no_entry:")


@client.command(pass_context=True)
async def perso(ctx):
    user = ctx.message.author
    server = ctx.message.server
    dagger = "\U0001F5E1"
    shield = "\U0001F6E1"
    bow = "\U0001F3F9"
    arrow = discord.utils.get(client.get_all_emojis(), name='Fleches')
    mat = "\U0001F48E"
    quest = "\U0001F5DD"
    supr = "\U0001F4E4"
    add = "\U0001F4E5"
    info = "\U00002139"
    give = "\U0001F91D"
    equip2 = "\U00002694"
    down = "\U00002B07"
    up = "\U00002B06"
    yes = "\U00002705"
    no = "\U0001F6AB"
    money = "\U0001F4B0"
    pack = "\U0001F4E6"
    skill = discord.utils.get(client.get_all_emojis(), name='Larme_de_lumiere')
    fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\id.txt", "r")
    fichier2 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt",
                    "r")
    fichier3 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes " + user.id + ".txt", "r")
    fichier4 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers " + user.id + ".txt", "r")
    fichier5 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs " + user.id + ".txt", "r")
    fichier6 = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\flèches " + user.id + ".txt", "r")
    player = fichier.readlines()
    perso = fichier2.readlines()
    armes = fichier3.readlines()
    bouc = fichier4.readlines()
    arc = fichier5.readlines()
    fleche = fichier6.readlines()
    fichier.close()
    fichier2.close()
    fichier3.close()
    fichier4.close()
    fichier5.close()
    fichier6.close()
    b = 0
    for i in range(len(player)):
        if player[i] == str(user.id) + "\n":
            b = 1
            break
        else:
            pass
    if b == 1:
        msg = await client.say("```Ceci est l'interface de gestion de votre personnage. Vous pouvez grâce à celle-ci vérifier votre argent, votre vie, votre équipement... Finalement tout ce dont vous avez à savoir sur votre personnage ! Ce menu est intéractif, et vous pouvez gérer facilement votre personnages grâce aux réactions.```\n\n**Nom :** " + perso[0] + "**Age :** " + perso[1] + "**Sexe :** " + perso[2] + "**Race :** " + perso[3] + "\n:moneybag: **:** " + perso[8] + "<:Larme_de_lumiere:491215229594632193> **:** " + perso[10] + ":heart: **:** " + perso[5] + " / " + perso[6] + "\n:dagger::package: **:** " + str(len(armes)) + "/" + perso[29] + "\n:shield::package: **:** " + str(len(bouc)) + "/" + perso[30] + "\n:bow_and_arrow::package: **:** " + str(len(arc)) + "/" + perso[31] + "\n\n```Que voulez-vous faire ?\n:moneybag: : Pour gérer votre argent\n:package: : Pour gérer votre inventaire\n:crossed_swords: : Pour gérer votre équipement\n<:Larme_de_lumiere:491215229594632193> : Pour gérer vos compétences\n:no_entry_sign: : Pour quitter l'interface")
        await client.add_reaction(msg, money)
        await client.add_reaction(msg, pack)
        await client.add_reaction(msg, equip2)
        await client.add_reaction(msg, skill)
        await client.add_reaction(msg, no)
        res = await client.wait_for_reaction([money, pack, equip2, skill, no], user=user, message=msg)
        await client.delete_message(msg)
        if res.reaction.emoji == money:
            msg = await client.say("```Ce menu vous permet de gérer votre argent. Vous pouvez dépenser (dans le contexte du rp), ou bien donner de l'argent à un autre joueur.```\n\nVotres solde est d'actuellement de :\n" + str(int(perso[8])) + "<:Rubis_Vert:489369798849855498>\n\nQue voulez-vous faire ?\n:outbox_tray: : Pour retirer de l'argent\n:handshake: : Pour donner de l'argent à quelqu'un\n:no_entry_sign: : Pour quitter l'interface")
            await client.add_reaction(msg, supr)
            await client.add_reaction(msg, give)
            await client.add_reaction(msg, no)
            res = await client.wait_for_reaction([supr, give, no], user=user, message=msg)
            await client.delete_message(msg)
            if res.reaction.emoji == supr:
                msg = await client.say("```Indiquez le montant que vous voulez retirer```\n\nSolde actuelle :\n" + str(int(perso[8])) + "<:Rubis_Vert:489369798849855498>")
                msg2 = await client.say("Veuillez indiquer un nombre inférieur à votre solde totale, ou bien écrivez `exit` pour sortir de l'interface")
                while True:
                    res = await client.wait_for_message(author=user, channel=ctx.message.channel)
                    if res.content == "exit" or res.content == "Exit":
                        await client.delete_message(msg)
                        await client.delete_message(msg2)
                        await client.say("Sortie...")
                        break
                    else:
                        try:
                            int(res.content)
                            continue
                        except ValueError:
                            await client.delete_message(res)
                            await client.edit_message(msg2, msg2.content + "\n(Saisie incorrecte, veuillez saisir un nombre)")
                            pass
                    if int(res.content) > int(perso[8]):
                        await client.delete_message(res)
                        await client.edit_message(msg2, msg2.content + "\n(Vous ne possédez pas autant d'argent, veuillez indiquer un nombre plus petit)")
                        pass
                    elif int(res.content) <= 0:
                        await client.delete_message(res)
                        await client.edit_message(msg2, msg2.content + "\n(Vous ne pouvez pas rentrer de nombres négatifs ou nul, veuillez entrer un nombre correct)")
                    else:
                        await client.delete_message(msg)
                        await client.delete_message(msg2)
                        await client.delete_message(res)
                        msg = await client.say("Solde actuelle : " + str(int(perso[8])) + "<:Rubis_Vert:489369798849855498>\nArgent retiré : " + res.content + "<:Rubis_Vert:489369798849855498>\nSolde après argent retiré : " + str(int(perso[8]) - int(res.content)) + "<:Rubis_Vert:489369798849855498>\n\nVoulez-vous vraiment retirer ce montant de votre compte ?")
                        await client.add_reaction(msg, yes)
                        await client.add_reaction(msg, no)
                        res2 = await client.wait_for_reaction([yes, no], user=user, message=msg)
                        if res2.reaction.emoji == yes:
                            await client.delete_message(msg)
                            perso[8] = str(int(perso[8]) - int(res.content))
                            fichier = open("C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + user.id + ".txt", "w")
                            while True:
                                if len(perso) == 0:
                                    break
                                else:
                                    fichier.write(perso[0])
                                    del(perso[0])
                            fichier.close()
                            await client.say(res.content + "<:Rubis_Vert:489369798849855498> on été retiré de votre compte avec succès !")
        elif res.reaction.emoji == equip2:
            msg = await client.say("```Ce menu vous permet de gérer votre équipement, il y a trois emplacements, l'arme, le bouclier, et l'arc. Chaque objet équipé dans ces emplacements modifiera votre attaque et votre défense, et s'usera en fonction des rolls que vous faites.```\n\n:crossed_sword: Voici votre équipement actuel : ")
            msg2 = await client.say(":dagger: : " + perso[33])
            msg3 = await client.say(":shield: : " + perso[34])
            msg4 = await client.say(":bow_and_arrow: : " + perso[35])
            msg5 = await client.say("<:Fleches:502113788347023361> : " + perso[36])
            msg6 = await client.say("Que voules-vous faire ? (:arrow_down: :arrow_up: Pour sélectionner, :inbox_tray: Pour s'équiper, :outbox_tray: Pour se déséquiper, :no_entry_sign: Pour quitter)")
            await client.add_reaction(msg6, down)
            await client.add_reaction(msg6, up)
            await client.add_reaction(msg6, add)
            await client.add_reaction(msg6, supr)
            await client.add_reaction(msg6, no)
            msglist = [msg2, msg3, msg4, msg5]
            msgcontent = [msg2.content, msg3.content, msg4.content, msg5.content]
            await client.edit_message(msg2, ":arrow_forward: " + msg2.content)
            c = 0
            while True:
                res = await client.wait_for_reaction([down, up, add, supr, no], user=user, message=msg6)
                if res.reaction.emoji == down:
                    await client.edit_message(msglist[c], msgcontent[c])
                    c += 1
                    if c > 3:
                        c = 3
                    await client.edit_message(msglist[c], ":arrow_forward: " + msgcontent[c])
                    await client.remove_reaction(msg6, down, user)
                elif res.reaction.emoji == up:
                    await client.edit_message(msglist[c], msgcontent[c])
                    c -= 1
                    if c < 0:
                        c = 0
                    await client.edit_message(msglist[c], ":arrow_forward: " + msgcontent[c])
                    await client.remove_reaction(msg6, up, user)
                elif res.reaction.emoji == add:
                    await client.delete_message(msg)
                    for i in range(len(msglist)):
                        await client.delete_message(msglist[i])
                    await client.delete_message(msg6)
                    vide = 0
                    if msglist[c] == msg2:
                        if len(armes) == 0:
                            await client.say("Votre inventaire d'armes est vide, vous ne pouvez donc rien équiper. Sortie...")
                            vide = 1
                        else:
                            msg = await client.say(":dagger: Votre inventaire d'armes :")
                            msgid = []
                            for j in range(len(armes)):
                                msg2 = await client.say("- " + armes[j])
                                msgid.append(msg2.id)
                            msg3 = await client.say("Choisissez l'arme que vous voulez équiper")
                            armes = objets3
                    elif msglist[c] == msg3:
                        if len(bouc) == 0:
                            await client.say(
                                "Votre inventaire de boucliers est vide, vous ne pouvez donc rien équiper. Sortie...")
                            vide = 1
                        else:
                            msg = await client.say(":shield: Votre inventaire de boucliers :")
                            msgid = []
                            for j in range(len(bouc)):
                                msg2 = await client.say("- " + bouc[j])
                                msgid.append(msg2.id)
                            msg3 = await client.say("Choisissez le bouclier que vous voulez équiper")
                            bouc = objets3
                    elif msglist[c] == msg4:
                        if len(arc) == 0:
                            await client.say(
                                "Votre inventaire d'arcs est vide, vous ne pouvez donc rien équiper. Sortie...")
                            vide = 1
                        else:
                            msg = await client.say(":bow_and_arrow: Votre inventaire d'arcs :")
                            msgid = []
                            for j in range(len(arc)):
                                msg2 = await client.say("- " + arc[j])
                                msgid.append(msg2.id)
                            msg3 = await client.say("Choisissez l'arc que vous voulez équiper")
                            arc = objets3
                    elif msglist[c] == msg5:
                        msg = await client.say("<:Fleches:502113788347023361> Votre inventaire des flèches :")
                        msgid = []
                        msg2 = await client.say("<:Fleches:502113788347023361> : " + fleche[0])
                        msgid.append(msg2.id)
                        msg2 = await client.say(":fire: : " + fleche[1])
                        msgid.append(msg2.id)
                        msg2 = await client.say(":snowflake: : " + fleche[2])
                        msgid.append(msg2.id)
                        msg2 = await client.say(":zap: : " + fleche[3])
                        msgid.append(msg2.id)
                        msg2 = await client.say(":bomb: : " + fleche[4])
                        msgid.append(msg2.id)
                        msg2 = await client.say("<:Fleche_archeonique:502114704769155092> : " + fleche[5])
                        msgid.append(msg2.id)
                        msg3 = await client.say("Choisissez le type de flèche que vous voulez équiper")
                        fleche = objets3
                    await client.add_reaction(msg3, down)
                    await client.add_reaction(msg3, up)
                    await client.add_reaction(msg3, yes)
                    await client.add_reaction(msg3, no)
                    while True:
                        res = await client.wait_for_reaction([down, up, yes, no], user=user, message=msg3)
                        
        elif res.reaction.emoji == no:
            await client.delete_message(msg2)
            while a == 0:
                if len(msgid) == 0:
                    break
                else:
                    msg = await client.get_message(ctx.message.channel, msgid[0])
                    await client.delete_message(msg)
                    del (msgid[0])
            await client.delete_message(msg4)
            await client.say("Sortie de l'inventaire...")
        elif res.reaction.emoji == pack:
            msg = await client.say(
                "Quel inventaire désirez vous regarder ?\n\n:dagger: - Inventaire des armes\n:shield: - Inventaire des boucliers\n:bow_and_arrow: - Inventaire des arcs\n<:Fleches:502113788347023361> - Inventaire des flèches\n:gem: - Inventaire des matériaux\n:old_key: - Inventaire de quête\n:no_entry_sign: - Quitter")
            await client.add_reaction(msg, dagger)
            await client.add_reaction(msg, shield)
            await client.add_reaction(msg, bow)
            await client.add_reaction(msg, arrow)
            await client.add_reaction(msg, mat)
            await client.add_reaction(msg, quest)
            await client.add_reaction(msg, no)
            res = await client.wait_for_reaction([dagger, shield, bow, arrow, mat, quest, no], user=user, message=msg)
            d = 0
            equip = 0
            if res.reaction.emoji == dagger:
                await client.delete_message(msg)
                msg2 = await client.say(":package: Inventaire des armes de " + user.mention + " :")
                inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\armes "
                dura = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités armes "
                equip = 1
            elif res.reaction.emoji == shield:
                await client.delete_message(msg)
                msg2 = await client.say(":package: Inventaire des boucliers de " + user.mention + " :")
                inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\boucliers "
                dura = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités boucliers "
                equip = 2
            elif res.reaction.emoji == bow:
                await client.delete_message(msg)
                msg2 = await client.say(":package: Inventaire des arcs de " + user.mention + " :")
                inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\arcs "
                dura = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\durabilités arcs "
                equip = 3
            elif res.reaction.emoji == arrow:
                await client.delete_message(msg)
                msg2 = await client.say(":package: Inventaire des flèches de " + user.mention + " :")
                inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\flèches "
                dura = 0
            elif res.reaction.emoji == mat:
                await client.delete_message(msg)
                msg2 = await client.say(":package: Inventaire des matériaux de " + user.mention + " :")
                inv = "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\matériaux "
                dura = 0
            elif res.reaction.emoji == quest:
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
                    dura2 = fichier2.readlines()
                    fichier2.close()
                if len(objets) == 0:
                    await client.say("(vide)")
                else:
                    msgid = []
                    for j in range(len(objets)):
                        msg3 = await client.say("- " + objets[j])
                        msgid.append(msg3.id)
                    msg4 = await client.say(
                        "Que voulez-vous faire ? (Sélectionnez les flèches haut et bas pour choisir un objet, puis :outbox_tray: pour le supprimer, :information_source: pour otenir des informations sur cet objet, ou bien :handshake: pour le donner à quelqu'un.)")
                    await client.add_reaction(msg4, down)
                    await client.add_reaction(msg4, up)
                    await client.add_reaction(msg4, supr)
                    await client.add_reaction(msg4, give)
                    if res.reaction.emoji == dagger or res.reaction.emoji == shield or res.reaction.emoji == bow:
                        await client.add_reaction(msg4, equip2)
                    await client.add_reaction(msg4, no)
                    msg5 = await client.get_message(ctx.message.channel, msgid[0])
                    await client.edit_message(msg5, ":arrow_forward: " + msg5.content)
                    a = 0
                    c = 0
                    while a == 0:
                        if res.reaction.emoji == dagger or res.reaction.emoji == shield or res.reaction.emoji == bow:
                            res = await client.wait_for_reaction([down, up, supr, give, equip2, no], user=user, message=msg4)
                        else:
                            res = await client.wait_for_reaction([down, up, supr, give, no], user=user, message=msg4)
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
                            msg = await client.say("Voulez-vous vraiment vous débarasser de cet objet ?")
                            await client.add_reaction(msg, yes)
                            await client.add_reaction(msg, no)
                            res = await client.wait_for_reaction([yes, no], user=user, message=msg)
                            if res.reaction.emoji == yes:
                                del (objets[c])
                                fichier = open(inv + user.id + ".txt", "w")
                                while a == 0:
                                    if len(objets) == 0:
                                        break
                                    else:
                                        fichier.write(objets[0])
                                        del (objets[0])
                                fichier.close()
                                if dura != 0:
                                    del (dura2[c])
                                    fichier = open(dura + user.id + ".txt", "w")
                                    while a == 0:
                                        if len(dura2) == 0:
                                            break
                                        else:
                                            fichier.write(dura2[0])
                                            del (dura2[0])
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
                                            del (perso[0])
                                    fichier.close()
                                await client.delete_message(msg)
                                await client.say("L'objet a été retiré avec succès !")
                            elif res.reaction.emoji == no:
                                await client.say("Annulation et sortie de l'inventaire...")
                            break
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
                                fichier = open(
                                    "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\\player " + str(
                                        int(player[i])) + ".txt", "r")
                                name = fichier.readlines()
                                fichier.close()
                                name2.append(name[0])
                                msg2 = await client.say("- " + name[0])
                                msgid.append(msg2.id)
                            msg3 = await client.say(
                                "Choisissez une personne grâce aux flèches, puis sélectionnez :white_check_mark: pour valider votre choix, ou sinon sélectionnez :no_entry_sign: pour quitter.")
                            await client.add_reaction(msg3, down)
                            await client.add_reaction(msg3, up)
                            await client.add_reaction(msg3, yes)
                            await client.add_reaction(msg3, no)
                            msg4 = await client.get_message(ctx.message.channel, msgid[0])
                            await client.edit_message(msg4, ":arrow_forward: " + msg4.content)
                            e = 0
                            while a == 0:
                                res = await client.wait_for_reaction([down, up, yes, no], user=user, message=msg3)
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
                                        fichier = open(
                                            "C:\\Users\MaxLink\PycharmProjects\papytest\server " + server.id + "\player " + str(
                                                int(player[e])) + ".txt", "r")
                                        fichier2 = open(inv + str(int(player[e])) + ".txt", "r")
                                        perso2 = fichier.readlines()
                                        objets2 = fichier2.readlines()
                                        fichier.close()
                                        fichier2.close()
                                        await client.delete_message(msg)
                                        if (equip == 1 and len(objets2) == int(perso2[29])) or (
                                                equip == 2 and len(objets2) == int(perso2[30])) or (
                                                equip == 3 and len(objets2) == int(perso2[31])):
                                            await client.say(
                                                "L'inventaire de cette personne est plein !\nVous sortez de votre inventaire...")
                                        else:
                                            fichier = open(inv + str(int(player[e])) + ".txt", "a")
                                            fichier.write(objets[c])
                                            fichier.close()
                                            nomobjet = objets[c]
                                            del (objets[c])
                                            fichier = open(inv + user.id + ".txt", "w")
                                            if dura != 0:
                                                fichier2 = open(dura + str(int(player[e])) + ".txt", "a")
                                                fichier2.write(dura2[c])
                                                fichier2.close()
                                                del (dura2[c])
                                                fichier2 = open(dura + user.id + ".txt", "w")
                                            while a == 0:
                                                if len(objets) == 0:
                                                    break
                                                else:
                                                    fichier.write(objets[0])
                                                    del (objets[0])
                                                    if dura != 0:
                                                        fichier2.write(dura2[0])
                                                        del (dura2[0])
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
                                            member = discord.utils.get(ctx.message.server.members, id=str(int(player[e])))
                                            await client.say(
                                                user.mention + " a donné un objet à " + member.mention + " : " + nomobjet)
                                    elif res.reaction.emoji == no:
                                        await client.delete_message(msg)
                                        await client.say("Vous quittez votre inventaire...")
                                    break


client.run(token)
