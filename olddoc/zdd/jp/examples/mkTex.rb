#!/usr/bin/env ruby
# coding: utf-8

system "rm *.csv"

# 「例1」のように例の番号に利用するカウンター
$counter=1

# $0: ./func_sum.rb
# => name: func_sum
# => texEx:  tex/func_sum_ex.tex
# => texFig: tex/func_sum_fig.tex
$name=$0.sub("./","").sub(".rb","")
$texEx ="tex/"+$name+"_ex.tex"
$texFig="tex/"+$name+"_fig.tex"
system "rm -f #{$texEx}"
system "rm -f #{$texFig}"

#################################
# 例としてのtexを作成
def genExample(title,comment,log,number)

if log=="" then
doc= <<"EOF"
\\subsubsection*{例#{number}: #{title}}

#{comment}
EOF
else
doc= <<"EOF"
\\subsubsection*{例#{number}: #{title}}

#{comment}

\\begin{Verbatim}[baselinestretch=0.7,frame=single]
#{log}\\end{Verbatim}
EOF
end

	return doc
end

#################################
# figureとしてのtexを作成
def genFigure(title,log,number)
doc= <<"EOF"
\\begin{figure}[htbp]
\\begin{Verbatim}[baselinestretch=0.7,frame=single]
#{log}\\end{Verbatim}
\\caption{#{title}\\label{fig:#{$name}_#{number}}}
\\end{figure}
EOF
	return doc
end

#################################
# スクリプトを実行しログを得る
def exec(scp)
	return "" if scp==""

	# スクリプトのファイル書き出し
	File.open("xxscp","w"){|fpw| fpw.write(scp)}
	# --verboseで実行コマンド行も表示する
	system "irb --prompt simple <xxscp | grep -v '^=>' | sed 's/^>>/>/' | sed 's/^\?>/>/' >xxlog "

	# 以下、logとscpをマッチングさせ、コマンド実行行の先頭に"$ "をつける。
	log=nil
	File.open("xxlog","r"){|flog|
		log=flog.read()
	}
	log.sub!(/^Switch to inspect mode.*\n/,"") # irbの最初のメッセージは削除
	log.sub!(/> \n$/,"") # 最終行に">"が入るので削除
	log.gsub!(/^> $/,"") # ">"だけの行は空行にする
	log.gsub!(/^> #/,"#") # コメント行
	log.gsub!("#VERB_BEGIN#","\\begin{Verbatim}[baselinestretch=0.7,frame=single]")
	log.gsub!("#VERB_END#","\\end{Verbatim}")
	log.gsub!("##","")
#
	return log
end

def runfig(scp,title)
	log=exec(scp)                               # scpを実行してログを得る

	doc=genFigure(title,log,$counter)           # 例形式のtexを生成
	File.open($texFig,"a"){|fpw| fpw.puts doc } # texファイルには追記していく
	puts doc                                    # 確認のため標準出力にも出力
	$counter+=1
end

def run(scp,title,comment)
	log=exec(scp)                              # scpを実行してログを得る

	doc=genExample(title,comment,log,$counter) # 例形式のtexを生成
	File.open($texEx,"a"){|fpw| fpw.puts doc } # texファイルには追記していく
	puts doc                                   # 確認のため標準出力にも出力
	$counter+=1
end

