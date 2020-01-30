
./tex2html.rb xxview ../../view/jp view.tex view.sty VIEW

rm -rf jp
cp -R xxview jp
scp -r jp nysol@nysol.sakura.ne.jp:~/www/view/
