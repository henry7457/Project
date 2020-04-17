from discord import Webhook, RequestsWebhookAdapter, Embed, Color

def icon_url():
    return "https://images-ext-2.discordapp.net/external/zgUG44I9dqW193Y6_Vv7aMrJ92DO4gCy5VVd9u9cpXg/http/icons.iconarchive.com/icons/iconscity/flags/256/usa-icon.png"

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title='Successful Checkout!:white_check_mark:',color=Color.from_rgb(50,205,50))
    embed.set_thumbnail(url='https://images-ext-2.discordapp.net/external/xSpQEjwaK72NQT27CL1M7cVg7XFIUisuFAEmV4ZfVRs/https/assets.supremenewyork.com/185568/sm/bq8EZBTj4n8.jpg?width=80&height=80')
    embed.add_field(name='Product',value='Motion Logo Hooded Sweatshirt')\
    .add_field(name='Size/Color',value='Large/White')\
    .add_field(name='订单号（order#)',value='||78654958||')\
    .add_field(name='ProfileName',value='Test')\
    .add_field(name='Checkout IP',value='||TCB||')\
    .add_field(name='App Version',value='0.5.3')\
    .add_field(name='模式（mode)',value='browser')\
    .add_field(name='Checkout Speed',value='6.876s')\
    .add_field(name='Queued',value='True')\
    .add_field(name='Dropped Time',value='2020-04-09T15:00:13.681Z')\
    .add_field(name='CaptchaBypass',value='True')\
    .add_field(name='ThreeDBypass',value='False')\
    .add_field(name='RestockMode',value='True')\
    .add_field(name='TicketMode',value='True')\
    .add_field(name='Status',value='paid')\
    .add_field(name='PookyCookie',value='Cookie: ticket=9ef03a7826de73de51ff397ed687ef13de976f101b5db095e98b8d24c9f26513e8bb1b841b038b0b4bb3652061160c5e8cea9a7d273c933c51bc19dfe66622741586444415_ticket=469f0ed8604253f2dfa701edd245a48c4890f8a527cf622756a106611a06ff8dd3a0ab4e9392426e16f284ac227e7cc597a831f4dc9a725278e1c98bfba8e2fe1586444418')\
    .set_footer(icon_url=icon_url(),text='2020-04-09T15:02:35.664Z')

    webhook.send(embed=embed,username="Mek Bot")

if __name__ == '__main__':
    send_webhook()
