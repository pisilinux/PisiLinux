"
" Just a little plugin to automatically set utf-8 for new Python files
"

if &compatible || v:version < 603
    finish
endif

fun! MakeNewPythonFile()
    " actions.py has another handler
    if expand("<afile>") == 'actions.py'
        return
    endif
    set nopaste
    0 put = '#!/usr/bin/python'
    put = '# -*- coding: utf-8 -*-'
    put = ''
    5
endfun

com! -nargs=0 NewPythonFile call MakeNewPythonFile()

augroup NewPythonFile
    au!
    autocmd BufNewFile *.py call MakeNewPythonFile()
augroup END

" vim: set et foldmethod=marker : "
