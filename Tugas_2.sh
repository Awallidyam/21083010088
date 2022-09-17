echo "siapa namamu?"
read nama
echo -e "\nHalo $nama :)\nSelamat datang di latihan soal matematika"
echo -e "\nApakah mau langsung mengerjakan soal?"
echo "iya/tidak?"
read tanya

if [ $tanya == "iya" ]
then
  echo "oke selamat mengerjakan $nama"
  echo -e "\nHitunglah soal ini di bawah ini!"
  let pilih=$RANDOM%10
  let a=$pilih
  echo "a=$a"
  echo "Masukkan angka b: "
  read b
  let jumlah=$a+$b
  echo "a + b = "
  echo "Berapakah hasilnya?"
  read hasil
  if [ $hasil == $jumlah ]
  then
   echo "wah jawaban kamu benar"
  else
   echo "yah hasil kamu salah, selamat mencoba lagi"
  fi
else
 echo "hmm oke deh"
fi
