import os

class Config:
    aid = int(os.environ.get("API_ID", "2163860"))
    ahash = os.environ.get("API_HASH", "e0ef74bbb305f18fc731b8c9475492f1")
    bot_token = os.environ.get("BOT_TOKEN", "1524081172:AAHbRtaZKKCzgcQnp7nz_Qsn9Ejf7Be9tAs")
    sudo = [1078841825, 1076632911]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
