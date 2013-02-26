# GLib filename encoding guesser.
# Author: Stanislav Brabec <sbrabec@suse.cz>
# Additions are welcome.
# This script must be executed after setting LANG variable.

# Try filenames which are invalid in UTF-8 as locale specific.
# For selected locales, G_FILENAME_ENCODING takes precedence.
export G_BROKEN_FILENAMES=1

# In West Europe there was used both ISO-8859-15 and ISO-8859-1.
# There is no chance to recognize it, so we must guess.
#west_europe_legacy_encoding=ISO-8859-1
west_europe_legacy_encoding=ISO-8859-15

# In Russia, "official" encoding is ISO-8859-5, but most GNOME users
# preferred KOI8-R. We must guess.
#russian_legacy_encoding=ISO-8859-5
russian_legacy_encoding=KOI8-R

# In former Yugoslavia sr_YU have covered two different alphabets -
# one Latin and on Cyrillic. No chance to guess.
sr_YU_legacy_encoding=ISO-8859-2,CP1250
#sr_YU_legacy_encoding=ISO-8859-5

# Japanese uses two legacy encodings. Guess sometimes fails, sometimes not.
# Defining preferred encoding increases chance for success.
japanese_legacy_encoding=EUC-JP
#japanese_legacy_encoding=SHIFT_JIS

case $LANG in
    aa_DJ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    af_ZA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    an_ES* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-15,CP1252
	;;
    ar_AE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_BH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_DZ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_EG* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_IQ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_JO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_KW* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_LB* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_LY* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_MA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_OM* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_QA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_SA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_SD* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_SY* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_TN* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    ar_YE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-6
	;;
    be_BY* )
	G_FILENAME_ENCODING=@locale,UTF-8,CP1251
	;;
    bg_BG* )
	G_FILENAME_ENCODING=@locale,UTF-8,CP1251
	;;
    br_FR* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    bs_BA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    ca_ES* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    cs_CZ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    cy_GB* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-14,CP1252
	;;
    da_DK* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    de_AT* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    de_BE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    de_DE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    de_CH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    de_LU* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    el_GR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-7
	;;
    en_AU* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_BE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    en_BW* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_CA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_DK* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_GB* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    en_HK* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_IE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    en_NZ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_PH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_SG* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_US* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    en_ZA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    en_ZW* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_AR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_BO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_CL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_CO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_CR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_DO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_EC* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_ES* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    es_GT* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_HN* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_MX* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_NI* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_PA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_PE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_PR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_PY* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_SV* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_US* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_UY* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    es_VE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    et_EE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    eu_ES* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    fa_IR* )
	G_FILENAME_ENCODING=@locale,UTF-8,CP1256
	;;
    fi_FI* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    fo_FO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    fr_BE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    fr_CA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    fr_FR* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    fr_CH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    fr_LU* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    ga_IE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    gd_GB* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-15,CP1252
	;;
    gl_ES* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    gv_GB* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    he_IL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-8
	;;
    hr_HR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    hu_HU* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    hy_AM* )
	G_FILENAME_ENCODING=@locale,UTF-8,ARMSCII-8
	;;
    id_ID* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    is_IS* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    it_CH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    it_IT* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    iw_IL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-8
	;;
    ja_JP* )
	G_FILENAME_ENCODING=@locale,UTF-8,$japanese_legacy_encoding,EUC-JP,SHIFT_JIS,ISO-8859-1
	;;
    ka_GE* )
	G_FILENAME_ENCODING=@locale,UTF-8,GEORGIAN-PS
	;;
    kl_GL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    km_KH* )
	G_FILENAME_ENCODING=@locale,UTF-8,GB18030
	;;
    ko_KR* )
	G_FILENAME_ENCODING=@locale,UTF-8,EUC-KR,ISO-8859-1
	;;
    kw_GB* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    lg_UG* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-10,CP1252
	;;                                          
    lt_LT* )                                        
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-13,CP1252
	;;                                          
    lv_LV* )                                        
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-13,CP1252
	;;                                          
    mi_NZ* )                                        
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-13,CP1252
	;;
    mk_MK* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-5,CP1251
	;;
    ms_MY* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    mt_MT* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-3
	;;
    nb_NO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    nl_BE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    nl_NL* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    nn_NO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    no_NO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    oc_FR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    om_KE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    pl_PL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    pt_BR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    pt_PT* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    ro_RO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    ru_RU* )
	G_FILENAME_ENCODING=@locale,UTF-8,$russian_legacy_encoding,CP1251
	;;
    ru_UA* )
	G_FILENAME_ENCODING=@locale,UTF-8,KOI8-U
	;;
    sh_YU* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    sk_SK* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    sl_SI* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-2,CP1250
	;;
    so_DJ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    so_KE* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    so_SO* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    sq_AL* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    sr_YU* )
	G_FILENAME_ENCODING=@locale,UTF-8,$sr_YU_legacy_encoding
	;;
    st_ZA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    sv_FI* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    sv_SE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    tg_TJ* )
	G_FILENAME_ENCODING=@locale,UTF-8,KOI8-T
	;;
    th_TH* )
	G_FILENAME_ENCODING=@locale,UTF-8,TIS-620,ISO-8859-1
	;;
    tl_PH* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    tr_TR* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-9
	;;
    uk_UA* )
	G_FILENAME_ENCODING=@locale,UTF-8,KOI8-U
	;;
    uz_UZ* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    vi_VN* )
	G_FILENAME_ENCODING=@locale,UTF-8,TCVN5712-1,ISO-8859-1
	;;
    wa_BE* )
	G_FILENAME_ENCODING=@locale,UTF-8,$west_europe_legacy_encoding,CP1252
	;;
    xh_ZA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
    yi_US* )
	G_FILENAME_ENCODING=@locale,UTF-8,CP1255
	;;
    zh_CN* )
	G_FILENAME_ENCODING=@locale,UTF-8,GB2312,GB18030,GBK,ISO-8859-1
	;;
    zh_HK* )
	G_FILENAME_ENCODING=@locale,UTF-8,BIG5-HKSCS,ISO-8859-1
	;;
    zh_SG* )
	G_FILENAME_ENCODING=@locale,UTF-8,GB2312,GB18030,GBK,ISO-8859-1
	;;
    zh_TW* )
	G_FILENAME_ENCODING=@locale,UTF-8,BIG5,EUC-TW,ISO-8859-1
	;;
    zu_ZA* )
	G_FILENAME_ENCODING=@locale,UTF-8,ISO-8859-1,CP1252
	;;
esac
export G_FILENAME_ENCODING

unset west_europe_legacy_encoding
unset russian_legacy_encoding
unset sr_YU_legacy_encoding
