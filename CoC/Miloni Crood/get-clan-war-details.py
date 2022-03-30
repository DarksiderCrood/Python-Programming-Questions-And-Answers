# Install: py -3 -m pip install -U coc.py
import coc

client = coc.login('email', 'password')

async def main():
    player = await client.get_player("tag")
    print("{0.name} has {0.trophies} trophies!".format(player))

    clans = await client.search_clans(name="Best Clan Ever", limit=5)
    for clan in clans:
        print("{0.name} ({0.tag}) has {0.member_count} members".format(clan))

    try:
        war = await client.get_current_war("#clantag")
        print("{0.clan_tag} is currently in {0.state} state.".format(war))
    except coc.PrivateWarLog:
        print("Uh oh, they have a private war log!")

client.loop.run_until_complete(main())
client.close()