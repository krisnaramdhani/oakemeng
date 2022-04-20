import errno#
import os#
import sys#
import tempfile#

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('75dDow8XTK5yHrZMNwMBVKQBg5aRQW0Hfi9WYPEakL44pwiv3pOmAh9olFJFCF6vGDpvzLeYeDFM579HotIkQ2hN65ywypw0dFMZPZAmkY2083EoBICSYPpOnsrr+f0Y5eDzHnu0+Z/RX13R34wB7AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ebe5de089b73e44b2635a45b8db907ff')


#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(JoinEvent)#
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Ktik [Kemeng help] utk command :D\nKtik [Kemeng bye] utk Pergi :D\n\nCreator by Kris => \n{https://line.me/ti/p/~krissthea} \nor => \n{https://line.me/ti/p/~kriskemeng2}')) 


@handler.add(MessageEvent, message=TextMessage)#
def handle_text_message(event):
    text = event.message.text

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
#=====[ LEAVE GROUP OR ROOM ]==========
            
    if text == 'aku' or text == 'Aku' or text == 'Me' or text == 'me':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile in group chat"))

    if text == 'Kemeng bye' or text == 'kemeng bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Bye..(-_-), Aim Pamit, Jangan Lupa Bahagia Ya..(-_-)...!!!'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Bye..(-_-), Aim Pamit, Jangan Lupa Bahagia Ya..(-_-)...!!!'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

    if text == 'OrderPromo':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ʳᵉᵃᵈʸ ᵒʳᵈᵉʳ:
║☛ˢᵇ ᵗᵉᵐᵖˡ+ʲˢ
║☛ˢᵇ ᵗᵉᵐᵖˡ+ᵃˢⁱˢᵗ+ᵃⁿᵗⁱʲˢ
║☛ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ
║☛ᵇᵒᵗ ʷᵃʳ
║☛ᵇᵒᵗ ᶜˡ
║☛ᵇᵒᵗ ᶜʰᵃᵗ
║☛ᵇᵒᵗ ᵖᵘʳᵍᵉ
║☛ᵇᵒᵗ ᵍᵒˡᵃⁿᵍ
╠═════════════
║☛ᵗᵒᵏᵉⁿ ᵖʳⁱᵐᵃʳⁱ
║ ✔️1 ᵗᵒᵏᵉⁿ = 10ᵏ
╠═════════════
║☛ᵛᵖˢ
║ ✔️ᵃˡˡ ᵗʸᵖᵉ ᵛᵖˢ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════

'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ʳᵉᵃᵈʸ ᵒʳᵈᵉʳ:
║☛ˢᵇ ᵗᵉᵐᵖˡ+ʲˢ
║☛ˢᵇ ᵗᵉᵐᵖˡ+ᵃˢⁱˢᵗ+ᵃⁿᵗⁱʲˢ
║☛ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ
║☛ᵇᵒᵗ ʷᵃʳ
║☛ᵇᵒᵗ ᶜˡ
║☛ᵇᵒᵗ ᶜʰᵃᵗ
║☛ᵇᵒᵗ ᵖᵘʳᵍᵉ
║☛ᵇᵒᵗ ᵍᵒˡᵃⁿᵍ
╠═════════════
║☛ᵗᵒᵏᵉⁿ ᵖʳⁱᵐᵃʳⁱ
║ ✔️1 ᵗᵒᵏᵉⁿ = 10ᵏ
╠═════════════
║☛ᵛᵖˢ
║ ✔️ᵃˡˡ ᵗʸᵖᵉ ᵛᵖˢ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════

'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

    if text == 'HargaSBTemplate':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ˢᵉʷᵃ ˢᵉˡᶠᵇᵒᵗ [ˢᵇ]
╠═════════════
║☛ˢᵇ ᵗᵉᵐᵖˡ + ʲˢ
║ ✔️50ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 1 ᵃⁿᵗⁱʲˢ
║ ✔️75ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 1ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️100ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 2ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️125ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 3ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️150ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 4ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️175ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 5ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️200ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 10ᵃˢⁱˢᵗ + 2ᵃⁿᵗⁱʲˢ
║ ✔️350ʳᵇ/ᵇˡⁿ
╠═════════════
║ˢᵉʷᵃ ʰᵉˡᵖᵉʳ ˢᵉˡᶠᵇᵒᵗ[ˢᵇ]
╠═════════════
║ ✔️1 ʰᵉˡᵖᵉʳ ˢᵇ
║ ✔️10 ˢˡᵒᵗ
║ ✔️350ʳᵇ/ᵇˡⁿ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ˢᵉʷᵃ ˢᵉˡᶠᵇᵒᵗ [ˢᵇ]
╠═════════════
║☛ˢᵇ ᵗᵉᵐᵖˡ + ʲˢ
║ ✔️50ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 1 ᵃⁿᵗⁱʲˢ
║ ✔️75ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 1ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️100ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 2ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️125ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 3ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️150ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 4ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️175ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 5ᵃˢⁱˢᵗ + 1ᵃⁿᵗⁱʲˢ
║ ✔️200ʳᵇ/ᵇˡⁿ
║
║☛ˢᵇ ᵗᵉᵐᵖˡ ʲˢ + 10ᵃˢⁱˢᵗ + 2ᵃⁿᵗⁱʲˢ
║ ✔️350ʳᵇ/ᵇˡⁿ
╠═════════════
║ˢᵉʷᵃ ʰᵉˡᵖᵉʳ ˢᵉˡᶠᵇᵒᵗ[ˢᵇ]
╠═════════════
║ ✔️1 ʰᵉˡᵖᵉʳ ˢᵇ
║ ✔️10 ˢˡᵒᵗ
║ ✔️350ʳᵇ/ᵇˡⁿ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

    if text == 'HargaBotProtek':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ˢᵉʷᵃ ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ
╠═════════════
║🛡ᵃᵈᵐⁱⁿ ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ ʳᵒᵒᵐ
║
║ ✔️5 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 100ʳᵇ/ᵇˡⁿ
║   🔘 + 1ᵃⁿᵗⁱʲˢ
║
║ ✔️8 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 150ʳᵇ/ᵇˡⁿ
║   🔘 + 2ᵃⁿᵗⁱʲˢ
║
║ ✔️10 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 200ʳᵇ/ᵇˡⁿ
║    + 2ᵃⁿᵗⁱʲˢ
║
║ ✔️15 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 300ʳᵇ/ᵇˡⁿ
║   🔘 + 3ᵃⁿᵗⁱʲˢ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║ˢᵉʷᵃ ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ
╠═════════════
║🛡ᵃᵈᵐⁱⁿ ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ ʳᵒᵒᵐ
║
║ ✔️5 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 100ʳᵇ/ᵇˡⁿ
║   🔘 + 1ᵃⁿᵗⁱʲˢ
║
║ ✔️8 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 150ʳᵇ/ᵇˡⁿ
║   🔘 + 2ᵃⁿᵗⁱʲˢ
║
║ ✔️10 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 200ʳᵇ/ᵇˡⁿ
║    + 2ᵃⁿᵗⁱʲˢ
║
║ ✔️15 ᵇᵒᵗ ᵖʳᵒᵗᵉᶜᵗ 300ʳᵇ/ᵇˡⁿ
║   🔘 + 3ᵃⁿᵗⁱʲˢ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

    if text == 'HargaEditing':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║☛ᵉᵈⁱᵗ ᶜᵒᵛᵉʳ & ˡᵒᵍᵒ 
║ ✔️10ʳᵇ/ᶜᵒᵛᵉʳ
║ ✔️10ʳᵇ/ˡᵒᵍᵒ
║☛ᵉᵈⁱᵗ ˡᵒᵍᵒ ᵛⁱᵈᵉᵒ
║ ✔️20ʳᵇ/ˡᵒᵍᵒ
╠═════════════
║☛ˢᵒⁿᵍᵇᵒᵒᵏ ˢᵐᵘˡᵉ 
║ ✔️20ʳᵇ/ˡᵃᵍᵘ
║ ✔️100ʳᵇ/6ˡᵃᵍᵘ
║☛ᵛⁱᵖ ˢᵐᵘˡᵉ
║ ✔️20ʳᵇ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡
╠═════════════
║☛ᵉᵈⁱᵗ ᶜᵒᵛᵉʳ & ˡᵒᵍᵒ 
║ ✔️10ʳᵇ/ᶜᵒᵛᵉʳ
║ ✔️10ʳᵇ/ˡᵒᵍᵒ
║☛ᵉᵈⁱᵗ ˡᵒᵍᵒ ᵛⁱᵈᵉᵒ
║ ✔️20ʳᵇ/ˡᵒᵍᵒ
╠═════════════
║☛ˢᵒⁿᵍᵇᵒᵒᵏ ˢᵐᵘˡᵉ 
║ ✔️20ʳᵇ/ˡᵃᵍᵘ
║ ✔️100ʳᵇ/6ˡᵃᵍᵘ
║☛ᵛⁱᵖ ˢᵐᵘˡᵉ
║ ✔️20ʳᵇ
╠═════════════
║☛http://line.me/ti/p/~kriskemeng2
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))

    if text == 'Bigsticker123fjs':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛Big Sticker☚'
╠═════════════
║makasih
║helo/halo
║hai
║sabar
║wkwk
║hihi
║siap
║ok/oke
║gak
║malam/mlm
║knp/kenapa
║tikung
║waw/wow
║hhh
║sun/sun dong
║kiss
║haha
║marah/ngambek
║sst/diam
║sepi
║gendeng/koplak woy
║kabur
║otw/pergi
║bye
║joget/joged
║goyang/goyang bro
║wasyik/goyang bool
║cipok
║kojom.mojok
║tipok
║pentung
║tabok
║galau
║goyang brow
║asem
║rasakno/puas
║udud brow
║terlena/terpana
║mimi uu
║sambil ngopi brow
║oh/ooh
║kemeng
║beb/syg
║maaf/sory
║njir
║pisang
║pisang2
║pisang3
║sosis
║laksanakan
║bomat
║mksh/thank
║anjay/njay
╠═════════════
║Rokok/Udud
║Cantiknya/Ayune
║Cukup dua saja/Cukup 2 saja/Cukup 2/2 aja
║Hajar brow/Hajar bro
║Nah loh/nah loh
║Nah kan/nah kan
║Sedot brow/Hisap brow
║Lihat saja/Liat aja
║Nah itu/nah itu
║Lemper/Baper
║Mantap brow/'Mantap bro
║Wasyik/wasyik
║Siap 86/86 brow
║Apa lu/Kapok
║Kopi uu
║Gendeng woy
║Tikung aku donk/Tikung donk
║Upst/Keceplosan
║Buat kamu/Buat km
║Di atas apa/Ngapain di atas
║Pada kmn neh/Pada kmn
║Gak mau/Moh
║Pasti pd mojok/Pada mojok/Pasti mojok
║Gara2 kamu/Gara2 km/Kamu seh
║goyang donk
║apa seh/kepo
║pada ngapain/ngapain
║ass
║wslm
║met pagi
║udah ngopi blm/ngopi
║udah mkn blm/mkn/makan
╠═════════════
║sodok woy
║kenyot woy
║kemeng woy
║kungging woy
║bool woy
║naikin woy/ebol woy
║tunggingin
║lari
║jilat woy
║bomat woy
║mbut woy/jembut woy
║yoi/jiah
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛Big Sticker☚'
╠═════════════
║makasih
║helo/halo
║hai
║sabar
║wkwk
║hihi
║siap
║ok/oke
║gak
║malam/mlm
║knp/kenapa
║tikung
║waw/wow
║hhh
║sun/sun dong
║kiss
║haha
║marah/ngambek
║sst/diam
║sepi
║gendeng/koplak woy
║kabur
║otw/pergi
║bye
║joget/joged
║goyang/goyang bro
║wasyik/goyang bool
║cipok
║kojom/mojok
║lelah/cape deh
║tipok
║pentung
║tabok
║galau
║goyang brow
║asem
║rasakno/puas
║udud brow
║terlena/terpana
║mimi uu
║sambil ngopi brow
║oh/ooh
║kemeng
║beb/syg
║maaf/sory
║njir
║pisang
║pisang2
║pisang3
║sosis
║laksanakan
║bomat
║mksh/thank
║anjay/njay
╠═════════════
║Rokok/Udud
║Cantiknya/Ayune
║Cukup dua saja/Cukup 2 saja/Cukup 2/2 aja
║Hajar brow/Hajar bro
║Nah loh/nah loh
║Nah kan/nah kan
║Sedot brow/Hisap brow
║Lihat saja/Liat aja
║Nah itu/nah itu
║Lemper/Baper
║Mantap brow/'Mantap bro
║Wasyik/wasyik
║Siap 86/86 brow
║Apa lu/Kapok
║Kopi uu
║Gendeng woy
║Tikung aku donk/Tikung donk
║Upst/Keceplosan
║Buat kamu/Buat km
║Di atas apa/Ngapain di atas
║Pada kmn neh/Pada kmn
║Gak mau/Moh
║Pasti pd mojok/Pada mojok/Pasti mojok
║Gara2 kamu/Gara2 km/Kamu seh
║goyang donk
║apa seh/kepo
║pada ngapain/ngapain
║ass
║wslm
║met pagi
║udah ngopi blm/ngopi
║udah mkn blm/mkn/makan
╠═════════════
║sodok woy
║kenyot woy
║kemeng woy
║kungging woy
║bool woy
║naikin woy/ebol woy
║tunggingin
║lari
║jilat woy
║bomat woy
║mbut woy/jembut woy
║yoi/jiah
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'Assa' or text == 'Assalamu' or text == "assa":
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
Wa'alaikumsallam.Wr,Wb
وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
Wa'alaikumsallam.Wr,Wb
وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TEMPLATE MESSAGE ]=============
    elif "Pagi" in event.message.text:
        quo = ('Pagi juga Kak, Met sarapan dan selamat beraktivitas ya..(-_-)...!!!','Pagi kak, tumben udah bangun neh, Mandi dulu gih kak...!!!')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
               
    elif "Siang" in event.message.text:
        quo = ('Siang juga Kak, Met makan siang dan selamat Istirahat ya..(-_-)...!!!','Selamat siang kak, kopi break dulu kak biar fresh...!!!')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0 
                
    elif "Sore" in event.message.text:
        quo = ('Sore juga Kak, Moga lelahmu menjadi masa depanmu yang cerah ya..(-_-)...!!!','Selamat sore kak, mandi dulu kak, terus jalan2 sore kak...!!!')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0 
                
    elif "Malam" in event.message.text:
        quo = ('Malam juga Kak, Selamat Tidur kak, moga mimpi indah..(-_-)...!!!','Selamat malam kak, selamat beristirahat...!!!')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0 
        
    elif "Mlm" in event.message.text:
        quo = ('Malam juga Kak, Selamat Tidur kak, moga mimpi indah..(-_-)...!!!','Selamat malam kak, selamat beristirahat...!!!')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0 
        
    elif "Idline: " in event.message.text:
        skss = event.message.text.replace('Idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Dasar kebotan Lho..!!!')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tes') or (text == 'tes') or (text == 'Test') or (text == 'test'):
        message = TextSendMessage(text='Testing Satu Tetes Bunting..Lol..(-_-)')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bah') or (text == 'bah'):
        message = TextSendMessage(text='Lul')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Nah') or (text == 'nah'):
        message = TextSendMessage(text='Kan')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Naik') or (text == 'Naik woy') or (text == "Naik yux"):
        message = TextSendMessage(text='Jangan mau naik kak, paling di atas di gombalin, ujung2nya modus..:3)')
        line_bot_api.reply_message(event.reply_token, message)
#===========================================================
    elif text == 'Kemeng help':#template
        buttons_template = TemplateSendMessage(
            alt_text='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
            template=ButtonsTemplate(
                title='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
                text= 'ᶜʸᵇΣʳ Δʳᵐʸ βΩᵗ => Kris',
                actions=[
                    MessageTemplateAction(
                        label='Menu',
                        text='Menubot'
                    ),
                    MessageTemplateAction(
                        label='Big Sticker',
                        text='Bigsticker123fjs'
                    ),
                    MessageTemplateAction(
                        label='Team Pasukan Kemeng',
                        text='TeamPasukanKemeng'
                    ),
                    MessageTemplateAction(
                        label='Creator',
                        text='OwnerCyberArmyBot'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
        
    elif text == 'Menubot':#template
        buttons_template = TemplateSendMessage(
            alt_text='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
            template=ButtonsTemplate(
                title='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='Promo',
                        text='OrderPromo'
                    ),
                    MessageTemplateAction(
                        label='List Harga',
                        text='ListHarga'
                    ),
                    MessageTemplateAction(
                        label='Cover PK',
                        text='CoverPK'
                    ),
                    MessageTemplateAction(
                        label='Logo PK',
                        text='LogoPK'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == 'ListHarga':#template
        buttons_template = TemplateSendMessage(
            alt_text='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
            template=ButtonsTemplate(
                title='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='Harga SB Template',
                        text='HargaSBTemplate'
                    ),
                    MessageTemplateAction(
                        label='Harga Bot Protek',
                        text='HargaBotProtek'
                    ),
                    MessageTemplateAction(
                        label='Harga Editing',
                        text='HargaEditing'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========
    elif text == 'TeamPasukanKemeng':#carousel
        message = TemplateSendMessage(
            alt_text='🛡ᵖΔˢᵘᵏΔⁿ ᵏΣᵐΣⁿᵍ🛡',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Team PK',
                        text='Kris',
                        actions=[
                            URITemplateAction(
                                label='>Kris<',
                                uri='https://line.me/ti/p/~kriskemeng2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Litam',
                        actions=[
                            URITemplateAction(
                                label='>Litam<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Anak Soleh',
                        actions=[
                            URITemplateAction(
                                label='>Sengkuni<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Inneu',
                        actions=[
                            URITemplateAction(
                                label='>Inneu<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Fadli',
                        actions=[
                            URITemplateAction(
                                label='>Fadli<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Indra',
                        actions=[
                            URITemplateAction(
                                label='>Indra<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Lingling',
                        actions=[
                            URITemplateAction(
                                label='>Lingling<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Devil',
                        actions=[
                            URITemplateAction(
                                label='>Devil<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Team PK',
                        text='Ayhu',
                        actions=[
                            URITemplateAction(
                                label='>Ayhu<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====================================================================================================================
    elif text == 'Apakah':
        #rep = text.replace("Apakah ","")
        txt = ["Ya","Tidak","Bisa Jadi","Mungkin","Hoax"]
        line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(text=random.choice(txt))
            ]
        )
            
    elif text == 'Carivideo':
        separate = text.split(" ")
        search = text.replace(separate[0] + " ","")
        params = {"search_query": search}
        source = requests.get("https://www.youtube.com/results", params = params)
        bsoup = BeautifulSoup(source.content, "html5lib")
        ret_ = "[ RESULT ]"
        datas = []
        num = 0
        for data in soup.select(".yt-lockup-title > a[title]"):
            if "&lists" not in data["href"]:
                datas.append(data)
        num += 1
        for data in datas:
            ret_ += "\n\n{}. Judul: {}".format(num, data["title"])
            ret_ += "\n    Link: https://www.youtube.com{}".format(data["href"])
        ret_ += "\n\n[ TOTAL: {} VIDEO ]".format(len(datas))
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=ret_))
                
    elif text == 'Carigambar':
        separate = text.split(" ")
        search = text.replace(separate[0] + " ","")
        r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
        data = r.text
        data = json.loads(data)

        if data["result"] != []:
            items = data["result"]
            path = random.choice(items)
            a = items.index(path)
            b = len(items)

        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path
        )

        line_bot_api.reply_message(
            event.reply_token,
            image_message
        )
#======================================================================================================================
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Do it?', actions=[
            MessageAction(label='Yes', text='Yes!'),
            MessageAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping'),
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#================================================================================= 
    elif text == 'OwnerCyberArmyBot':
        confirm_template = ConfirmTemplate(text='Owner Cyber Army Bot', actions=[
            MessageAction(label='Kris1', text='Kris!1!'),
            MessageAction(label='Kris2', text='Kris!2!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Creator', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#=======================================================================================================================
    elif text == 'Kris!1!':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.pinimg.com/564x/e1/9f/b0/e19fb0f83cbe4b669551dd74ac18fccc.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~krissthea', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='Owner: Kris', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Order',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Self Bot, Bot Protect, Anti JS',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Edit',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Cover, Logo, Logo Video",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Kris', uri="https://line.me/ti/p/~krissthea")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak1 kris", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#======================================================= 
    elif text == 'Kris!2!':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://i.pinimg.com/564x/5a/c9/93/5ac99335f394b56f53f0faf8c6f6467d.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~kriskemeng2', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='Owner: Kris', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Order',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Self Bot, Bot Protect, Anti JS',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Edit',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Cover, Logo, Logo Video",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Kris', uri="https://line.me/ti/p/~kriskemeng2")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak2 kris", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#===============================================================================================
#=====[ FLEX MESSAGE ]==========
        
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/--gxZM-3_8xk/WFasL3Y55gI/AAAAAAAFd14/tu2DK-ITFfcOjZHAnq3ynEyQR7TEAStRQCLcB/s1600/AW352983_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'helo') or (text == 'Helo') or (text == 'halo') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://thumbs.gfycat.com/AdeptIdioticIchidna-max-1mb.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hai') or (text == 'Hai'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-TS3IrlyRK18/WE_QlVbh1KI/AAAAAAAFMuM/mcEPg4f4MV4KJgfNWc-IMb8MmU4IpRk6ACLcB/s1600/AW293929_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-d2s2TZWQL3M/WRxIlxH2wmI/AAAAAAAHlYE/vmDRTrJR3C461hEsMFZL28qRCglREM7bQCLcB/s1600/AW429484_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'wkwk') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-OVigsYHr2n0/WymMu2gJipI/AAAAAAAgaIo/rW6lhc_8y1k7La3QYpq67YOORu64jyuxgCLcBGAs/s1600/AW1238316_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hihi') or (text == 'Hihi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-wk4iPzjOYoQ/WFvyR-NDP0I/AAAAAAAFLwo/Yuh40_TQLP0cDCHwtqeN5VmNfGN0LnxQgCLcB/s1600/AW355622_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'siap') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-ipl1HRIeSOM/WRMvRhMGU1I/AAAAAAAPEH0/ea9RXLFj1sQWKL-Zs0YgthUqJGGQo3QwgCLcB/s1600/AW424038_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ok') or (text == 'oke') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/0e/91/e3/0e91e3422c0c765ce74601ccecace5cf.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bott',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Malam') or (text == 'Met mlm') or (text == 'Met malam') or (text == 'Selamat malam') or (text == 'Mlm'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bott',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/cd/13/79/cd1379986667309c892717c2c0017b90.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Knp') or (text == 'knp') or (text == 'Kenapa') or (text == 'Apa') or (text == '?'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-qRlbAaTzSsI/WE_QldvuKPI/AAAAAAAFMuI/0tGUHoqtvgYOH97ftYe4WlKDtLuaK7V_ACLcB/s1600/AW293929_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Krisna') or (text == 'Tikung') or (text == 'Manis'):
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA4k/mb76_dr8Veo9ryWnBS70dF5TT5Fg7C3HQCJoC/w795-h801-n-rw/807838.jpg',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#    elif (text == 'Krisna') or (text == 'Tikung') or (text == 'Manis'):
#        message = ImagemapSendMessage(
#            base_url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA4k/mb76_dr8Veo9ryWnBS70dF5TT5Fg7C3HQCJoC/w795-h801-n-rw/807838.jpg',
#            alt_text='Kris',
#            base_size=BaseSize(height=1040, width=1040),
#            actions=[
#                URIImagemapAction(
#                    link_uri='https://line.me/ti/p/~kriskemeng2',
#                    area=ImagemapArea(
#                        x=0, y=0, width=1040, height=1040
#                    )
#                ),
#                MessageImagemapAction(
#                    text='Kris Manis',
#                    area=ImagemapArea(
#                        x=520, y=0, width=520, height=1040
#                    )
#                )
#            ]
#        )
#        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'waw') or (text == 'Waw') or (text == 'wow') or (text == 'Wow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/--PyKKdhyjbo/WMlfB-9gfUI/AAAAAAAOBaM/1XAFQtTAxyoQTxFGjm4UOCzVckJq3GiTgCLcB/s1600/AW392366_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'hhh') or (text == 'Hhh'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-OcsIXDFKcnA/WRxI6NIil1I/AAAAAAAHldE/BHP9ijh88eYZROMWHdPcHH3-kPWXiCd4QCLcB/s1600/AW429514_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sun') or (text == 'Sun dong'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-GpEExd0b9-A/WyheSQrPFPI/AAAAAAANJXM/M5YBhnT_vcofTJZ9Xw2fX2lQrRbFmKV7wCLcBGAs/s1600/AW1238614_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kiss') or (text == 'kiss'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-J9W5u3_TxbQ/WmS8qVYvGCI/AAAAAAAA1iE/LgxLU0g3WZUalKIdjNS-L3DNbocSiZDXwCJoC/w800-h800/0DjyylSLOtvLxegotklwyVCg02N.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Haha') or (text == 'haha'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://s.kaskus.id/images/2018/07/04/2216544_20180704015520.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Marah') or (text == 'Ngambek'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-W5WaLvaUoyU/WMQX7uAyHpI/AAAAAAAN_M0/xHgXrqlJwmczxIbB3R73_13vXpgnDAPkACLcB/s1600/AW391031_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sst') or (text == 'Diam'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-zMbjVh62jpk/WS2EH_K-j2I/AAAAAAAH0ks/7M3o_hMbfk8TDAiR9stehYVH6DjTOBr4QCLcB/s1600/AW438063_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sepi') or (text == 'sepi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-JwgXAXNVG2w/WykhtxpIJqI/AAAAAAAgYNY/W_uh6gn5uoYrx0aA6Q0GvQbPsfzLMTtYgCLcBGAs/s1600/AW1237931_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Koplak woy') or (text == 'Somplak woy'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-USupKtE-__s/WM1eaBaDuII/AAAAAAAOIV8/voYdrf_YWUEqj2boITcjGY5dwgrB8283ACLcB/s1600/AW395051_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kabur') or (text == 'kabur'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-qqBCTr7ZpI4/WM1eau1_q1I/AAAAAAAOIWE/Fa5C3zL28esKZmN6vsRPcBHFmVgRs3FIgCLcB/s1600/AW395051_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Otw') or (text == 'Pergi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-MbJFVYtQ4n0/WM1eaywyfjI/AAAAAAAOIWI/y0DTio3zSAoaXbt9QsgH4L_G7XxaA0jYQCLcB/s1600/AW395051_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bye') or (text == 'bye'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/74/f7/31/74f73145230b0a5e54a8e579d27ca1a7.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Joged') or (text == 'Joget') or (text == 'Joged bro'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-Cgdf-zL8OF4/WymMaaO2QBI/AAAAAAAgaGo/hIVovpbQTvA8xFsm9kA17Js6A5_1bIGLQCLcBGAs/s1600/AW1238310_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Goyang') or (text == 'Goyang bro'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-buFHNCEXtdI/WetfJvdCCWI/AAAAAAALsJE/p2xMIVFuu6cJRmFkf9ZomligmbClPXLtwCLcBGAs/s1600/AW586900_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Goyang bool'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-YkMj7-lrhkY/WetfJHV4nLI/AAAAAAALsJA/_5x8w9hw9kQrSsUS_oz8VigjZmTawSlAACLcBGAs/s1600/AW586900_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kojom') or (text == 'Mojok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-RCN2F5_sW8s/WETV3aiPh8I/AAAAAAALxnM/UnmNbtuVCkEZ_bbqlq2t5mHf49EmgvndwCLcB/s1600/AW324437_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Lelah') or (text == 'Cape deh'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/-fXRrFVN_0is/WE0P-W45r_I/AAAAAAAMLfc/UqBiPW9xU0k0WREB5NyzNXZ9FuBPyP-sQCLcB/s1600/AW295200_20.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'cipok') or (text == 'Cipok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-yoMHiOR17Bg/WETVuzbvyBI/AAAAAAALxm4/od4pFuukfH40cuMn2c08wqtkGOX3HuNSACLcB/s1600/AW324437_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tipok') or (text == 'tipok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-e3cFsWiKLdA/WTAH1EByiRI/AAAAAAAIMvM/dUvAXujr4cIwsjn5DPEvRfCYZVp3DWvSQCLcB/s1600/AW439317_13.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pentung') or (text == 'pentung'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/-uqvJKBeQORI/WD6hrAEpeOI/AAAAAAALo9g/6QmAHA53bI039Gv1Brt5RA-E0av-tueJACLcB/s1600/AS002044_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tabok') or (text == 'tabok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-CXej0VEJkps/WDv1XSwipPI/AAAAAAALlNU/UjrTOos8KF86vkw05SE25bUkAQc86b2pwCLcB/s1600/AS001630_08.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Galau') or (text == 'galau'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-oB7VOXVL0FI/WUMi8gN7FdI/AAAAAAAPwaM/GO0TjY65hvEP5GsBPELtoTJJ3WFm6vGDgCLcBGAs/s1600/AW448914_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Goyang brow') or (text == 'goyang brow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-3i31UNhuF-Q/Wkhcq7CdO1I/AAAAAAAQgw4/RHaLNrmlw1MhNRD9lmf1sJIS66eLa53wgCLcBGAs/s1600/AW709937_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Asem') or (text == 'Aseem'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-Yc0J49r3g0Q/WEjmHvYf8vI/AAAAAAAL54w/XKP9sFitJGshWkEpS8kWQ0Bxay0vT3qUgCLcB/s1600/AW337107_08.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Rasakno') or (text == 'Puas'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-VE3Pt6nU6qs/WymMsufN77I/AAAAAAAgaIY/49zgf3ECVGY0cX048uaI6OhrZaXRZi-owCLcBGAs/s1600/AW1238316_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Beb') or (text == 'Bebz') or (text == 'Syg'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-WYlD4B78Ujw/WRxHdQFBZMI/AAAAAAAHlIc/aOT51KgCN4s_-LpUzULNFPyeguR7iRNHACLcB/s1600/AW429388_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Maaf') or (text == 'maaf') or (text == 'Sory'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/-qACbXtfK1hk/WOz1iQOnMjI/AAAAAAAG2-A/Taf1opmO9zEgH9iINyv7m0RYzFegbJQfQCLcB/s1600/AW405967_02.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Njir') or (text == 'Njiir') or (text == 'Njirr'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-5wFNSCJlYWI/WRxHdiXJl0I/AAAAAAAHlIg/k9KvZJCkpfIslWlgqyxtjR5jzBEvEgA6QCLcB/s1600/AW429388_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pisang') or (text == 'pisang'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-7wUpNkpU9XU/Wke_zvXj2GI/AAAAAAAKnmo/9D3dj4ZafxAYgm09Jn0gUQ-ixOoxvDyggCLcBGAs/s1600/AW708510_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sosis') or (text == 'sosis'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-uV86hoCScvs/Wke_3IxTVWI/AAAAAAAKnnQ/VRKwswJBldgVaE78KijyXaR5QMoOvdMIQCLcBGAs/s1600/AW708510_10.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pisang2') or (text == 'pisang2'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-SrbGOhOcgc8/Wke_z6owprI/AAAAAAAKnms/vc7_c55NREA98-E_EU_u3Gbk7cyXvZf3ACLcBGAs/s1600/AW708510_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pisang3') or (text == 'pisang3'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-RMCrIuaq0nc/Wke_0vEgNqI/AAAAAAAKnmw/Wl5FoRbXlz0b3ALJI-SAhpWmVX2ongTZgCLcBGAs/s1600/AW708510_02.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Laksanakan') or (text == 'Ok siap'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-5zuWnTfuLrQ/WyhbjPawoeI/AAAAAAANIz0/EBKlSGHX9hIFj3ATYkcaGzbypVRzViipwCLcBGAs/s1600/AW1238502_02.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bomat') or (text == 'Bodo amat'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-XaxpSN2sY_8/WL00p-1296I/AAAAAAAN0lw/-9oq6jHwE6wzKx3f3dyfeg1nULuJ4tIIwCLcB/s1600/AW386855_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mksh') or (text == 'Thank'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-TB5GXQQXLto/WL00psnryZI/AAAAAAAN0ls/Xpyr2jhPZho8iNdQF0HdaADFUPzAMF72gCLcB/s1600/AW386855_02.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Anjay') or (text == 'Njay'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-vSWZs-330CA/Wyhbkesgp2I/AAAAAAANI0E/LAWKSGoELcEHdA00rh0PgpgNMv1EnZirQCLcBGAs/s1600/AW1238502_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Hmm') or (text == 'Hmmm'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-l6fgHHlv5l8/WykcspjpKhI/AAAAAAAgXdo/z7PQC0mZJPUpoylsOaFkxi0eeOMIpkCHACLcBGAs/s1600/AW1237813_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gift') or (text == 'gift'):
        message1 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-arvHWmHfsvE/W9mRqtlljtI/AAAAAAAABRk/NW9W8zXzu3wYhrZgX4CgnfVpvZ0vsTEGwCJoC/w510-h477-n-rw/0444.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        message2 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-gTlzFCvzVg0/W9mRqhbyBpI/AAAAAAAABRk/sh_H4ZvX324hb1sU9DIGNOcjV0LzEwo-gCJoC/w485-h477-n-rw/0111.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        message3 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-7Abvz5IhB5s/W9mRqsE14DI/AAAAAAAABRk/zaGVDJajkbYKtRlKK6_COCW7bFJ8x_ipACJoC/w509-h477-n-rw/0333.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        message4 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-P79QXZuRIaE/W9mRquYtcNI/AAAAAAAABRk/4ZruYxENrjUSOreRC2L2brNG_82WS-ZfwCJoC/w540-h477-n-rw/0222.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(
                event.reply_token, [
                    message1,
                    message2,
                    message3,
                    message4
                ]
            )
#===============================================================
#===============================================================================================
    elif (text == 'Udud Brow') or (text == 'Udud bro') or (text == 'Sambil udud brow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-qp6-x_MJOTo/W7duhg5hl3I/AAAAAAAABBo/chEKABTP3Js-CfVBirxusHndsySBkVToQCJoC/w150-h150-n-rw/krisukuran%2Bkecil.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Terlena') or (text == 'Terpana'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-GZtSXJV3ubg/W7oBNFwIW3I/AAAAAAAABIQ/HmCBwJ83FBIA9in_X1IB-yhjVFqd1tOZQCJoC/w105-h105-n-rw/1111111111111111.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mantap') or (text == 'Tikung') or (text == 'Nikung'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-5LPIi-A0A4w/W7gAYivP9TI/AAAAAAAABDo/txLEFe8KYwwsQrTfbT8V-rEHH-NtvdRbQCJoC/w135-h135-n-rw/krkrkrrrrrrrrrrrrrrrrrrr.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mimi uu brow') or (text == 'Sambil mimi brow') or (text == 'Mimi uu'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-Dy0fzicTJRA/W7gDbez9UxI/AAAAAAAABEc/l8csTiCUCWMAktPPb7VxQaT-M5VSP9a5gCJoC/w87-h87-n-rw/bromadddddddddddddd.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sambil ngopi brow') or (text == 'Sambil kopi brow') or (text == 'Kopi brow') or (text == 'Kopi bro') or (text == 'Sambil ngopi bro'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-yPJtZV8RrZE/W7n-YN3s7cI/AAAAAAAABHQ/5tPWDXlAnbc1LRecpv0BJzNA6O-jwpbpQCJoC/w150-h150-n-rw/hajiirrrrrrrrrr.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#==================================================
    elif text == 'Oh' or text == 'Ooh':
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-sQ-7Vzo76f4/WyhdsXue8qI/AAAAAAANJPk/VYxa7abxAWMVjhNxcURfVKta5NVc9qJNwCLcBGAs/s1600/AW1238589_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Kemeng' or text == 'kemeng':
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-3MXW9EujSPs/W3gDYSTMU1I/AAAAAAAZBCM/VAaceV7Xc8IOcTEpkkeS-hAs66PKVFtSgCLcBGAs/s1600/AW1575124_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#======================================================================
    elif text == 'Kemeng naga1' or text == 'Naga1':
        message1 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510674/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message2 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510675/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message3 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510676/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message4 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510677/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        #line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(
                event.reply_token, [
                    message1,
                    message2,
                    message3,
                    message4
                ]
            )
    elif text == 'Kemeng naga2' or text == 'Naga2':
        message5 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510678/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message6 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510679/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message7 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510680/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        message8 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510681/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                    )
                ]
            )
        )
        #line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(
                event.reply_token, [
                    message5,
                    message6,
                    message7,
                    message8
                ]
            )
#==========================================================================
    elif (text == 'Rokok') or (text == 'Udud'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319902/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Cantiknya') or (text == 'Ayune'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319903/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Cukup dua saja') or (text == 'Cukup 2 aja') or (text == 'Cukup 2') or (text == '2 aja'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319904/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hajar brow') or (text == 'Hajar bro'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319905/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Nah loh') or (text == 'nah loh'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319906/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Nah kan') or (text == 'nah kan'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319907/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sedot brow') or (text == 'Hisap brow'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319908/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Lihat aja') or (text == 'Liat aja'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/95319909/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/4998879')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#===============================================================================================================
    elif (text == 'Nah itu') or (text == 'nah itu'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521302/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Lemper') or (text == 'Baper'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521303/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mantap brow') or (text == 'Mantap bro'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521304/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Wasyik') or (text == 'wasyik'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521305/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Siap 86') or (text == '86 brow'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521306/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Apa lu') or (text == 'Kapok'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521307/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kopi uu'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521308/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gendeng woy'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/96521309/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5032081')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=========================================================================================================================
    elif (text == 'Tikung aku donk') or (text == 'Tikung donk'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025142/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Upst') or (text == 'Keceplosan'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025143/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Buat kamu') or (text == 'Buat km'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025144/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Di atas ngapain') or (text == 'Ngapain di atas'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025145/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pada kmn neh') or (text == 'Pada kmn'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025146/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gak mau') or (text == 'Moh'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025147/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pasti pd mojok') or (text == 'Pada mojok') or (text == 'Pasti mojok'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025148/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gara2 kamu') or (text == 'Gara2 km') or (text == 'Kamu seh'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/100025149/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5133176')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#===============================================================================================================
    elif (text == 'Goyang donk') or (text == 'goyang donk') or (text == 'Goyang dong'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612118/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Apa sih') or (text == 'Apa seh') or (text == 'Kepo'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612119/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pada ngapain') or (text == 'Ngapain') or (text == 'ngapain'):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612120/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Ass') or (text == 'ass') or (text == "Assalamu'alaikum"):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612121/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Wslm') or (text == 'Waalaikumsalam') or (text == "wslm"):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612122/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Met pagi') or (text == 'Pgi') or (text == "Pagiii"):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612123/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Udah pada ngopi blm') or (text == 'Udah ngopi blm') or (text == "Ngopi"):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612124/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Udah pada mkn blm') or (text == 'Udah mkn blm') or (text == "Mkn") or (text == "Makan"):
        message = TemplateSendMessage(
            alt_text='Sticker Kris Manis',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/102612125/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/S/sticker/5206151')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#===============================================================================================================
    elif (text == 'Sodok woy') or (text == 'sodok woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-NOqpi3Jtzpo/WfTBCBO0bHI/AAAAAAAL7G4/Nk8zSMB9-54iq7WJ2uJcNt_ghC7qM21UwCLcBGAs/s1600/AW594934_10.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kenyot woy') or (text == 'kenyot woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-jAUybQWtvhw/WfTBEhQ9klI/AAAAAAAL7HQ/MXz-SExzbughM20tk15fch6T69Ej3mDzACLcBGAs/s1600/AW594934_16.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kemeng woy') or (text == 'kemeng woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-UsLVtXb2Ats/WfTBF8VhfCI/AAAAAAAL7Hk/NB9HR98Cq_wtbKHdgbt9hF0Hr29eHX8OACLcBGAs/s1600/AW594934_21.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Nungging woy') or (text == 'nungging woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://1.bp.blogspot.com/-LSzCLvB3bQ4/WEqL8xRoftI/AAAAAAAETkM/vDvwhe7xJWod5rnQ1Hv1samFHQXvx3ErQCLcB/s1600/AW331300_10.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bool woy') or (text == 'bool woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-UyTbNR9WEkk/WfTA_1oJi3I/AAAAAAAL7Gc/CyA0eV7B2nEvEJA9UQjrdRcUpGbvyvNpwCLcBGAs/s1600/AW594934_03.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Naikin woy') or (text == 'Ebol woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-YWFYPiYoMSE/WfTBDuQhxHI/AAAAAAAL7HI/rnoe74yUy1Ehoud6i_AZ3S5Lsv-79N9ywCLcBGAs/s1600/AW594934_14.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tunggingin') or (text == 'tunggingin'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://pic.pimg.tw/win54000/1509946828-4249195164.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Lari') or (text == 'lari'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://1.bp.blogspot.com/-VcrxRZW1iiU/WIYkwx21PMI/AAAAAAAFnAo/Oyy3B-cJlxEQ_c92-oF7sivSwt-ppFP3gCLcB/s1600/AW367991_23.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Jilat woy') or (text == 'jilat woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://4.bp.blogspot.com/-PHU3V6xuExg/WIYkvpv7FLI/AAAAAAAFnAM/9mLkLJITbiwAmXz0Cnc_Ef9LuRj3JlzVwCLcB/s1600/AW367991_15.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bomat woy') or (text == 'bomat woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://1.bp.blogspot.com/-1_npZkypdgo/WEqL-E8jabI/AAAAAAAETko/BZp8EF8Rzrk_ozKihC8Wd0gUK2jI1ZiGACLcB/s1600/AW331300_16.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mbut woy') or (text == 'Jembut woy'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://1.bp.blogspot.com/-DX2XKr7tp7U/WIYkv1Jkn8I/AAAAAAAFnAQ/ZTgHhMn_j10ewFmJrQw1gI8iMD6ZSMdTACLcB/s1600/AW367991_17.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Yoi') or (text == 'Jiah'):
            message = TemplateSendMessage(
                alt_text='Sticker Kris Manis',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://1.bp.blogspot.com/-eNAJXyJD8sk/WUpZ83JxkrI/AAAAAAAAN_Y/TtBqmDfm8D0JYF62SfGWyEBia7visG6kQCLcBGAs/s1600/AW454875_01.gif',
                            action=URIAction(uri='https://line.me/ti/p/~kriskemeng2')
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, message)
#===============================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
