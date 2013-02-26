# GLib filename encoding guesser.
# Author: Stanislav Brabec <sbrabec@suse.cz>
# Additions are welcome.
# This script must be executed after setting LANG variable.

# Try filenames which are invalid in UTF-8 as locale specific.
# For selected locales, G_FILENAME_ENCODING takes precedence.
setenv G_BROKEN_FILENAMES 1

# In West Europe there was used both ISO-8859-15 and ISO-8859-1.
# There is no chance to recognize it, so we must guess.
#set west_europe_legacy_encoding=ISO-8859-1
set west_europe_legacy_encoding=ISO-8859-15

# In Russia, "official" encoding is ISO-8859-5, but most GNOME users
# preferred KOI8-R. We must guess.
#set russian_legacy_encoding=ISO-8859-5
set russian_legacy_encoding=KOI8-R

# In former Yugoslavia sr_YU have covered two different alphabets -
# one Latin and on Cyrillic. No chance to guess.
set sr_YU_legacy_encoding=ISO-8859-2,CP1250
#set sr_YU_legacy_encoding=ISO-8859-5

# Japanese uses two legacy encodings. Guess sometimes fails, sometimes not.
# Defining preferred encoding increases chance for success.
set japanese_legacy_encoding=EUC-JP
#set japanese_legacy_encoding=SHIFT_JIS

if (! ${?LANG} ) goto skip

switch ( $LANG )
    case aa_DJ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case af_ZA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case an_ES*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-15,CP1252
	breaksw
    case ar_AE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_BH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_DZ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_EG*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_IQ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_JO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_KW*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_LB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_LY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_MA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_OM*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_QA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_SA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_SD*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_SY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_TN*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case ar_YE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-6
	breaksw
    case be_BY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,CP1251
	breaksw
    case bg_BG*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,CP1251
	breaksw
    case br_FR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case bs_BA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case ca_ES*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case cs_CZ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case cy_GB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-14,CP1252
	breaksw
    case da_DK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case de_AT*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case de_BE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case de_DE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case de_CH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case de_LU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case el_GR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-7
	breaksw
    case en_AU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_BE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case en_BW*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_CA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_DK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_GB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case en_HK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_IE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case en_NZ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_PH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_SG*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_US*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case en_ZA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case en_ZW*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_AR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_BO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_CL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_CO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_CR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_DO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_EC*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_ES*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case es_GT*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_HN*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_MX*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_NI*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_PA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_PE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_PR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_PY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_SV*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_US*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_UY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case es_VE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case et_EE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case eu_ES*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case fa_IR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,CP1256
	breaksw
    case fi_FI*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case fo_FO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case fr_BE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case fr_CA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case fr_FR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case fr_CH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case fr_LU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case ga_IE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case gd_GB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-15,CP1252
	breaksw
    case gl_ES*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case gv_GB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case he_IL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-8
	breaksw
    case hr_HR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case hu_HU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case hy_AM*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ARMSCII-8
	breaksw
    case id_ID*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case is_IS*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case it_CH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case it_IT*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case iw_IL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-8
	breaksw
    case ja_JP*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$japanese_legacy_encoding,EUC-JP,SHIFT_JIS,ISO-8859-1
	breaksw
    case ka_GE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,GEORGIAN-PS
	breaksw
    case kl_GL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case km_KH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,GB18030
	breaksw
    case ko_KR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,EUC-KR,ISO-8859-1
	breaksw
    case kw_GB*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case lg_UG*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-10,CP1252
	breaksw
    case lt_LT*:                                           
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-13,CP1252
	breaksw
    case lv_LV*:                                           
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-13,CP1252
	breaksw
    case mi_NZ*:                                           
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-13,CP1252
	breaksw
    case mk_MK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-5,CP1251
	breaksw
    case ms_MY*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case mt_MT*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-3
	breaksw
    case nb_NO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case nl_BE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case nl_NL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case nn_NO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case no_NO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case oc_FR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case om_KE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case pl_PL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case pt_BR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case pt_PT*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case ro_RO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case ru_RU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$russian_legacy_encoding,CP1251
	breaksw
    case ru_UA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,KOI8-U
	breaksw
    case sh_YU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case sk_SK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case sl_SI*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-2,CP1250
	breaksw
    case so_DJ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case so_KE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case so_SO*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case sq_AL*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case sr_YU*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$sr_YU_legacy_encoding
	breaksw
    case st_ZA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case sv_FI*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case sv_SE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case tg_TJ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,KOI8-T
	breaksw
    case th_TH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,TIS-620,ISO-8859-1
	breaksw
    case tl_PH*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case tr_TR*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-9
	breaksw
    case uk_UA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,KOI8-U
	breaksw
    case uz_UZ*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case vi_VN*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,TCVN5712-1,ISO-8859-1
	breaksw
    case wa_BE*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,$west_europe_legacy_encoding,CP1252
	breaksw
    case xh_ZA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
    case yi_US*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,CP1255
	breaksw
    case zh_CN*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,GB2312,GB18030,GBK,ISO-8859-1
	breaksw
    case zh_HK*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,BIG5-HKSCS,ISO-8859-1
	breaksw
    case zh_SG*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,GB2312,GB18030,GBK,ISO-8859-1
	breaksw
    case zh_TW*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,BIG5,EUC-TW,ISO-8859-1
	breaksw
    case zu_ZA*:
	setenv G_FILENAME_ENCODING @locale,UTF-8,ISO-8859-1,CP1252
	breaksw
endsw

skip:

unset west_europe_legacy_encoding
unset russian_legacy_encoding
unset sr_YU_legacy_encoding
