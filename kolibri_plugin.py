from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from django.templatetags.static import static

from kolibri.core import theme_hook
from kolibri.plugins import KolibriPluginBase
from kolibri.plugins.hooks import register_hook


class Bot1ThemePlugin(KolibriPluginBase):
    pass


@register_hook
class Bot1ThemeHook(theme_hook.ThemeHook):

    @property
    def theme(self):
        background_image = static("background.jpg")
        logo_image = static("kolibri-logo-login.svg")
        return {
            "brandColors": {
                "primary": {
                    "v_50": "#efece6",
                    "v_100": "#efece6",
                    "v_200": "#000a00",
                    "v_300": "#45BFB9", #titulo de login
                    "v_400": "#45BFB9", #botones, temaa
                    "v_500": "#390000",
                    "v_600": "#390000",
                    "v_700": "#40afaa", #texto login, hover menu, texto activo
                    "v_800": "#390000",
                    "v_900": "#00ee",
                },
                "secondary": {
                    "v_50": "#e3f0ed",
                    "v_100": "#badbd2",
                    "v_200": "#8dc5b6",
                    "v_300": "#62af9a",
                    "v_400": "#479e86",
                    "v_500": "#368d74",
                    "v_600": "#328168",
                    "v_700": "#2c715a",
                    "v_800": "#26614d",
                    "v_900": "#1b4634",
                },
            },
            "tokenMapping": {
                "primary": "#45BFB9",
                "appBar": "#45BFB9",
            },
            # sign-in page config
            "signIn": {
                "background": background_image,
                "scrimOpacity": 0.7,
                "title":  "Bienvenido",  # use default: ""
                "topLogo": {
                    "src": logo_image,
                    "style": "padding-left: 64px; padding-right: 64px; margin-bottom: 8px; margin-top: 8px",
                    "alt": None,
                },
                "titleStyle": "font-style: NotoSans; color: #45BFB9 !important", 
                "showPoweredBy": False,
                "showTitle": True,
                'backgroundImgCredit': '1bot S.A.',
                "showKolibriFooterLogo": False, 
                
            },
            # side-nav config
            "sideNav": {
                "title": "1bot", 
                "brandedFooter": {
                    "logo": {
                        "src": logo_image,
                    },
                    "paragraphArray": [
                        "1bot.org ",
                    ],
                },
                "showKolibriFooterLogo": False,
            },
            # app bar config
            "appBar": {
                "topLogo": {
                    "src": logo_image,
                },
                "v_50": "#e3f0ed",
                "v_100": "#badbd2",
                "v_200": "#8dc5b6",
                "v_300": "#62af9a",
                "v_400": "#479e86",
                "v_500": "#368d74",
                "v_600": "#328168",
                "v_700": "#2c715a",
                "v_800": "#26614d",
                "v_900": "#1b4634",
            },
        }

