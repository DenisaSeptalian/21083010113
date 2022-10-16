#!/bin/bash
echo "---------------------------------------"
echo "Program menghitung Menghitung nilai IPK"
echo "---------------------------------------"
echo -n "Masukan Nama  :"
read nama
echo -n "Masukan NPM   :"
read NPM
echo -n "Masukan Nilai Tugas  : "
read Tugas
echo -n "Masukan Nilai UTS    : "
read UTS
echo -n "Masukan Nilai UAS    : "
read UAS
echo
echo "---------------------------------------"
echo "Daftar nilai semester"
echo "---------------------------------------"
echo "Nama : $nama "
echo "NPM  : $NPM "
echo "Nilai: $Tugas "
echo "Nilai: $UTS "
echo "Nilai: $UAS "

total=`expr $Tugas + $UTS + $UAS`
IPK=`echo $total /3 |bc`

echo "IPS mahasiswa = $total / 3"
echo "IPk Mahasiswa = $IPK"
