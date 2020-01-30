
./tex2html.rb xxfumi ../../fumi/jp fumi.tex fumi.sty FUMI

rm -rf jp
cp -R xxfumi jp
scp -r jp nysol@nysol.sakura.ne.jp:~/www/fumi/
