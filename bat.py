from pyrogram import Client, filters

api_id = 24449013
api_hash = "c6e06058575798ffd33ccfdf6643d807"
session_string = "BQF1D_UARgaFbCiTYgzf1ih56hvksfZetek4AmWZmJDnYzzLJmKqEpjdNuHQQEyAQLrQqDsO3tCl6moL2myJLHOA_ugHwCVvIz99X4ua5NRLKcgztaNwdUJLaqKLZsYMLBWNjjHGK6ChvbsHBBKyp6hBDS00vLilviV8t1VP5Do2bKtnPfJUFvQn2iGKlmZyMo9BdGD9FNOKUKHF3Oav6DUAFtwIMTM5BM7d-HnHXydqAoJmW429KE5P-nH8e7AHFRZs1rTJPBDuOsM5ltbjJWldJm9kI8RJBZuRuh_ac6G9u4pfyJ6ZxXTGSVVFm5BVnGivafXIgUIjlvl_sRAGhW5vxq0lmwAAAAHYiZhGAA"  # <-- apna full session string daalna

app = Client("MONSTERxCAPTAIN_session", api_id=api_id, api_hash=api_hash, session_string=session_string)

@app.on_message(filters.private)
def auto_reply(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="⚡ Reply from MONSTERxCAPTAIN' DON'T TRY TO SPAM"
    )

print("🤖 MONSTERxCAPTAIN bot started... waiting for messages!")
app.run()
