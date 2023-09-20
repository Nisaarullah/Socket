import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Vote  # Import the Vote model from your app's models

# Create a global vote counter variable
vote_counter = 0

class VoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        global vote_counter  # Access the global vote counter variable
        text_data_json = json.loads(text_data)
        vote_value = text_data_json.get('vote')

        if vote_value:
            # Increment the vote counter
            vote_counter += 1

            # Save the vote value in the database
            await self.save_vote(vote_value)

            # Send the updated vote count back to the client
            await self.send(text_data=json.dumps({
                'vote': vote_value,
                'total_votes': vote_counter,
            }))

    @sync_to_async
    def save_vote(self, vote_value):
        # Create and save a new Vote object with the vote_value
        vote = Vote.objects.create(value=vote_value)
        vote.save()
