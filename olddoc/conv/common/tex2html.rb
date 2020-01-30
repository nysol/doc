#!/usr/bin/env ruby
#-*- coding: utf-8 -*-

class TEX2HTML

	attr_reader :iPath
	attr_reader :oPath
	attr_reader :tex
	attr_reader :sty

	def help
		STDERR.puts "tex2html.rb"
		STDERR.puts "convert LATEX documents to HTML documents using plastex"
		STDERR.puts "usage) #{$0} mcmd|zdd|mruby jp|en"
		exit
	end

	def initialize(name,lang)
		help unless name
		help unless lang
		help unless ["mcmd","zdd"].index(name)
		help unless ["jp","en"].index(lang)

		@name=name
		@lang=lang
		@iPath="../../#{@name}/#{@lang}"
		@oPath=File.expand_path("./xx#{@name}")
		@tex="#{@name}.tex"
		@sty="#{@name}.sty"
		@wp="./xxsrc"
	end

	# ------------------------
	# copying all files under #{iPath} to `#{@wp}'
	def copyAllFiles()
		puts "## copying all files from #{@iPath} to #{@wp} ..."
		system "rm -rf #{@wp}"
		system "mkdir #{@wp}"
		system "cp -R #{iPath}/* #{@wp}"
	end

	# ------------------------
	def cleanStyle()
		puts "## cleaning style file `#{@wp}/#{@sty}' ..."

		# cleaning style file
		# 1) delete all functions about paper setting
		iFile="#{@wp}/#{@sty}"
		oFile="#{@wp}/#{@sty}"
		File.open(iFile,"r"){|fpr|
			File.open("xxsty","w"){|fpw|
				while line=fpr.gets
					next if line.index("setlength")
					next if line.index("addtolength")
					fpw.puts line.chomp
				end
			}
		}
		system "cp xxsty #{oFile}"
	end

	# ------------------------
	def cleanTex()
		puts "## cleaning all tex files maching #{@wp}/*.tex and #{@wp}/examples/tex/*.tex ..."
		# 2) cleaning tex files
		files=[]
		Dir["#{@wp}/*.tex"]             .each{|f| files << f}
		Dir["#{@wp}/examples/tex/*.tex"].each{|f| files << f}
		files.each{|iFile|
			next if File.basename(iFile)=="#{@name}.tex" # skip main tex file (see cleanMain)
			oFile=iFile
			File.open(iFile,"r"){|fpr|
				File.open("xxtex","w"){|fpw|
					while line=fpr.gets
						# Verbatim => verbatim
						if line.index('begin{Verbatim}')
							fpw.puts '\begin{verbatim}'
							next
						end
						if line.index('end{Verbatim}')
							fpw.puts '\end{verbatim}'
							next
						end

						# hyperref[] => hyperlink{}
						while line.index('\\hyperref')
							line=~/\\hyperref\[(.+?)\]/
							line.sub!("[#{$1}]","{#{$1}}")
							line.sub!("\\hyperref","\\hyperlink")
						end

						line=line.chomp
						line=extendTex(line)

						fpw.puts line
					end
				}
				system "cp xxtex #{oFile}"
			}
		}
	end

	# #{mcmd.texは特別に最初からクリーニング実行
	# 1) jsbook => book
	# ------------------------
	def cleanMain()
		puts "## cleaning main file `#{@wp}/#{@name}.tex' ..."
		iFile="#{@iPath}/#{@name}.tex"
		oFile=iFile
		doc=nil
		File.open(iFile,"r"){|fpr|
			doc=fpr.read
			doc.gsub!("jsbook","book")
		}
		File.open(oFile,"w"){|fpw|
			fpw.write(doc)
		}
	end

	# ------------------------
	# HTMLへの変換 plastexの実行
	# #{tmpTex} => #{oPath}/*
	# oPath, tmpTexともに絶対パス指定になっている。
	#   => plastex実行時に\include{xxx.tex}が相対パス指定となっているため。
	# --titleはnavigationバーの真ん中に表示される文字列
	# --split-levelを指定しなければ節毎に分割されたhtml文書が生成される
	# --base-urlは右上のtable of contentsのnavigation link
	def runPlastex()
		puts "## converting tex(#{@wp}) to html(#{@oPath}) using plastex ... #{}"
		system "mkdir #{@oPath}"
		system "(cd #{@wp} ; plastex -d #{@oPath} --title=#{@name.upcase} --split-level=1 #{@tex})"
	end

	# ------------------------
	# post cleaning of html files
	# embed the java script for google analytics
	def cleanHtml()
		puts "## cleaning html files `#{@wp}/#{@name}.html' ..."
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

		Dir["#{@oPath}/*.html"].each{|htmlFile|
			puts "converting #{htmlFile}"
			doc=nil
			File.open(htmlFile,"r"){|fpr|
				doc=fpr.read()
			}
			doc.sub!("</head>","#{googleAna}\n</head>")
			doc=extendHtml(doc)
			# doc.gsub!("x8x","   ")
			File.open(htmlFile,"w"){|fpw|
				fpw.write(doc)
			}
		}
	end

end

