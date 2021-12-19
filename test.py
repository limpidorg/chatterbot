import asyncio
import threading

from run import bot, t_run

loop = asyncio.new_event_loop()
t = threading.Event()


def hasJoinedDiscord(username):
    loop.call_soon_threadsafe(asyncio.ensure_future, bot.has_joined_discord(username, t))
    t.wait(5)
    res = t.has_joined_discord
    print(res)
    return res


def sendMessage(id, message):
    asyncio.ensure_future(bot.send_message(id, message))


id = hasJoinedDiscord("Bonsaï#8521")
sendMessage(id, "hi there im so brilliant")

loop.call_soon_threadsafe(loop.stop)
