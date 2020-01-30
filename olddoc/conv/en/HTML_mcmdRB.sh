
./tex2html.rb xxmcmdRB ../../ruby/en mcmdRB.tex mcmdRB.sty MCMDRB

rm -rf en
cp -R xxmcmdRB en
scp -r en nysol@nysol.sakura.ne.jp:~/www/mcmdRB/

