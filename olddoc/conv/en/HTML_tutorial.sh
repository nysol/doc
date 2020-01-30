
./tex2html.rb xxtutorial ../../tutorial/mcmd/en tutorial.tex tutorial.sty MCMD_TUTORIAL
cp -R ../../tutorial/mcmd/en/exercise ./xxtutorial
rm -rf ./xxtutorial/tutorial_en

rm -rf en
cp -R xxtutorial en
scp -r en nysol@nysol.sakura.ne.jp:~/www/tutorial/

