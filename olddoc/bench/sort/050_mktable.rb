#!/usr/bin/env ruby
#coding:utf-8
require "mcmd"

f=""
f << "mcat   i=log/bench1_avg.csv,log/bench2_avg.csv |"
f << "msortf f=cmdOrder,dsOrder |"
f << "mcross k=command s=data_set f=real |"
f << "msortf f=command |"
f << "mjoin  k=command m=xxcmdOrder f=cmdOrder,strnum,text |"
f << "msortf f=cmdOrder o=xxham"
system(f)
# command,fld,100_10,100_100,100_1000,100_10000,100_2,100_rand,100_rand_asc,100_rand_dec,cmdOrder,strnum,text
# msortf,real,1.671,1.243,1.402,1.222,1.377,1.359,0.995,1.025,1,1,msortf k=key
# xtsort,real,1.235,1.256,1.33,1.223,1.41,1.194,1.318,1.186,2,1,xtsort -k key\%n
# sortk1,real,25.726,24.839,24.156,23.501,26.545,21.39,10.937,11.326,3,1,sort -k1
# msortf_n,real,1.725,1.867,1.967,2.107,1.412,2.876,1.744,1.247,4,2,xtsort -k key
# xtsort_n,real,2.877,4.138,3.528,3.423,2.715,5.339,2.064,1.927,5,2,sort -k1 -n
# sortk1_n,real,22.369,17.6,13.064,8.732,25.508,1.685,0.598,0.682,6,2,msortf k=key\%n
File.open("figure/comp.tex","w"){|fpw|
	fpw.puts "\\begin{table}[hbt]"
	fpw.puts "\\begin{center}"
	fpw.puts "\\caption{キー項目の値の種類数および状態に関する比較}"
	fpw.puts "\\begin{tabular}{clrrrrrrrr}"
	fpw.puts "\\hline"
	fpw.puts "No. & コマンド & 2種 & 10種 & 100種 & 1000種 & 10000種 & 乱数 & 乱数昇順 & 乱数降順 \\\\"
	MCMD::Mcsvin.new("i=xxham k=strnum"){|csv|
		no=1
		csv.each{|flds,top,bot|
print "#{flds['text']}\n"
			fpw.puts "\\hline" if top
			fpw.print "(#{no})&"
			fpw.print "#{flds['text']}&#{sprintf("%.2f",flds['100_2'].to_f)}&#{sprintf("%.2f",flds['100_10'].to_f)}&#{sprintf("%.2f",flds['100_100'].to_f)}&#{sprintf("%.2f",flds['100_1000'].to_f)}&#{sprintf("%.2f",flds['100_10000'].to_f)}&#{sprintf("%.2f",flds['100_rand'].to_f)}&#{sprintf("%.2f",flds['100_rand_asc'].to_f)}&#{sprintf("%.2f",flds['100_rand_dec'].to_f)}"
			fpw.puts " \\\\"
			no+=1
		}
	}
	fpw.puts "\\hline"
	fpw.puts "\\end{tabular}"
	fpw.puts "\\end{center}"
	fpw.puts "\\end{table}"
}
