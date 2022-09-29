echo -n "masukkan angka yang kamu mau "
read angka;
a=0

until [ ! $angka -gt $a ]
do
  echo $angka
  angka=$((angka-2))
done
