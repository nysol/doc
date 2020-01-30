#!/usr/bin/env ruby
#-*- coding: utf-8 -*-

#require 'rubygems'
#require 'mcmd'
require '../common/tex2html'

# PILをインストールする必要あり
# # ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future
# # 以下でSourceKitをダウンロード
# # http://www.pythonware.com/products/pil/
# # 解凍したディレクトリで以下を実行
# # sudo python setup.py install
# # エラーが出るようであれば、以下を試してみる
# # sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future python setup.py install

# 引数チェック
if ARGV.size != 5 and ARGV.size != 6 then
	STDERR.puts "texマニュアルをhtmlに変換する"
	STDERR.puts "#{$0} 出力dir名 "
	STDERR.puts "#{$0} xxmcmd ../../mcmd/en mcmd2.tex mcmd2.sty MCMD2"
	STDERR.puts "#{$0} xxtutorial ../../tutorial/mcmd/en tutorial.tex tutorial.sty MCMD_TUTORIAL"

	exit
end

#iPath="../../mcmd/jp"
#tex="mcmd.tex"
#sty="mcmd_jp.sty"
oPath=ARGV[0]
iPath=ARGV[1]
tex=ARGV[2]
sty=ARGV[3]
title=ARGV[4]
targetCMD=ARGV[5]
oPath=File.expand_path(oPath)
iPath=File.expand_path(iPath)

puts "###########################"
puts "convertion from tex to html"
puts "oPath:#{oPath}"
puts "iPath:#{iPath}"
puts "tex file:#{tex}"
puts "sty file:#{sty}"
puts "target command:#{targetCMD}" if targetCMD
print "ok(Y/n)? "
yn=STDIN.gets
if yn.chomp!="Y"
	puts "nothing to be done"
	exit
end

# ------------------------
# プレクリーニング実行
#  tex => #{tmpTex}

# 全ファイルコピー
puts "## copying all files from #{iPath} to ./xxsrc ..."
system "rm -rf ./xxsrc"
system "mkdir ./xxsrc"

if targetCMD
  system "cp #{iPath}/#{tex} ./xxsrc"
  system "mkdir -p ./xxsrc/examples/tex"
  system "cp #{iPath}/examples/tex/#{targetCMD}_ex.tex ./xxsrc/examples/tex"
else
  system "cp -R #{iPath}/* ./xxsrc"
end

# ターゲットのtexをクリーニング
puts "## cleaning all files under ./xxsrc ..."

# mcmd.styのクリーニング実行
# 1) 用紙設定は全て省く <= 数式が改行される
iFile="#{iPath}/#{sty}"
oFile="./xxsrc/#{File.basename(iFile)}"
puts iFile
puts oFile
File.open(iFile,"r"){|fpr|
	File.open(oFile,"w"){|fpw|
		while line=fpr.gets
#     以下の２行を有効にするとイメージの全行が大きく改行されてしまう。
#			next if line.index("setlength")
#			next if line.index("addtolength")
			fpw.puts line.chomp
		end
	}
}

# texのクリーニング実行
files=[]
if targetCMD
  Dir["#{iPath}/#{targetCMD}.tex"]             .each{|f| files << f}
  Dir["#{iPath}/examples/tex/#{targetCMD}_ex.tex"].each{|f| files << f}
else
	Dir["#{iPath}/*.tex"]             .each{|f| files << f}
	Dir["#{iPath}/examples/tex/*.tex"].each{|f| files << f}
end
files.each{|iFile|
	name=iFile.sub("#{iPath}/","")
	oFile="./xxsrc/#{name}"
	File.open(iFile,"r"){|fpr|
		File.open(oFile,"w"){|fpw|
			while line=fpr.gets
				# Verbatim => verbatimに変更
				if line.index('begin{Verbatim}')
					fpw.puts '\begin{verbatim}'
					next
				end
				if line.index('end{Verbatim}')
					fpw.puts '\end{verbatim}'
					next
				end

				# hyperref[] => hyperlink{}に変更
				while line.index('\\hyperref')
					line=~/\\hyperref\[(.+?)\]/
					line.sub!("[#{$1}]","{#{$1}}")
					line.sub!("\\hyperref","\\hyperlink")
				end

				# 図\ref => Figure \ref
				while line.index('図\\ref')
					line.sub!("図\\ref","Figure \\ref")
				end

				# 表\ref => Table \ref
				while line.index('表\\ref')
					line.sub!("表\\ref","Table \\ref")
				end

				fpw.puts line.chomp
			end
		}
	}
}

# mcmd.texは特別に最初からクリーニング実行
# 1) jsbook => book
iFile="#{iPath}/#{tex}"
oFile="./xxsrc/#{File.basename(iFile)}"
puts iFile
puts oFile
#File.open(iFile,"r"){|fpr|
#	doc=fpr.read
	#doc.gsub!(/run:(.+).pdf/,"../"+'\1'+"/index.html")
#	doc.gsub!("jsbook","book")

#	File.open(oFile,"w"){|fpw|
#		fpw.write(doc)
#	}
#}

File.open(oFile,"w"){|fpw|
  File.open(iFile,"r"){|fpr|
    while line=fpr.gets
      line=line.strip
      line.gsub!("jsbook","book")

      #next unless targetCMD and line=~/^\\include\{#{targetCMD}\}/
		  if targetCMD
        if line=~/^\\include/
          next unless line=~/\{#{targetCMD}\}/
        end
      end

# plastex cannot handle japanese charactor in printindex
			next if line=~/printindex/
      fpw.puts(line)
    end
  }
}

# ------------------------
# HTMLへの変換 plastexの実行
# #{tmpTex} => #{oPath}/*
# oPath, tmpTexともに絶対パス指定になっている。
#   => plastex実行時に\include{xxx.tex}が相対パス指定となっているため。
# --titleはnavigationバーの真ん中に表示される文字列
# --split-levelを指定しなければ節毎に分割されたhtml文書が生成される
# --base-urlは右上のtable of contentsのnavigation link
puts "## converting tex to html using plastex ..."
system "mkdir #{oPath}"
system "(cd ./xxsrc ; plastex                 -d #{oPath} --title=#{title} --split-level=1 #{tex})"

# ------------------------
# ポストクリーニング実行
# google analyticsのjavaスクリプトを埋め込む
googleAna=<<'EOF'
<script>
 	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
 	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
 	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
 	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43616783-2', 'sakura.ne.jp');
 	ga('send', 'pageview');
</script>
EOF

googleSE=<<'EOF'
    <div id="search" style="width:350px;float:right;">
    <script>
        (function() {
         var cx = '001852874768317180488:o1yevsdh0xa';
         var gcse = document.createElement('script');
         gcse.type = 'text/javascript';
         gcse.async = true;
         gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
         '//www.google.com/cse/cse.js?cx=' + cx;
         var s = document.getElementsByTagName('script')[0];
         s.parentNode.insertBefore(gcse, s);
         })();
        </script>
    <gcse:search></gcse:search>
    </div>
<div class="navigation">
EOF

Dir["#{oPath}/*.html"].each{|htmlFile|
	puts "converting #{htmlFile}"
	doc=nil
	File.open(htmlFile,"r"){|fpr|
		doc=fpr.read()
	}
	doc.sub!("</head>","#{googleAna}\n</head>")
	doc.gsub!("x8x","   ")
	File.open(htmlFile,"w"){|fpw|
		fpw.write(doc)
	}
}
