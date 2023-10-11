import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))
        channels_to_send = ["", ""]  # Add the IDs of the channels you want to send messages to

        while True:
            for channel_id in channels_to_send:
                channel = self.get_channel(int(channel_id))
                if channel:
                    try:
                        random_number = ''.join(random.choice('0123456789') for _ in range(27))
                        
                        await channel.send(random_number)
                        
                    except Exception as e:
                        print(f"An error occurred while sending a message: {e}")
                else:
                    print(f"Channel with ID {channel_id} not found.")
            
            await asyncio.sleep(random.uniform(2, 5))

client = MyClient()
client.run('TOKEN')
#your bot token goes here