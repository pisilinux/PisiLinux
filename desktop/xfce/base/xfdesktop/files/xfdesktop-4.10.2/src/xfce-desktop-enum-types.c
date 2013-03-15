


#undef GTK_DISABLE_DEPRECATED
#define GTK_ENABLE_BROKEN
#include "xfce-desktop.h"
#include "xfce-backdrop.h"
#include "xfce-desktop-enum-types.h"

/* enumerations from "xfce-backdrop.h" */
GType
xfce_backdrop_image_style_get_type (void)
{
	static GType type = 0;
	if (type == 0) {
	static const GEnumValue values[] = {
	{ XFCE_BACKDROP_IMAGE_AUTO, "XFCE_BACKDROP_IMAGE_AUTO", "auto" },
	{ XFCE_BACKDROP_IMAGE_CENTERED, "XFCE_BACKDROP_IMAGE_CENTERED", "centered" },
	{ XFCE_BACKDROP_IMAGE_TILED, "XFCE_BACKDROP_IMAGE_TILED", "tiled" },
	{ XFCE_BACKDROP_IMAGE_STRETCHED, "XFCE_BACKDROP_IMAGE_STRETCHED", "stretched" },
	{ XFCE_BACKDROP_IMAGE_SCALED, "XFCE_BACKDROP_IMAGE_SCALED", "scaled" },
	{ XFCE_BACKDROP_IMAGE_ZOOMED, "XFCE_BACKDROP_IMAGE_ZOOMED", "zoomed" },
	{ 0, NULL, NULL }
	};
	type = g_enum_register_static ("XfceBackdropImageStyle", values);
  }
	return type;
}
GType
xfce_backdrop_color_style_get_type (void)
{
	static GType type = 0;
	if (type == 0) {
	static const GEnumValue values[] = {
	{ XFCE_BACKDROP_COLOR_SOLID, "XFCE_BACKDROP_COLOR_SOLID", "solid" },
	{ XFCE_BACKDROP_COLOR_HORIZ_GRADIENT, "XFCE_BACKDROP_COLOR_HORIZ_GRADIENT", "horiz-gradient" },
	{ XFCE_BACKDROP_COLOR_VERT_GRADIENT, "XFCE_BACKDROP_COLOR_VERT_GRADIENT", "vert-gradient" },
	{ XFCE_BACKDROP_COLOR_TRANSPARENT, "XFCE_BACKDROP_COLOR_TRANSPARENT", "transparent" },
	{ 0, NULL, NULL }
	};
	type = g_enum_register_static ("XfceBackdropColorStyle", values);
  }
	return type;
}

/* enumerations from "xfce-desktop.h" */
GType
xfce_desktop_icon_style_get_type (void)
{
	static GType type = 0;
	if (type == 0) {
	static const GEnumValue values[] = {
	{ XFCE_DESKTOP_ICON_STYLE_NONE, "XFCE_DESKTOP_ICON_STYLE_NONE", "none" },
	{ XFCE_DESKTOP_ICON_STYLE_WINDOWS, "XFCE_DESKTOP_ICON_STYLE_WINDOWS", "windows" },
	{ XFCE_DESKTOP_ICON_STYLE_FILES, "XFCE_DESKTOP_ICON_STYLE_FILES", "files" },
	{ 0, NULL, NULL }
	};
	type = g_enum_register_static ("XfceDesktopIconStyle", values);
  }
	return type;
}



