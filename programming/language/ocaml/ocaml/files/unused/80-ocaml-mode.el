;;; ocaml.mode

(require 'caml-font)
(autoload 'caml-mode "caml" "Caml editing mode" t)
(add-to-list 'auto-mode-alist '("\\.mli?$" . caml-mode))
