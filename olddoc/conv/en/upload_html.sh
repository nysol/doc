
rm -rf jp
cp -R $1 jp
scp -r jp nysol@nysol.sakura.ne.jp:~/www/mcmd
