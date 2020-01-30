#!/usr/bin/env ruby
#-*- coding: utf-8 -*-

# 必要なソフトウェア:pandoc
# http://johnmacfarlane.net/pandoc/installing.html
# 上記からmac用のdmgをダウンロードしてインストールする。

require 'rubygems'
require 'nysol/mcmd'

# 引数チェック
if ARGV.size != 1 then
	STDERR.puts "mcmd/enのtexマニュアルをヘルプ用textに変換する"
	STDERR.puts "#{$0} 出力dir名"
	STDERR.puts "#{$0} xxhelp"
	exit
end

iPath="../../mcmd/en"
oPath=ARGV[0]
oPath=File.expand_path(oPath)

tmp="mcal"

def evalUse(line)
	use=nil
	if line=~/^\\subsection/
                if line=~/Format/ or line=~/Parameters/ or line=~/Examples/  or line=~/Using regular expressions/ then
			use=true
		else
			use=false
		end
	# 概要説明で表を交えて詳しく説明しているようなパラグラフの前に挿入されている。
	elsif line=~/if0 #no help#/ then 
		use=false
	end
	return use
end

$header=<<'EOF'
/* ////////// LICENSE INFO ////////////////////

 * Copyright (C) 2013 by NYSOL CORPORATION
 *
 * Unless you have received this program directly from NYSOL pursuant
 * to the terms of a commercial license agreement with NYSOL, then
 * this program is licensed to you under the terms of the GNU Affero General
 * Public License (AGPL) as published by the Free Software Foundation,
 * either version 3 of the License, or (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING THOSE OF 
 * NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.
 *
 * Please refer to the AGPL (http://www.gnu.org/licenses/agpl-3.0.txt)
 * for more details.

 ////////// LICENSE INFO ////////////////////*/
// =============================================================================
/// kg##name##Help.h : kg##name## help
// =============================================================================
_title="##title##";
_doc="\
##document##";

EOF

# ディレクトリ作成
puts "rm -rf ./xxsrc"
system "rm -rf ./xxsrc"
puts "mkdir -p ./xxsrc/examples/tex"
system "mkdir -p ./xxsrc/examples/tex"

# ------------------------
# プレクリーニング実行
#  tex => #{tmpTex}

# ターゲットのtexをクリーニング
puts "## cleaning all tex files under #{iPath} ..."

# texのクリーニング実行(xxsrcに出力)
files=[]
#Dir["#{iPath}/#{tmp}.tex"]             .each{|f| files << f}
#Dir["#{iPath}/examples/tex/#{tmp}_ex.tex"].each{|f| files << f}
Dir["#{iPath}/m*.tex"]             .each{|f| files << f}
Dir["#{iPath}/examples/tex/m*.tex"].each{|f| files << f}
files.each{|iFile|
	name=iFile.sub("#{iPath}/","")
	oFile="./xxsrc/#{name}"
	next if name=="mcmd2.tex"

	File.open(iFile,"r"){|fpr|
		File.open(oFile,"w"){|fpw|
			use=true
			while line=fpr.gets
				next if line =~ /^%/
				# mcalは特別扱い
				if name=="mcal.tex" then
					if line=~/^\\section/ then
#						if line=~/label{sect:mcal}/ or line=~/定数/ or line=~/項目値/ or line=~/前行の項目値/ or line=~/前行の結果項目値/ or\
#						   line=~/算術演算子/ or line=~/比較演算子/ or line=~/論理演算子/ or line=~/関数/ then

						if line=~/label{sect:mcal}/ or line=~/Constant/ or line=~/Field value/ or line=~/Value from Previous Row/ or line=~/Values from Next Row/ or\
						   line=~/Arithmetic Operators/ or line=~/Comparison Operators/ or line=~/Logical Operator/ or line=~/Function/ then
							use=true
						else
							use=false
						end
					else
						u=evalUse(line)
						use=u if u!=nil
					end
				else
					u=evalUse(line)
					use=u if u!=nil
				end
				next if not use

				# 番号なしセクションには対応していないので*を削除
				line.sub!("subsection*","subsection")
				line.sub!("subsection*","subsection")
				# labelは出力されるので削除する。
				line.sub!(/\\label{.+?}/,"")
				# hyperrefには対応していないので{}の箇所のみ出力。
				while line.index('\\hyperref')
					line=~/\\hyperref\[(.+?)\] ?{(.+?)}/
					line.sub!(/\\hyperref\[.+?\] ?{.+?}/,$2)
				end
				# refには対応していないので削除。
				line.gsub!(/\\ref{.+?}/,"")

				line=~/\\begin{minipage}{(.+?)}/
				line.sub!("begin{minipage}{#{$1}}","begin{minipage}")

				# tableの位置指定を消す
				line=~/begin{table}\[(.+?)\]/
				line.sub!("begin{table}[#{$1}]","begin{table}")

				# hrefはURLを表示させる。
				while line.index('\\href')
					line=~/\\href\{(.+?)\}{(.+?)}/
					line.sub!(/\\href\{.+?\}{.+?}/,$1)
				end

				# 数学記号は変換できないので
				line.gsub!("\\pi","π")
				line.gsub!("\\infty","∞")
				line.gsub!("\\sim","~")
				line.gsub!("\\le","<=")
				line.gsub!("\\cdots","…")
				line.gsub!("\\times","×")
				line.gsub!("\\min","min")
				line.gsub!("\\max","max")
				line.gsub!("\\rightarrow","→")

				fpw.puts line.chomp
			end
		}
	}
}

#### PANDOC実行 *tex => *.txt
files=[]
#Dir["xxsrc/#{tmp}.tex"].each{|iFile|
Dir["xxsrc/*.tex"].each{|iFile|
	name=iFile.sub("xxsrc/","").sub(".tex","")
	puts "(cd xxsrc ; pandoc -f latex -t plain #{name}.tex -o #{name}.h)"
	system "(cd xxsrc ; pandoc -f latex -t plain #{name}.tex -o #{name}.h)"
}

# 事後クリーニング&出力
system "mkdir #{oPath}"
files=[]
#Dir["xxsrc/#{tmp}.h"].each{|iFile|
Dir["xxsrc/*.h"].each{|iFile|
	name=iFile.sub("xxsrc/","").sub(".h","")[1,100] # 頭文字mを削る
	oFile="#{oPath}/kg#{name}Help.h"

	# 1行目のタイトルを読み込む
	title=nil
	File.open(iFile,"r"){|fpr|
		line=fpr.gets()
		title=line.split(" ")[1]
              loop{
                line=fpr.gets()
		break if line == nil
                next if line.chomp==""
                title=line.split(" ")[1]
                break
               }


	}
	puts "post cleaning m#{name}: #{title}"

	# .hデータを読み込み
	doc=nil
	File.open(iFile,"r"){|fpr|
		doc=fpr.read()
	}

	### クリーニング本体
	doc.gsub!(/^  -+ -+$/,"") # パラメータ欄の罫線削除
	doc.gsub!(/^c+$/,"") # minipageを列挙した表のcccが残るので削除

	# 見た目の2行以上の空白削除
	doc.gsub!(/^\s+$/,"") # 空白のみの行削除
	while doc.index("\n\n\n") # 3連続改行がなくなるまで
		doc.gsub!("\n\n\n","\n\n")
	end

	# sectionやsubsection下の空行は削除
	doc.gsub!("==\n\n","==\n")
	doc.gsub!("--\n\n","--\n")

	# versionの表示位置がおかしいので
	doc.gsub!("\n[--version]","[--version]")

	# mcalの節へのリンク項目を削除しているので表題も削除
	if name=="cal" then
		doc.gsub!(" 節 ","    ")
	end

	# C++の文字列なので、'\'をエスケープする
	doc.gsub!('\\%','%')
	doc.gsub!('\\','\\\\\\\\\\\\\\\\')

	# C++の文字列なので、"をエスケープする
	doc.gsub!('"','\"')
	# C++の文字列なので、行末に"\n\"を付ける
	doc.gsub!("\n","\\n\\\n")

	header=$header.dup
	header.gsub!("##name##",name)
	header.sub!("##title##",title)
	header.sub!("##document##",doc)

	File.open(oFile,"w"){|fpw|
		fpw.write(header)
	}
}

