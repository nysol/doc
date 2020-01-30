#!/usr/bin/env ruby
#-*- coding: utf-8 -*-

require 'rubygems'

# 引数チェック
if ARGV.size != 2 and ARGV.size != 3 then
	STDERR.puts "tex2help.rbで変換したhelp文書(*.hファイル)をmcmdのソースにコピーする"
	STDERR.puts "#{$0} 入力dir名 出力ディレクトリ名 [run]   : runを指定しないと確認だけ"
	STDERR.puts "#{$0} xxhelp ~/nysol/mcmd/lib/help/jp"
	exit
end

iPath=ARGV[0]
oPath=ARGV[1]
exe=ARGV[2]

iFiles=[]
Dir["#{iPath}/*.h"].each{|f|
	iFiles << f.sub("#{iPath}/","")
}
oFiles=[]
Dir["#{oPath}/*.h"].each{|f|
	oFiles << f.sub("#{oPath}/","")
}
allFiles=(iFiles+oFiles).uniq

iNotExist=[]
oNotExist=[]
diff=[]
same=[]
allFiles.each{|file|
	iExist=File.exist?("#{iPath}/#{file}")
	oExist=File.exist?("#{oPath}/#{file}")

	if iExist and oExist then
		system("diff #{iPath}/#{file} #{oPath}/#{file} >xxdifflog")
		size=File.size("xxdifflog")
		if size==0 then
			same << file
		else
			diff << file
		end
	elsif not iExist
		iNotExist << file
	elsif not oExist
		oNotExist << file
	end
}

puts "1) #{iPath}に存在して、#{oPath}に存在しないコマンド:"
p oNotExist
puts "2) #{oPath}に存在して、#{iPath}に存在しないコマンド:"
p iNotExist
puts "3) 両方に存在して内容が異なるコマンド:"
p diff
puts "4) 両方に存在して内容が同じコマンド:"
p same
puts "runを指定して実行すると、上記の1)と3)について#{oPath}にコピーする。"

if exe=="run" then
	puts "コピー実行"
	oNotExist.each{|file|
		puts   "cp #{iPath}/#{file} #{oPath}/#{file}"
		system "cp #{iPath}/#{file} #{oPath}/#{file}"
	}
	diff.each{|file|
		puts   "cp #{iPath}/#{file} #{oPath}/#{file}"
		system "cp #{iPath}/#{file} #{oPath}/#{file}"
	}
end

