
#./tex2html.rb xxmcmd2 ../../mcmd2/jp mcmd2.tex mcmd_jp.sty MCMD2
#./tex2html.rb xxmcmd ../../mcmd/jp mcmd.tex mcmd_jp.sty MCMD2
#./tex2html.rb xxmcmd2 ../../mcmd/jp mcmd.tex mcmd_jp.sty MCMD2
./tex2html.rb xxmcmd ../../mcmd/jp mcmd.tex mcmd_jp.sty MCMD
rm -rf jp
#cp -R xxmcmd2 jp
cp -R xxmcmd jp
#scp -r jp nysol@nysol.sakura.ne.jp:~/www/mcmd2/

