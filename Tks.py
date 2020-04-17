from discord import Webhook, RequestsWebhookAdapter, Embed, Color


def send_webhook():
    url = ''


    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    content = "Success: adidas Originals Yeezy Boost 350 V2 - Men's"


    embed = Embed(title='You cooked',color=Color.from_rgb(155,89,182))

    embed.set_thumbnail(url= 'https://images-ext-1.discordapp.net/external/slLUJkwr81yr4FTh19TyyD-D7_-xNVihD19n45AeZwY/https/images.footlocker.com/pi/9033FL/cart/9033FL.jpeg')
    embed.add_field(name='Website',value='Footlocker.com')\
    .add_field(name='Product',value='adidas Originals Yeezy Boost 350 V2 - Men\'s')\
    .add_field(name='Size',value='||10||')\
    .add_field(name='Price',value='$220.00')\
    .add_field(name='Link',value='9033FL')\
    .add_field(name='Profile',value='||Test||')\
    .add_field(name='Proxy',value='||TCB||')\
    .add_field(name='Time Stamp(utc)',value='2020-02-23 01:10:32AM')\
    .add_field(name='Mode',value='Safe')

    webhook.send(content, embed=embed)

if __name__ == '__main__':
    send_webhook()
