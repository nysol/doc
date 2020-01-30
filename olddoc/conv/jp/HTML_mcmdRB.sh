
./tex2html.rb xxmcmdRB ../../ruby/jp mcmdRB.tex mcmdRB.sty MCMDRB

rm -rf jp
cp -R xxmcmdRB jp
scp -r jp nysol@nysol.sakura.ne.jp:~/www/mcmdRB/

