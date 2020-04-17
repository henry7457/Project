from discord import Webhook, RequestsWebhookAdapter, Embed, Color

def avatar_url():
    return "https://cdn.discordapp.com/avatars/663939917314785280/b63669f142e713de30f1f5f48b33502d.webp?size=128"
def icon_url():
    return "https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png"

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title='Successfully checked out!',description='Supreme®/Nike® Air Force 1 Low',color=Color.from_rgb(50,205,50))
    embed.set_thumbnail(url= 'https://images-ext-2.discordapp.net/external/oZ9NZ_e_5aWNao7YxIN1ucMww2JMeaE_85SJ5Ed1psM/https/assets.supremenewyork.com/187522/rs/xPJPEIEnx74.jpg?width=80&height=80')
    embed.add_field(name='Store',value='Supreme US')\
    .add_field(name='Size',value='8')\
    .add_field(name='Profile',value='||Test||')\
    .add_field(name='Order',value='||94218534||')\
    .add_field(name='Color',value='White')\
    .add_field(name='Catgory',value='Shoes')\
    .add_field(name='Captcha Bypass',value='Enabled')\
    .add_field(name='Mode',value='Safe')\
    .set_footer(icon_url=icon_url(),text='CyberAIO • 20/03/2020 11:00:53.055')

    webhook.send(embed=embed,avatar_url=avatar_url(),username="CyberAIO")

if __name__ == '__main__':
    send_webhook()
