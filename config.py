import os

api_id = int(os.environ.get("API_ID", "25478698"))
api_hash = os.environ.get("API_HASH", "7a80ffea6f9a06ec540a9fdf0fafb487")
bot_token = os.environ.get("BOT_TOKEN", "6382495868:AAFu3qlrkMCkJQSE2ew2PUPmXRyjs4C0nRc")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://Alexa:alexa@cluster0.h0zqfue.mongodb.net/true?retryWrites=true&w=majority")
db_name = os.environ.get("DB_NAME", "menfess")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1002063224209"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1001942915917"))
channel_3 = int(os.environ.get("CHANNEL_3", "-1001942915917"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002130790212"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "6366185217"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#NekoGirl #NekoBoy #NekoAsk #NekoFind #NekoSpill #NekoStory #NekoTalent").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/387bdabb03deaf94fa4e9.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/2bc2dc1fad8e33cf69e6d.jpg")
pic_talentgirl = os.environ.get("PIC_TALENTGIRL", "https://telegra.ph/file/95801451d752f089f8e1e.jpg")
pic_daddysugar = os.environ.get("PIC_DADDYSUGAR", "https://telegra.ph/file/14ca710511333621be61d.jpg")
pic_moansgirl = os.environ.get("PIC_MOANSGIRL" , "https://telegra.ph/file/10232ac2404b3e822f99d.jpg")
pic_moansboy = os.environ.get("PIC_MOANSBOY" , "https://telegra.ph/file/90359cf42550732058d20.jpg")
pic_gfrent = os.environ.get("PIC_GFRENT" , "https://telegra.ph/file/432e8cb26179ade6eba70.jpg")
pic_bfrent = os.environ.get("PIC_BFRENT" , "https://telegra.ph/file/e0dc732430d9b1b0cbfa1.jpg")
pic_owner = os.environ.get("PIC_OWNER" , "https://telegra.ph/file/f58b957f34a978524f07a.jpg")
pic_neko = os.environ.get("PIC_NEKO" , "https://telegra.ph/file/2d46007dd7d22645c4ec3.jpg")
pic_admingirl = os.environ.get("PIC_ADMINGIRL" , "https://telegra.ph/file/30c7b36f68d69840a762c.jpg")
pic_adminboy = os.environ.get("PIC_ADMINBOY" , "https://telegra.ph/file/192be803ec6722b3935ab.jpg")
# ============================================================#
pic_rekberboy = os.environ.get("PIC_REKBERBOY", "https://telegra.ph/file/78acf322385616cb5bab0.jpg")

# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak dapat diakses harap join terlebih dahulu")
start_msg = os.environ.get("START_MSG", """"
❏ Haii {mention}
<b>silahkan kirim pesan anda menggunakan hashtag:</b>

• #mba [ untuk identitas perempuan]
• #mas [ untuk identitas laki-laki ]
• #spill [ untuk spill masalah ]
• #tanya [ untuk bertanya ]
• #story [ untuk berbagi cerita/curhat ]
• #pap [ khusus media foto/video ]

<b>Contoh pesan:</b> <code>#mas yang dari jogja. meet yuk {username} </code>

<b>pastikan kamu sudah baca <a href="https://t.me/JAWAFES/9">rules</a> dan <a href="https://t.me/JAWAFES/10">help</a> terlebih dahulu</b>""")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, pesan mu gagal terkirim. silahkan baca <a href="https://t.me/JAWAFES/10">help</a> terlebih dahulu 
""")
