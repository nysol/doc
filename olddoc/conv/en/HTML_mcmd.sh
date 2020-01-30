
./tex2html.rb xxmcmd ../../mcmd/en mcmd2.tex mcmd2.sty MCMD

rm -rf en
cp -R xxmcmd en

#scp -r en nysol@nysol.sakura.ne.jp:~/www/mcmd/

