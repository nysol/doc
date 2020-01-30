
require "zdd"
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=2*a+2*b+4*a*c

f.each_item{|weight,item,top,bottom|
puts "#{weight} #{item} #{top} #{bottom}"
}
