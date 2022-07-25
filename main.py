import sys
import praw
import os
import time

reddit = praw.Reddit(
    client_id="lw20GRFStCJVjdNTmQsEgQ",
    client_secret="Zk4po6zqzLiUjtzsdtN37-tUsrF9vw",
    password="",
    user_agent="evet-nasilsiniz",
    username="",
    redirect_uri="https://www.youtube.com",
)
reddit.read_only = True     #Read only böylece username ve password girmeden kullanılabilir
print('Kullanıcı: ' + os.getlogin())    #Kullanıcı ismi alma
#print('Hesap Adı: ' + str(reddit.user.me()) )      #Reddit kullanıcı adını yazma (Read only olduğundan kullanılmıyor)
print('Post Linkini Girin:')
link = input()      #Link giriş
print('Link: ' + link)
submission = reddit.submission(url=link)
print("Dosya Adı Seçecek Misiniz (evet-hayır)")

sec = input()     #Dosya adı seçilsin mi

if sec == "evet":
  print("Dosya Adı Ne Olsun:")
  ad = input()     #Dosya adı
else:
    ad = (str(submission))     #Dosya adını post idsi yap
    print("Dosya Adı: " + ad)

if os.path.exists(str(ad)) == False:   #Dosya var mı yok mu kontrol etme
    print("Dosya oluşturuluyor")
    f = open(str(ad), 'w', encoding="utf-8")    #Dosya oluşturma
else:
    print("Dosya çoktan oluşturulmuş. Eski dosyayı silmek ister misiniz (evet-hayır)")
    sil = input()    #Silinsin mi sorusu
    if sil == "evet":
        print('Dosya çoktan oluşmuş, eski dosya siliniyor.')
        os.remove(ad)    #Aynı addan dosya varsa silme
        print("Silindi. Yenisi oluşturuşuyor")
        f = open(str(ad), 'w', encoding="utf-8")    #Dosya oluşturma
    else:
        time.sleep(1)   #Delay
        sys.exit("Çıkış yapılıyor")     #Dosya adı koyulmayacaksa çıkış


submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:    #Yorumları alır
    #print(top_level_comment.body)          #Yorumları konsola yazar (en baştaki # silinerek aktifleştirilebilir)
    f.write(str(top_level_comment.body + '\n' + '\n')) #Yorumları dosyaya yazar


print('Başarıyla oluşturuldu.')
print("Dosya adı " + "'" + ad + "'" + " olarak oluşturuldu.")
print('1 saniye içinde kapanacak')

time.sleep(1)   #Delay2
print('Kapatılıyor...')
