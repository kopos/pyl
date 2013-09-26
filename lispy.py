# Based on
# http://norvig.com/lispy.html
# http://norvig.com/lispy2.html
#
# http://julien.danjou.info/blog/2013/lisp-python-hy
#
# if (x.val() > 0) {
#   z = f(a * x.val() + b[i]);
# }
#
# (if (> (val x) 0)
#   (let z
#       (f (+ (* a (val x))
#             (aref b i)))))
#
#
# (if (> (val x) 0)
#   (let z
#       (f (+ (* a (val x))
#             (__getitem__ b i)))))
#
