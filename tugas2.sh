#!/bin/bash
echo "halo tuan";
echo "Aku bot linux senang bisa bertemu dengan anda.......!";
echo "sekarang coba perkenakan diri anda pada kolom dibawah: ";
read nama ;
echo "wahhhh $nama adalah nama yang bagus";

echo -e "\nTuan $nama -_-\nkita ada fitur baru"
echo -e "\nApakah tuan mau mencobanya?"
echo "iya/tidak"
read tanya
 
echo "oke fitur pertama yaitu tes kejujuran"
printf "siapa orang terganteng di dunia ?\n"
printf "deniz ?\n"
printf "Denisa ?\n"
printf "Denisa septalian ?\n"
read  ganteng

 case "$ganteng" in
"deniz")
echo "iya deniz memang ganteng!"
;;
"Denisa")
echo "jelas Denisa udah ganteng baik lagi"
;;
"Denisa septalian")
echo "kalau yang ini gk usah ditanya lagi soalnya udah jelas"
;;
*)
echo "yang kamu pilih bukan orang ganteng"
;;
esac
echo "***************************************************************"
echo "***************************************************************"
echo "coba ketik next  dikolom bawah ini untuk mencoba fitur berikutnya"
read fitur 
echo "$fitur ada  fitur satu lagi nih, fiturnya adalah kalkulator sederhana"
echo "coba masukan angka pertama:"
read x
echo "masukan angka berikutnya:"
read y
echo "pilihlah oprasi kalkulator berikut"
echo "1. penjumlahan"
echo "2. Pengurangan"
echo "3. perkalian"
echo "4. pembagian"
echo "pilih oprasi yang di inginkan (1/2/3/4):"
read oprasi
if [ $oprasi -eq 1 ]
then 
let hasil=x+y
echo "Hasil penjumlahan $x dan $y ($x + $y) = $hasil"
elif [$oprasi -eq 2]
then 
let hasil=x-y
echo "Hasil pengurangan $x dan $y ($x - $y) = $hasil"
elif [$oprasi -eq 3 ]
then
let hasil=x*y
echo "Hasil perkalian $x dan $y ($x * $y) = $hasil"
elif [$oprasi -eq 4]
then
let hasil=x/y
echo "Hasil pembagian $x dan $y ($x / $y) = $hasil"
else
echo "maaf pilihan anda belum tersedia"
fi
