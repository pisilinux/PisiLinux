" To use this file, add this line to your ~/.vimrc:, w/o the dquote
" source /path/to/kde/sources/kdesdk/scripts/kde-devel-vim.vim
"
" For CreateChangeLogEntry() : If you don't want to re-enter your
" Name/Email in each vim session then make sure to have the viminfo
" option enabled in your ~/.vimrc, with the '!' flag, enabling persistent
" storage of global variables. Something along the line of
" set   viminfo=%,!,'50,\"100,:100,n~/.viminfo
" should do the trick.

" Don't include these in filename completions
set suffixes+=.lo,.o,.moc,.la,.closure,.loT

" Search for headers here
set path=.,/usr/include,/usr/local/include,
if $QTDIR != ''
    let &path = &path . $QTDIR . '/include/,'
endif
if $KDEDIR != ''
    let &path = &path . $KDEDIR . '/include/,'
    let &path = &path . $KDEDIR . '/include/arts/,'
endif
if $KDEDIRS != ''
    let &path = &path . substitute( $KDEDIRS, '\(:\|$\)', '/include,', 'g' )
    let &path = &path . substitute( $KDEDIRS, '\(:\|$\)', '/include/arts,', 'g' )
endif
set path+=,

" Use makeobj to build
set mp=makeobj

" If TagList is Loaded then get a funny statusline
" Only works if kde-devel-vim.vim is loaded after taglist.
" Droping this script in ~/.vim/plugin works fine
if exists('loaded_taglist')
    let Tlist_Process_File_Always=1
    set statusline=%<%f:[\ %{Tlist_Get_Tag_Prototype_By_Line()}\ ]\ %h%m%r%=%-14.(%l,%c%V%)\ %P
endif

" Insert tab character in whitespace-only lines, complete otherwise
inoremap <Tab> <C-R>=SmartTab()<CR>

if exists("EnableSmartParens")
" Insert a space after ( or [ and before ] or ) unless preceded by a matching
" paren/bracket or space or inside a string or comment. Comments are only
" recognized as such if they start on the current line :-(
inoremap ( <C-R>=SmartParens( '(' )<CR>
inoremap [ <C-R>=SmartParens( '[' )<CR>
inoremap ] <C-R>=SmartParens( ']', '[' )<CR>
inoremap ) <C-R>=SmartParens( ')', '(' )<CR>
endif

" Insert an #include statement for the current/last symbol
inoremap <F5> <C-O>:call AddHeader()<CR>

" Insert a forward declaration for the current/last symbol
" FIXME: not implemented yet
" inoremap <S-F5> <C-O>:call AddForward()<CR>

" Switch between header and implementation files on ,h
nmap <silent> ,h :call SwitchHeaderImpl()<CR>

" Comment selected lines on ,c in visual mode
vmap ,c :s,^,//X ,<CR>:noh<CR>
" Uncomment selected lines on ,u in visual mode
vmap ,u :s,^//X ,,<CR>

" Insert an include guard based on the file name on ,i
nmap ,i :call IncludeGuard()<CR>o

" Insert simple debug statements into each method
nmap ,d :call InsertMethodTracer()<CR>

" Expand #i to #include <.h> or #include ".h". The latter is chosen
" if the character typed after #i is a dquote
" If the character is > #include <> is inserted (standard C++ headers w/o .h)
iab #i <C-R>=SmartInclude()<CR>

" Insert a stripped down CVS diff
iab DIFF <Esc>:call RunDiff()<CR>

" mark 'misplaced' tab characters
set listchars=tab:·\ ,trail:·
set list

set incsearch

function! SmartTab()
    let col = col('.') - 1
    if !col || getline('.')[col-1] !~ '\k'
        return "\<Tab>"
    else
        return "\<C-P>"
    endif
endfunction

function! SmartParens( char, ... )
    if ! ( &syntax =~ '^\(c\|cpp\|java\)$' )
        return a:char
    endif
    let s = strpart( getline( '.' ), 0, col( '.' ) - 1 )
    if s =~ '//'
        return a:char
    endif
    let s = substitute( s, '/\*\([^*]\|\*\@!/\)*\*/', '', 'g' )
    let s = substitute( s, "'[^']*'", '', 'g' )
    let s = substitute( s, '"\(\\"\|[^"]\)*"', '', 'g' )
    if s =~ "\\([\"']\\|/\\*\\)"
        return a:char
    endif
    if a:0 > 0
        if strpart( getline( '.' ), col( '.' ) - 3, 2 ) == a:1 . ' '
            return "\<BS>" . a:char
        endif
        if strpart( getline( '.' ), col( '.' ) - 2, 1 ) == ' '
            return a:char
        endif
        return ' ' . a:char
    endif
    if a:char == '('
        if strpart( getline( '.' ), col( '.' ) - 3, 2 ) == 'if' ||
          \strpart( getline( '.' ), col( '.' ) - 4, 3 ) == 'for' ||
          \strpart( getline( '.' ), col( '.' ) - 6, 5 ) == 'while' ||
          \strpart( getline( '.' ), col( '.' ) - 7, 6 ) == 'switch'
            return ' ( '
        endif
    endif
    return a:char . ' '
endfunction

function! SwitchHeaderImpl()
    let headers = '\.\([hH]\|hpp\|hxx\)$'
    let impl = '\.\([cC]\|cpp\|cc\|cxx\)$'
    let fn = expand( '%' )
    if fn =~ headers
        let list = glob( substitute( fn, headers, '.*', '' ) )
    elseif fn =~ impl
        let list = glob( substitute( fn, impl, '.*', '' ) )
    endif
    while strlen( list ) > 0
        let file = substitute( list, "\n.*", '', '' )
        let list = substitute( list, "[^\n]*", '', '' )
        let list = substitute( list, "^\n", '', '' )
        if ( fn =~ headers && file =~ impl ) || ( fn =~ impl && file =~ headers )
            execute( "edit " . file )
            return
        endif
    endwhile
    echohl ErrorMsg
    echo "File switch failed!"
    echohl None
endfunction

function! IncludeGuard()
    let guard = toupper( substitute( expand( '%' ), '\([^.]*\)\.h', '\1_h', '' ) )
    call append( '^', '#define ' . guard )
    +
    call append( '^', '#ifndef ' . guard )
    call append( '$', '#endif // ' . guard )
    +
endfunction

function! SmartInclude()
    let next = nr2char( getchar( 0 ) )
    if next == '"'
        return "#include \".h\"\<Left>\<Left>\<Left>"
    endif
    if next == '>'
        return "#include <>\<Left>"
    endif
    return "#include <.h>\<Left>\<Left>\<Left>"
endfunction

function! MapIdentHeader( ident )
    " Qt stuff
    if a:ident =~ 'Q.*Layout'
        return '<qlayout.h>'
    elseif a:ident == 'QListViewItem' ||
          \a:ident == 'QCheckListItem' ||
          \a:ident == 'QListViewItemIterator'
        return '<qlistview.h>'
    elseif a:ident == 'QIconViewItem' ||
          \a:ident == 'QIconDragItem' ||
          \a:ident == 'QIconDrag'
        return '<qiconview.h>'
    elseif a:ident =~ 'Q.*Drag' ||
          \a:ident == 'QDragManager'
        return '<qdragobject.h>'
    elseif a:ident == 'QMimeSource' ||
          \a:ident == 'QMimeSourceFactory' ||
          \a:ident == 'QWindowsMime'
        return '<qmime.h>'
    elseif a:ident == 'QPtrListIterator'
        return '<qptrlist.h>'
    elseif a:ident =~ 'Q.*Event'
        return '<qevent.h>'
    elseif a:ident == 'QTime' ||
          \a:ident == 'QDate'
        return '<qdatetime.h>'
    elseif a:ident == 'QTimeEdit' ||
          \a:ident == 'QDateTimeEditBase' ||
          \a:ident == 'QDateEdit'
        return '<qdatetimeedit.h>'
    elseif a:ident == 'QByteArray'
        return '<qcstring.h>'
    elseif a:ident == 'QWidgetListIt'
        return '<qwidgetlist.h>'
    elseif a:ident == 'QTab'
        return '<qtabbar.h>'
    elseif a:ident == 'QColorGroup'
        return '<qpalette.h>'
    elseif a:ident == 'QActionGroup'
        return '<qaction.h>'
    elseif a:ident =~ 'Q.*Validator'
        return '<qvalidator.h>'
    elseif a:ident =~ 'QListBox.*'
        return '<qlistbox.h>'
    elseif a:ident == 'QChar' ||
          \a:ident == 'QCharRef' ||
          \a:ident == 'QConstString'
        return '<qstring.h>'
    elseif a:ident =~ 'QCanvas.*'
        return '<qcanvas.h>'
    elseif a:ident =~ 'QGL.*'
        return '<qgl.h>'
    elseif a:ident == 'QTableSelection' ||
          \a:ident == 'QTableItem' ||
          \a:ident == 'QComboTableItem' ||
          \a:ident == 'QCheckTableItem'
        return '<qtable.h>'
    elseif a:ident == 'qApp'
        return '<qapplication.h>'

    " KDE stuff
    elseif a:ident == 'K\(Double\|Int\)\(NumInput\|SpinBox\)'
        return '<knuminput.h>'
    elseif a:ident == 'KConfigGroup'
        return '<kconfigbase.h>'
    elseif a:ident == 'KListViewItem'
        return '<klistview.h>'
    elseif a:ident =~ 'kd\(Debug\|Warning\|Error\|Fatal\|Backtrace\)'
        return '<kdebug.h>'
    elseif a:ident == 'kapp'
        return '<kapplication.h>'
    elseif a:ident == 'i18n' ||
          \a:ident == 'I18N_NOOP'
        return '<klocale.h>'
    elseif a:ident == 'locate' ||
          \a:ident == 'locateLocal'
        return '<kstandarddirs.h>'

    " aRts stuff
    elseif a:ident =~ '\arts_\(debug\|info\|warning\|fatal\)'
        return '<debug.h>'

    " Standard Library stuff
    elseif a:ident =~ '\(std::\)\?\(cout\|cerr\|endl\)'
        return '<iostream>'
    elseif a:ident =~ '\(std::\)\?is\(alnum\|alpha\|ascii\|blank\|graph\|lower\|print\|punct\|space\|upper\|xdigit\)'
        return '<cctype>'
    endif

    let header = tolower( substitute( a:ident, '::', '/', 'g' ) ) . '.h'
    let check = header
    while 1 
        if filereadable( check )
            return '"' . check . '"'
        endif
        let slash = match( check, '/' )
        if slash == -1
            return '<' . header . '>'
        endif
        let check = strpart( check, slash + 1 )
    endwhile
endfunction

" This is a rather dirty hack, but seems to work somehow :-) (malte)
function! AddHeader()
    let s = getline( '.' )
    let i = col( '.' ) - 1
    while i > 0 && strpart( s, i, 1 ) !~ '[A-Za-z0-9_:]'
        let i = i - 1
    endwhile
    while i > 0 && strpart( s, i, 1 ) =~ '[A-Za-z0-9_:]'
        let i = i - 1
    endwhile
    let start = match( s, '[A-Za-z0-9_]\+\(::[A-Za-z0-9_]\+\)*', i )
    let end = matchend( s, '[A-Za-z0-9_]\+\(::[A-Za-z0-9_]\+\)*', i )
    if end > col( '.' )
        let end = matchend( s, '[A-Za-z0-9_]\+', i )
    endif
    let ident = strpart( s, start, end - start )
    let include = '#include ' . MapIdentHeader( ident )

    let line = 1
    let incomment = 0
    let appendpos = 0
    let codestart = 0
    while line <= line( '$' )
        let s = getline( line )
        if incomment == 1
            let end = matchend( s, '\*/' )
            if end == -1
                let line = line + 1
                continue
            else
                let s = strpart( s, end )
                let incomment = 0
            endif
        endif
        let s = substitute( s, '//.*', '', '' )
        let s = substitute( s, '/\*\([^*]\|\*\@!/\)*\*/', '', 'g' )
        if s =~ '/\*'
            let incomment = 1
        elseif s =~ '^' . include
            break
        elseif s =~ '^#include' && s !~ '\.moc"'
            let appendpos = line
        elseif codestart == 0 && s !~ '^$'
            let codestart = line
        endif
        let line = line + 1
    endwhile
    if line == line( '$' ) + 1
        if appendpos == 0
            call append( codestart - 1, include )
            call append( codestart, '' )
        else
            call append( appendpos, include )
        endif
    endif
endfunction

function! RunDiff()
    echo 'Diffing....'
    read! cvs diff -bB -I \\\#include | egrep -v '(^Index:|^=+$|^RCS file:|^retrieving revision|^diff -u|^[+-]{3})'
endfunction

function! CreateChangeLogEntry()
    let currentBuffer = expand( "%" )

    if exists( "g:EMAIL" )
        let mail = g:EMAIL
    elseif exists( "$EMAIL" )
        let mail = $EMAIL
    else
        let mail = inputdialog( "Enter Name/Email for Changelog entry: " ) 
    if mail == ""
        echo "Aborted ChangeLog edit..."
        return
    endif
    let g:EMAIL = mail
    endif

    if bufname( "ChangeLog" ) != "" && bufwinnr( bufname( "ChangeLog" ) ) != -1
    execute bufwinnr( bufname( "ChangeLog" ) ) . " wincmd w"
    else
        execute "split ChangeLog"
    endif

    let lastEntry = getline( nextnonblank( 1 ) )
    let newEntry = strftime("%Y-%m-%d") . "  " . mail

    if lastEntry != newEntry 
        call append( 0, "" )
        call append( 0, "" )
        call append( 0, newEntry )
    endif

    " like emacs, prepend the current buffer name to the entry. but unlike
    " emacs I have no idea how to figure out the current function name :(
    " (Simon)
    if currentBuffer != ""
        let newLine = "\t* " . currentBuffer . ": "
    else
        let newLine = "\t* "
    endif

    call append( 2, newLine )

    execute "normal 3G$"
endfunction

function! AddQtSyntax()
    if expand( "<amatch>" ) == "cpp"
        syn keyword qtKeywords     signals slots emit foreach
        syn keyword qtMacros       Q_OBJECT Q_WIDGET Q_PROPERTY Q_ENUMS Q_OVERRIDE Q_CLASSINFO Q_SETS SIGNAL SLOT
        syn keyword qtCast         qt_cast qobject_cast qvariant_cast qstyleoption_cast
        syn keyword qtTypedef      uchar uint ushort ulong Q_INT8 Q_UINT8 Q_INT16 Q_UINT16 Q_INT32 Q_UINT32 Q_LONG Q_ULONG Q_INT64 Q_UINT64 Q_LLONG Q_ULLONG pchar puchar pcchar qint8 quint8 qint16 quint16 qint32 quint32 qint64 quint64 qlonglong qulonglong
        syn keyword kdeKeywords    k_dcop k_dcop_signals
        syn keyword kdeMacros      K_DCOP ASYNC
        syn keyword cRepeat        foreach
        syn keyword cRepeat        forever

        hi def link qtKeywords          Statement
        hi def link qtMacros            Type
        hi def link qtCast              Statement
        hi def link qtTypedef           Type
        hi def link kdeKeywords         Statement
        hi def link kdeMacros           Type
    endif
endfunction

function! InsertMethodTracer()
    :normal [[kf(yBjokdDebug() << ""()" << endl;
endfunction

function! UpdateMocFiles()
    if &syntax == "cpp"
        let i = 1
        while i < 80
            let s = getline( i )
            if s =~ '^#include ".*\.moc"'
                let s = substitute( s, '.*"\(.*\)\.moc"', '\1.h', '' )
                if stridx( &complete, s ) == -1
                    let &complete = &complete . ',k' . s
                endif
                break
            endif
            let i = i + 1
        endwhile
    endif
endfunction

autocmd Syntax * call AddQtSyntax()
autocmd CursorHold * call UpdateMocFiles()

" vim: sw=4 sts=4 et
