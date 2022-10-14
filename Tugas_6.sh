#menginputkan semester dari mahasiswa
echo -n "input : "
read semester

declare -a IPSMhs #mendeklarasikan array dari IPSmhs

i=0
let jumlah=$semester-1  #dari semester yang telah diinputkan dikurangi 1

while [ $i -le $jumlah ]; #memeriksa nilai indeks sama dengan jumlah 
do
	let nilai=$i+1 
	printf " " $nilai;
	read nilaisemester;
	IPSMhs[$i]=$nilaisemester;
	let total=total+$nilaisemester;
	let i=$i+1;
done

let IPK=$total/$semester
echo "IPS mhs = " $total "/" $semester
echo "IPK mhs = " $IPK

