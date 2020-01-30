
./tex2html.rb xxtutorial ../../tutorial/mcmd/jp tutorial.tex tutorial.sty MCMD_TUTORIAL
cp -R ../../tutorial/mcmd/jp/exercise ./xxtutorial
rm -rf ./xxtutorial/tutorial_jp

rm -rf jp
cp -R xxtutorial jp
scp -r jp nysol@nysol.sakura.ne.jp:~/www/tutorial/

