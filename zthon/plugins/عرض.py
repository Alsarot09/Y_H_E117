from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from hunthon import sarub

from ..core.managers import edit_or_reply

plugin_category = "البوت"


@sarub.sar_cmd(
    pattern="عرض$",
    command=("عرض", plugin_category),
    info={
        "header": "Reply to link To get link preview using telegrah.s.",
        "الاستخـدام": "{tr}عرض",
    },
)
async def _(event):
    "To get link preview"
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**- بالـرد ع رابــط ...**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**- بالـرد ع رابــط ...**")
        return
    chat = "@chotamreaderbot"
    sar = await edit_or_reply(event, "**- جــارِ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6275274612)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await sarub(unblock("chotamreaderbot"))
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=6275274612)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith(""):
            await sar.edit("Am I Dumb Or Am I Dumb?")
        else:
            await sar.delete()
            await event.client.send_message(event.chat_id, response.message)
