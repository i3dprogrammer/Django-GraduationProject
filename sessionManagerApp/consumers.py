import json
from .models import Session, ChatFullName
from studentsApp.models import StudentInfo
from professorsApp.models import Professor
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import AsyncToSync
from channels.layers import get_channel_layer

class MyConsumer(WebsocketConsumer):
    def connect(self):
        session_id = self.scope['url_route']['kwargs']['session_id']
        user = self.scope['user']
        # Check if the user is authenticated and the session exists.
        if user.is_authenticated and Session.objects.filter(id=session_id).exists():
            session = Session.objects.get(id=session_id)
            # Check if the session chat is active and the student has the current session in his sessions list.
            if (session.chatActive and StudentInfo.objects.filter(user=user, sessions=session)) or (Professor.objects.filter(user=user).exists() and session.professor == Professor.objects.get(user=user)):
                self.accept()

        if Professor.objects.filter(user=user).exists():
            ChatFullName.objects.all().delete()
            session.chatActive = True
            session.save()

        ChatFullName.objects.create(user=user, name=self.get_user_fullname(), session=session)
        AsyncToSync(self.channel_layer.group_add)('chat-{0}'.format(session_id), self.channel_name)
        self.send_message('[System] {0} Connected.'.format(self.get_user_fullname()), add_users=list(ChatFullName.objects.values('name')))
    
    def receive(self, text_data):
        self.send_message('[{0}] {1}'.format(self.get_user_fullname(), text_data))

    def send_message(self, text_data, add_users = [], remove_users = []):
        session_id = self.scope['url_route']['kwargs']['session_id']
        AsyncToSync(self.channel_layer.group_send)(
            'chat-{0}'.format(session_id),
            {
                "type": "chat.message",
                "text": json.dumps(
                    {
                        'text': text_data,
                        'add_users': add_users,
                        'remove_users': remove_users,
                    }),
            },
        )

    def chat_message(self, event):
        self.send(text_data=event["text"])

    def get_user_fullname(self):
        user = self.scope['user']
        fullname = ''
        if StudentInfo.objects.filter(user=user).exists():
            fullname = StudentInfo.objects.get(user=user).full_name
        elif Professor.objects.filter(user=user).exists():
            fullname = Professor.objects.get(user=user).name

        return fullname

    def disconnect(self):
        print('test')
        try:
            session_id = self.scope['url_route']['kwargs']['session_id']
            user = self.scope['user']

            # Send broadcast message to all users indicating that you disconnected.
            self.send_message('[System] {0} Disconnected.'.format(self.get_user_fullname()), remove_users = list(ChatFullName.objects.get(user=user).name))

            # Remove the channel name from the group on disconnecting.
            AsyncToSync(self.channel_layer.group_discard)('chat-{0}'.format(session_id), self.channel_name)

            # On disconnect remove the user from chat users model.
            ChatFullName.objects.filter(user=user).delete()

            # session = Session.objects.get(id=session_id)
            # if Professor.objects.filter(user=user).exists():
            #     ChatFullName.objects.all().delete()
            #     session.chatActive = False
            #     session.save()
        except:
            print('Error disconnecting the sockets!')