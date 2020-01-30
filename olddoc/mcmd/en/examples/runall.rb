#!/usr/bin/env ruby
# coding: utf-8

Dir["*.rb"].each{|file|
	next if file=="runall.rb"
	system "./#{file}"
}
