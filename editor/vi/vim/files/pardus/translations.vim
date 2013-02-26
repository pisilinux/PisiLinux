" Vim plugin
" Purpose:      Intelligently create content for PISI's translations.xml files
" Author:       İnanç Yıldırgan
" Copyright:    Copyright (c) 2008 İnanç Yıldırgan
" Licence:      You may redistribute this under the terms of the GNU GPL v2..

if &compatible || v:version < 603
    finish
endif

fun! MakeNewTranslations()
    set nopaste

    0 put = '<?xml version=\"1.0\" ?>'
    put = '<PISI>'
    put = '    <Source>'
    put = '        <Name></Name>'
    put = '        <Summary xml:lang=\"\"></Summary>'
    put = '        <Description xml:lang=\"\"></Description>'
    put = '    </Source>'
    put = '</PISI>'
    14
endfun

com! -nargs=0 MakeNewTranslations call MakeNewTranslations()

augroup MakeNewTranslations
    au!
    autocmd BufNewFile translations.xml call MakeNewTranslations()
augroup END

" vim: set et foldmethod=marker : "
