function panjang {
	echo "Masukkan panjang persegi panjang: "
	read panjang
}
function lebar {
	echo "Masukkan lebar persegi panjang: "
	read lebar
}
function luas {
	let luas=$panjang*$lebar
	echo "Luas Persegi: "
	echo $luas
}
#Memanggil fungsi
panjang
lebar
luas
