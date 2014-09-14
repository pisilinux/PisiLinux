;;; nxml site-lisp configuration

(require 'nxml-mode)
(fset 'xml-mode 'nxml-mode)
(setq nxml-child-indent 4)
(add-hook 'nxml-mode-hook
          (lambda ()
            (setq indent-tabs-mode nil)))
(setq auto-mode-alist
      (cons '("\\.\\(xml\\|xsl\\|rng\\|xhtml\\)\\'" . nxml-mode)
            auto-mode-alist))
