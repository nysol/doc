#!/usr/bin/env ruby
#-*- coding: utf-8 -*-

# 必要なソフトウェア:pandoc
# http://johnmacfarlane.net/pandoc/installing.html
# 上記からmac用のdmgをダウンロードしてインストールする。

require 'rubygems'
require 'mcmd'

# 引数チェック
if ARGV.size != 1 then
	STDERR.puts "xxx/jpのhtmlマニュアルを「さくら」にuploadする"
	STDERR.puts "#{$0} マニュアルdir名 upload先(www直下のディレクトリ名)"
	STDERR.puts "#{$0} xxzdd zdd"
	exit
end

system "rm -rf jp"
system "cp -R #{ARGV[0]} jp"
system "scp -r jp nysol@nysol.sakura.ne.jp:~/www/#{ARGV[1]}"

