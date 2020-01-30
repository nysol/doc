#!/usr/bin/env ruby
# coding: utf-8

system "rm *.csv"

# 「例1」のように例の番号に利用するカウンター
$counter=1

# $0: ./func_sum.rb
# => tex: tex/func_sum_ex.tex
$tex="tex/"+$0.sub("./","").sub(".rb","")+"_ex.tex"
system "rm -f #{$tex}"

def run(scp,title,comment,iFiles="",oFiles="")
	# スクリプトのファイル書き出し
	File.open("xxscp","w"){|fpw| fpw.write(scp)}
	# --verboseで実行コマンド行も表示する
	system 'bash --verbose xxscp &>xxlog'

	# 以下、logとscpをマッチングさせ、コマンド実行行の先頭に"$ "をつける。
	log=""
	File.open("xxscp","r"){|fscp|
	File.open("xxlog","r"){|flog|
	scpEQlog=true
	# notTop=false
	while true
 		logLine=flog.gets()
 		scpLine=fscp.gets() if scpEQlog
		break unless logLine
		scpEQlog=false
		if scpLine
			scpToken=scpLine.chomp.split(" ")[0]
			logToken=logLine.chomp.split(" ")[0]
			scpEQlog=true if scpToken==logToken
		end
		#log << "\n" if notTop and scpEQlog
		log << "$ " if scpEQlog
		#log << logLine.chomp. + "\n"
		log << "#{logLine.chomp.sub(/;.+$/,'')}\n"
		#notTop=true
	end
	}
	}

	###### スクリプトをファイル化&実行&終了メッセージ取得
	#File.open("xxhead","w"){|fpw| fpw.print "$ "}
	#system 'rm -rf xxlog'
	#scp.split("\n").each{|exe|
	#	File.open("xxscp","w"){|fpw| fpw.write(exe)}
	#	system 'bash xxscp &>xxmsg'
	#	msg=nil
	#	File.open("xxmsg","r"){|fpr| msg=fpr.read}
  #	msg=msg.sub(/;.+$/,'')

	#	system "cat xxhead >>xxlog"
	#	system "cat xxscp >>xxlog"
	#	File.open("xxlog","a"){|fpw| fpw.puts ""}
	#	#system "cat xxmsg >>xxlog"
	#	File.open("xxlog","a"){|fpw| fpw.puts "#{msg}\n"}
	#}
  #doc << "#{endmsg.sub(/;.+$/,'')}\n"

	#log=nil
	#File.open("xxlog","r"){|fpr| log=fpr.read}
	#File.open("xxscp","w"){|fpw| fpw.write(scp)}
	#system 'bash --verbose xxscp 2>xxlog'
	#log=nil
	#File.open("xxlog","r"){|fpr| log=fpr.read}

	###### 表示する入力ファイル内容を全て変数に代入
	iDisps=[]
	iFiles=iFiles.split(",")
	iFiles.each{|file|
		File.open(file,"r"){|fpr| iDisps << fpr.read}
	}

	###### 表示する出力ファイル内容を全て変数に代入
	oDisps=[]
	oFiles=oFiles.split(",")
	oFiles.each{|file|
		File.open(file,"r"){|fpr| oDisps << fpr.read}
	}

	##### tex文書生成
	doc="\n"
	doc << "\\subsubsection*{例#{$counter}: #{title}}\n"
	doc << "\n"
	doc << "#{comment}"
	doc << "\n"
	doc << "\\begin{Verbatim}[baselinestretch=0.7,frame=single]\n"

	(0...iDisps.size).each{|i|
		doc << "$ more #{iFiles[i]}\n"
		doc << "#{iDisps[i]}\n"
	}

	#doc << "$ #{scp}"
	#doc << "#{endmsg.sub(/;.+$/,'')}\n"
	doc << log
	(0...oDisps.size).each{|i|
		doc << "$ more #{oFiles[i]}\n"
		doc << "#{oDisps[i]}"
		puts "\n" if i<oDisps.size-1
	}

	doc << "\\end{Verbatim}\n"

	# texファイルには追記していく
	File.open($tex,"a"){|fpw|
		fpw.puts doc
	}

	# 標準出力には垂れ流し
	puts doc

	$counter+=1
end

