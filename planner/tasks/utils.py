from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_test_to_user(user_id):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user_id}",
        {
            "type": "task.notification",
            "data": {"message": "🔔 این یک پیام تستی است"}
        }
    )
