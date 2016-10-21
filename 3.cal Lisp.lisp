Assignment no.:
Title:-	Implement an calculator (64 bit Binary 				Multiplication) application using concurrent
		lisp
Batch:-	
*************************************************************

(defvar a)
(defvar b)
(defvar c)
(defun :bits (value &optional (size 64))
  (format t "~v,'~b" size value))

(write-line " Enter two numbers   : ")

	(setq  a(read))
   	(setq  b(read))     

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(+ a b))
			
				(print "ADDITION in decimal: ")
				(print c ))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(- a b))
				
				(print "SUBTRACTION in decimal: ")
				(print c))))

 	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(* a b))
				(print "MULTIPLICATION IN DECIMAL: ")
				(print c))))
	
	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(* a a))
				(print "SQUARE OF 1st NUMBER  : ")
				(print c))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(* b b b))
				(print "CUBE OF 2ND NUMBER : ")
				(print c))))	

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(sin a))
				(print "SINE OF 1ST NUMBER : ")
				(print c))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(tan a))
				(print "TAN OF 1ST NUMBER : ")
				(print c))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(cos a))
				(print "COSINE OF 1ST NUMBER : ")
				(print c))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(min a b))
				(print "MINIMUM NUMBER : ")
				(print c))))

	(sb-thread:make-thread(lambda()(progn(sleep 0)
				(setf c(max a b))
				(print "MAXIMUM NUMBER : ")
				(print c))))
(exit)

*************************************************************
Output:-
comp-sl-19@compsl19-OptiPlex-3020:~$ sbcl
This is SBCL 1.1.14.debian, an implementation of ANSI Common Lisp.
More information about SBCL is available at <http://www.sbcl.org/>.

SBCL is free software, provided as is, with absolutely no warranty.
It is mostly in the public domain; some portions are provided under
BSD-style licenses.  See the CREDITS and COPYING files in the
distribution for more information.
* (load "cal.lisp")
 Enter two numbers   : 
90
45

"ADDITION in decimal: " 
135 
"SUBTRACTION in decimal: " 
45 
"MULTIPLICATION IN DECIMAL: " 
4050 
"SQUARE OF 1st NUMBER  : " 
8100 
"CUBE OF 2ND NUMBER : " 
91125 
"SINE OF 1ST NUMBER : " 
0.89399666 
"TAN OF 1ST NUMBER : " 
-1.9952004 
"COSINE OF 1ST NUMBER : " 
-0.44807363 
"MINIMUM NUMBER : " 
45  
"MAXIMUM NUMBER : " 
90
comp-sl-19@compsl19-OptiPlex-3020:~$ 