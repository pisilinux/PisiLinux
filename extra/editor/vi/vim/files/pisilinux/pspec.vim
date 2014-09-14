if &compatible || v:version < 603
    finish
endif

fun! MakeNewPSPEC()
    set nopaste

    0 put = '<?xml version=\"1.0\" ?>'
    put = '<!DOCTYPE PISI SYSTEM \"http://www.pisilinux.org/projeler/pisi/pisi-spec.dtd\">'
    put = '<PISI>'
    put = '    <Source>'
    put = '        <Name></Name>'
    put = '        <Homepage>http://</Homepage>'
    put = '        <Packager>'
    put = '            <Name></Name>'
    put = '            <Email></Email>'
    put = '        </Packager>'
    put = '        <License>GPLv2</License>'
    put = '        <Icon></Icon>'
    put = '        <IsA></IsA>'
    put = '        <Summary></Summary>'
    put = '        <Description></Description>'
    put = '        <Archive sha1sum=\"\" type=\"\">http://</Archive>'
    put = '        <BuildDependencies>'
    put = '            <Dependency></Dependency>'
    put = '        </BuildDependencies>'
    put = '        <Patches>'
    put = '            <Patch level=\"\"></Patch>'
    put = '        </Patches>'
    put = '    </Source>'
    put = ''
    put = '    <Package>'
    put = '        <Name></Name>'
    put = '        <RuntimeDependencies>'
    put = '            <Dependency versionFrom=\"\"></Dependency>'
    put = '        </RuntimeDependencies>'
    put = '        <Files>'
    put = '            <Path fileType=\"config\">/etc</Path>'
    put = '            <Path fileType=\"executable\">/usr/bin</Path>'
    put = '            <Path fileType=\"header\">/usr/include</Path>'
    put = '            <Path fileType=\"library\">/usr/lib</Path>'
    put = '            <Path fileType=\"localedata\">/usr/share/locale</Path>'
    put = '            <Path fileType=\"man\">/usr/share/man</Path>'
    put = '            <Path fileType=\"doc\">/usr/share/doc</Path>'
    put = '            <Path fileType=\"data\">/usr/share</Path>'
    put = '        </Files>'
    put = '        <AdditionalFiles>'
    put = '            <AdditionalFile owner=\"root\" permission=\"0644\" target=\"\"></AdditionalFile>'
    put = '        </AdditionalFiles>'
    put = '        <Provides>'
    put = '            <COMAR script=\"\"></COMAR>'
    put = '        </Provides>'
    put = '    </Package>'
    put = ''
    put = '    <History>'
    put = '        <Update release=\"1\">'
    put = '            <Date>YYYY-MM-DD</Date>'
    put = '            <Version></Version>'
    put = '            <Comment>First release.</Comment>'
    put = '            <Name></Name>'
    put = '            <Email></Email>'
    put = '        </Update>'
    put = '    </History>'
    put = '</PISI>'
    14
endfun

com! -nargs=0 NewPSPEC call MakeNewPSPEC()

augroup NewPSPEC
    au!
    autocmd BufNewFile pspec.xml call MakeNewPSPEC()
augroup END

" vim: set et foldmethod=marker : "
