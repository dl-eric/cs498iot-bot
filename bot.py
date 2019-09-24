from discord.ext.commands import Bot
from discord.utils import get
from discord import ChannelType

# Secrets
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

# Discord Bot
BOT_PREFIX = (".")
client = Bot(command_prefix=BOT_PREFIX)

"""
-------------------------------------------------------------------------------
    Helper methods
-------------------------------------------------------------------------------
"""
def is_enrolled(net_id):
    return True

"""
-------------------------------------------------------------------------------
    Bot commands
-------------------------------------------------------------------------------
"""
@client.command(name='verify',
                description="Check if user is an enrolled student",
                brief="Verify user status",
                pass_context=True)
async def verify(context):
    message = context.message.content
    author = context.message.author

    # See if message is in enrolled students
    if is_enrolled():
        # Assign "Student" tole
        role = get(context.guild.roles, name="Student")
        await author.add_roles(role)

        await author.send("You're verified! Welcome to CS498IoT :)")
    else:
        await author.send("I couldn't verify that NetID. If you're sure that you're enrolled in the class, contact course staff for help.")

    return

@client.event
async def on_message(message):
    # If a user dm's the bot, we want to ignore it.
    if message.channel.type != ChannelType.text:
        return

    await client.process_commands(message)

"""
-------------------------------------------------------------------------------
    Main
-------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    print("Bot Starting...")

    # Run Discord Bot
    client.run(DISCORD_TOKEN)