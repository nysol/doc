#!/usr/bin/env ruby
# coding: utf-8
require "./mkTex.rb"

############## Example 1
title="Basic Example"
comment=<<'EOF'
In the following, using items \verb|a,b,c|, find out the exclusive OR on itemsets
\verb|2ab + a + 3b|, \verb|abc + 2ab + bc + 1|, \verb|ab+a|.
EOF
scp=<<'EOF'
require 'zdd'
# First, define the itemsets
a=ZDD::itemset("a")
b=ZDD::itemset("b")
c=ZDD::itemset("c")
f=2*a*b+a+3*b
f.show
#VERB_END#

## \verb|(2ab + a + 3b)|$\oplus$\verb|a| = \verb|3ab + 2b + 1|
#VERB_BEGIN#
f.delta(a).show
#VERB_END#

## \verb|(2ab + a + 3b)|$\oplus$\verb|b| = \verb|ab + 2a + 3|
#VERB_BEGIN#
f.delta(b).show
#VERB_END#

## \verb|(2ab + a + 3b)|$\oplus$\verb|ab| = \verb|3a + b + 2|
#VERB_BEGIN#
f.delta(a*b).show
#VERB_END#

## \verb|(2ab + a + 3b)|$\oplus$\verb|1| = \verb|2ab+a+3b|
## Since constant 1 is an empty itemset, it is remained in the original set for solving XOR operation.
#VERB_BEGIN#
f.delta(1).show
#VERB_END#

## The operation result of the each term in \verb|(abc + 2ab + bc + 1)|$\oplus$\verb|(2ab + a)|
## are as follows:
## \begin{itemize}
## \item \verb|abc |$\oplus$\verb| 2ab = 2c|
## \item \verb|2ab |$\oplus$\verb| 2ab = 4|
## \item \verb|bc  |$\oplus$\verb| 2ab = 2ac|
## \item \verb|1   |$\oplus$\verb| 2ab = 2ab|
## \item \verb|abc |$\oplus$\verb| a   = bc|
## \item \verb|2ab |$\oplus$\verb| a   = 2b|
## \item \verb|bc  |$\oplus$\verb| a   = abc|
## \item \verb|1   |$\oplus$\verb| a   = a|
## \end{itemize}
## 
## The result is summarized as \verb|a b c + 2 a b + 2 a c + a + b c + 2 b + 2 c + 4|.
#VERB_BEGIN#
g=((a*b*c)+2*(a*b)+(b*c)+1)
h=2*a*b + a
g.show
h.show
g.delta(h).show
EOF
run(scp,title,comment)

