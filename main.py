import sys
import praw
import os
import time
reddit = praw.Reddit(
    client_id="",
    client_secret="",
    password="",
    user_agent="",
    username="",
    redirect_uri="https://www.youtube.com",
)

print('Kullanıcı: ' + os.getlogin())
print('Hesap Adı: ' + str(reddit.user.me()) )
print('Post Linkini Girin:')
link = input()
print('Link: ' + link)
submission = reddit.submission(url=link)
print("Dosya Adı Seçecek Misiniz (evet-hayır)")

sec = input()

if sec == "evet":
  print("Dosya Adı Ne Olsun:")
  ad = input()
else:
    ad = (str(submission))
    print("Dosya Adı: " + ad)

if os.path.exists(str(ad)) == False:
    print("Dosya oluşturuşuyor")
    f = open(str(ad), 'w', encoding="utf-8")
else:
    print("Dosya çoktan oluşturulmuş. Eski dosyayı silmek ister misiniz (evet-hayır)")
    sil = input()
    if sil == "evet":
        print('Dosya çoktan oluşmuş, eski dosya siliniyor.')
        os.remove(ad)
        print("Silindi. Yenisi oluşturuşuyor")
        f = open(str(ad), 'w', encoding="utf-8")
    else:
        time.sleep(1)
        sys.exit("Çıkış yapılıyor")


submission.comments.replace_more(limit=1)
for top_level_comment in submission.comments:
    ##print(top_level_comment.body)
    f.write(str(top_level_comment.body + '\n' + '\n'))
##submission.award()

print('Başarıyla oluşturuldu.')
print("Dosya adı " + "'" + ad + "'" + " olarak oluşturuldu.")
print('3 saniye içinde kapanacak')

time.sleep(3)
print('Kapatılıyor...')
