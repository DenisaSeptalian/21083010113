#!/bin/bash
printf "Makanan apa yang kamu suka ?\n"
printf "geprek ?\n"
printf "penyetan ?\n"
printf "bubur ?\n"

read makanan

case "$makanan" in
"geprek")
echo "geprek mbk rara cuman 1ok!"
;;
"penyetan")
echo "penyetan kantin upn harganya 12k"
;;
"bubur")
echo "bubur depan uppn murah banget"
;;
*)
echo "ya udah gk usah tanya"
;;
esac
