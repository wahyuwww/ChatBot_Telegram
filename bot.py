import telebot
from telebot import types

api = '1388478702:AAG810qxQVonkQ5PovJQgxbsWqOd9f1UWJU'
bot = telebot.TeleBot(api)

  # nomor_id = message.from_user.id

  # bot.register_next_step_handler(msg,step1)
@bot.message_handler(commands=['start'])
def welcome(message):
          chat_id = message.chat.id
          custom = types.ReplyKeyboardMarkup()
          a = types.KeyboardButton('jam oprasional desa')
          b = types.KeyboardButton('Cara mengurus KK')
          c = types.KeyboardButton('Gejala Covid')
          d = types.KeyboardButton('Cara Mencegah')
          e = types.KeyboardButton('Selesai')
          custom.row(a)
          custom.row(b)
          custom.row(c)
          custom.row(d)
          custom.row(e)
          nama = message.from_user.first_name
          pesan = bot.send_message(chat_id,'''
hai apa kabar {} ??
silahkan pilih keyboard yang sudah ada yaa
kalau hilang keyboardnya ketikan start yaa yaa hehehe
    '''.format(nama),reply_markup=custom)

@bot.message_handler(content_types=['text'],)
def value_search(message):
        if message.text == "Start":
            chat_id = message.chat.id
            custom = types.ReplyKeyboardMarkup()
            a = types.KeyboardButton('jam oprasional desa')
            b = types.KeyboardButton('Cara mengurus KK')
            c = types.KeyboardButton('Gejala Covid')
            d = types.KeyboardButton('Cara Mencegah')
            e = types.KeyboardButton('Selesai')

            custom.row(a)
            custom.row(b)
            custom.row(c)
            custom.row(d)
            custom.row(e)
            nama = message.from_user.first_name
            pesan = bot.send_message(chat_id,'''
hai apa kabar {} ??
silahkan pilih keyboard yang sudah ada yaa
kalau hilang keyboardnya ketikan start yaa yaa hehehe
    '''.format(nama),reply_markup=custom)
        elif message.text == "help":
                bot.reply_to(message,'''
Hai ada yang bisa saya bantu ?
silahkan hubungi admin yaa..
0858383827
      ''')
        elif message.text == "jam oprasional desa":
           bot.reply_to(message,'''
hari senin - kamis : 08-00 sd 14.00
hari jumat : 08.00 sd 13.00
    ''')
        elif message.text == "Cara mengurus KK":
          bot.reply_to(message,'''
Sertakan surat kandungmu woiii
    ''')
        elif message.text == "Gejala Covid":
          bot.reply_to(message,'''
1. Gejala corona terbaru berupa Silent hypoxia
Gejala corona terbaru ini mengejutkan bagi sebagian dokter yang sudah berpengalaman puluhan tahun. Gejala corona terbaru ini membuat pasien menderita infeksi paru-paru kronis, dengan tingkat oksigen yang sangat rendah. Namun, tidak ada masalah pernapasan sama sekali.

Dalam sebuah opini yang ditulis untuk New York Times, Richard Levitan, MD, menjelaskan lebih dalam tentang hal ini. Dia mengatakan, kebanyakan pasien dengan kondisi tersebut dilaporkan sakit selama seminggu atau lebih dengan gejala demam, batuk, sakit perut dan kelelahan, tetapi napas mereka menjadi pendek di hari mereka datang ke rumah sakit.

"Pneumonia mereka jelas telah berlangsung selama berhari-hari, tetapi saat mereka merasa harus pergi ke rumah sakit, mereka seringkali sudah dalam kondisi kritis," ungkap dia.

Baca juga: Ini cara membedakan batuk musim kemarau dengan batuk gejala Covid-19

2. Gejala corona terbaru berupa pembekuan darah dan stroke
Salah satu gejala corona terbaru yang terkadang mematikan berkaitan dengan pembekuan darah yang tidak normal. Ahli radiologi intervensi Yale Medicine yang berspesialisasi dalam prosedur jantung yang dipandu gambar, Hamid Mojibian, MD memberikan penjelasannya.

Dia mengatakan, otopsi pasien Covid-19 menunjukkan mikroemboli (gumpalan kecil) di berbagai organ yang menjelaskan beberapa disfungsi organ pada pasien. "Pasien Covid-19 memiliki risiko lebih tinggi untuk membentuk gumpalan darah arteri yang bisa sangat berbahaya," kata dia.

Namun, tingkat berbahayanya bergantung pada di mana gumpalan terbentuk atau bermigrasi. "Semua organ dalam tubuh kita bergantung pada darah yang dibawa melalui sistem arteri untuk berfungsi dengan benar. Setiap gangguan suplai darah dapat mengakibatkan konsekuensi yang parah," tambah Mojibian.

Ada sejumlah laporan pembekuan terjadi di aorta, arteri ginjal (menyebabkan infark ginjal), dan tungkai (menyebabkan kaki hitam dan gangren). Namun, yang paling merusak adalah gumpalan di pembuluh darah otak yang dapat menyebabkan stroke, bahkan pada orang yang lebih muda.

Simak gejala corona terbaru lain di halaman berikutnya

3. Gejala corona terbaru mirip sindrom kawasaki
Pada 6 Mei lalu, otoritas negara bagian New York mengeluarkan peringatan yang menjelaskan bahwa ada 64 anak di negara bagian tersebut dirawat di rumah sakit dengan kondisi aneh. Para dokter menggambarkan kondisi mereka seperti "sindrom inflamasi multisistem pediatrik." "Secara klinis menyerupai proses inflamasi masa kanak-kanak lainnya, penyakit kawasaki." Demikian diungkapkan profesor pediatri sekaligus dokter penyakit menular pediatrik dari Yale School of Medicine, Thomas Murray, MD.

Contoh gejala corona terbaru yang harus diwaspadai orangtua antara lain demam tinggi yang berkepanjangan, mata merah, ruam, nyeri otot, muntah, dan diare. Biasanya, kondisi ini terjadi beberapa hari setelah infeksi awal.
    ''')
        elif message.text == "Cara Mencegah":
          bot.reply_to(message,'''
1. Cuci Tangan

Tindakan pertama yang dapat dilakukan untuk menangkal virus corona adalah dengan rajin mencuci tangan. Sebab, tangan adalah salah satu anggota tubuh yang menjadi sumber penyakit.

Cuci tangan dengan durasi minimal 20 detik untuk membunuh virus corona menggunakan sabun dan air bersih yang mengalir. Setelah itu, keringkan tangan menggunakan kain yang bersih atau tisu.

Tindakan pencegahan yang satu ini dianggap lebih efektif untuk membunuh kuman, bakteri, termasuk virus corona. Cuci tangan merupakan langkah yang disarankan oleh banyak pihak, termasuk Organisasi Kesehatan Dunia.

2. Hindari Sentuh Wajah

Telah diketahui bahwa tangan dapat menjadi sumber penyakit sebab sering terjadi kontak dengan benda maupun orang lain. Sementara itu, virus corona disinyalir dapat masuk tubuh manusia melalui segitiga wajah yakni mata, hidung, dan mulut.

Maka dari itu, hindari untuk menyentuh wajah menggunakan tangan. Apabila terpaksa harus menyentuh wajah, maka pastikan untuk mencuci tangan terlebih dahulu dengan sabun.
    ''')
        elif message.text == "Selesai":
          chat_id = message.chat.id
          custom = types.ReplyKeyboardRemove()
          bot.send_message(chat_id,'''
Terima kasih sudah berkunjung
Jika Ingin Memulai lagi ketikan Start
      ''',reply_markup=custom)
  # nama_akhir = message.from_user.last_name
        else:
            bot.send_message(message.chat.id, "waduh maaf yang anda masukan salah")


# @bot.message_handler(regexp="id")
# def echo_all(message):
#   nomor_id = message.from_user.id
#   nama = message.from_user.first_name
#   nama_akhir = message.from_user.last_name
#   bot.reply_to(message,'''
# hai id kamu
# id    = {}
# Nama  = {}
#     '''.format(nomor_id,nama,nama_akhir))



print('bot start running')
bot.polling()