;;; python-mode site-lisp configuration
(add-to-list 'load-path "/usr/share/emacs/site-lisp/python/")

(autoload 'python-mode "python-mode" "Python editing mode." t)
(autoload 'jython-mode "python-mode" "Python editing mode." t)
(autoload 'py-shell "python-mode" "Start an interactive Python interpreter in another window." t)
(autoload 'doctest-mode "doctest-mode" "Editing mode for Python Doctest examples." t)
(autoload 'py-complete "pycomplete" "Complete a symbol at point using Pymacs." t)

(add-to-list 'auto-mode-alist '("\\.py$" . python-mode))
(add-to-list 'auto-mode-alist '("\\.doctest$" . doctest-mode))

(add-to-list 'interpreter-mode-alist '("python" . python-mode))
(add-to-list 'interpreter-mode-alist '("jython" . jython-mode))

;; Add menu
(require 'easymenu)
(easy-menu-add-item nil '("tools") ["PYTHON" python-mode t])
