import yattag
import toolz as tz
import pathlib
import subprocess
import codecs
import sys
import dataclasses as dcs

urls = {'bulma': r"https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css",
        'fontawesome': r"https://use.fontawesome.com/releases/v5.15.4/css/all.css"}
extraCSS = (
    "/*! bulma.io v0.9.3 | MIT License | https://github.com/jgthms/bulma */"
    "/*! Font Awesome Free 5.15.4 by @fontawesome | https://fontawesome.com |"
    " license: https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) */"
    ".button.is-floating {"
    "position: fixed;"
    "width: 60px;height: 60px;bottom: 40px;right: 40px;"
    "border-radius: 100px;"
    "text-align: center;"
    "font-size: 1.6rem;"
    "box-shadow: 0 .0625em .125em rgba(10, 10, 10, .05);"
    "z-index: 3;}"
    ".button.is-floating.is-medium {"
    "width: 75px;height: 75px;"
    "font-size: 2.2rem;}"
    ".menu {"
    "position: sticky;"
    "display: inline-block;"
    "vertical-align: top;"
    "max-height: 100vh;"
    "overflow-y: auto;"
    # "width: 200px;"
    "top: 0;bottom: 0;"
    # "padding: 30px}"
    "}"
    #  ".content {display: inline-block}"
    ".image img{height: 100%; object-fit: cover;}")


def sp_join(*ss):
    return ' '.join(ss)


def hy_join(*ss):
    return '-'.join(ss)


green = "primary"
dark_green = hy_join(green, "dark")
blue = "info"
light = "light"
purple = "link"


def has_bg(color):
    return hy_join('has', 'background', color)


def is_color(color):
    return hy_join('is', color)


def is_(attr):
    return is_color(attr)


def has_text(color):
    return hy_join('has', 'text', color)


class HTMLGenerator:
    def __init__(self, title=''):
        self.doc, self.tag, self.text, self.line = yattag.Doc().ttl()
        self.title = title

    def stag(self, *args, **kwargs):
        return self.doc.stag(*args, **kwargs)

    def tag_of(self, name, *args, **kwargs):
        return self.tag(name, klass=sp_join(*args), **kwargs)

    def generate(self):
        self.doc.asis('<!DOCTYPE html>')  # noqa
        with self.tag('html', lang='ja'):
            with self.tag('head'):
                self.head()
            with self.tag_of('body', has_bg(light)):
                self.body()
                with self.tag_of('footer', "footer", has_bg(dark_green)):
                    self.footer()

    def head(self):
        self.stag('meta', charset='utf-8')
        self.line('title', self.title)
        self.stag('link', rel="stylesheet", href=urls['bulma'])
        self.stag('link', rel="stylesheet", href=urls['fontawesome'])
        self.line('style', extraCSS)

    def body(self):
        raise NotImplementedError

    def footer(self):
        # self.line_of('p', "made by hand_accident", "level-item", has_text(light))
        raise NotImplementedError

    def out(self) -> str:
        return yattag.indent(self.doc.getvalue())

    def tag_div(self, *args, **kwargs):
        return self.tag_of('div', *args, **kwargs)

    def tag_sec(self, *args, **kwargs):
        return self.tag_of('section', *args, **kwargs)

    def line_of(self, name, text, *args, **kwargs):
        return self.line(name, text, klass=sp_join(*args), **kwargs)

    def stag_of(self, name, *args, **kwargs):
        return self.stag(name, klass=sp_join(*args), **kwargs)

    def ex_line(self, tag_name, content):
        if callable(content):
            with self.tag(tag_name):
                content()
        else:
            self.line(tag_name, content)

    def table(self, contents, header=False, index=None, row_ids=None):
        if index is None:
            index = []
        if row_ids is None:
            row_ids = []
        with self.tag_of('table', 'table'):
            if header and index:
                with self.tag('thead'):  # noqa
                    with self.tag('tr'):
                        for i in index:
                            self.ex_line('th', i)

            with self.tag('tbody'):  # noqa
                if row_ids and len(row_ids) == len(contents):
                    for row, id_ in zip(contents, row_ids):
                        with self.tag('tr', id=id_):
                            for c in row:
                                self.ex_line('td', c)

                else:
                    for row in contents:
                        with self.tag('tr'):
                            for c in row:
                                self.ex_line('td', c)

    def jump_to_id(self, id_, display_name):
        with self.tag('a', href=f'#{id_}'):
            self.text(display_name)

    def jump_to_file(self, path: pathlib.Path, display_name):
        with self.tag('a', href=f'file:///{path.resolve()}',
                      target='_blank', rel='noopener noreferrer'):  # noqa
            self.text(display_name)

    def jump_to_link(self, path: pathlib.Path, display_name):
        with self.tag('a', href=str(path), target='_blank', rel='noopener noreferrer'):  # noqa
            self.text(display_name)

    def u_list(self, content, **kwargs):
        with self.tag('ul', **kwargs):
            for c in content:
                self.ex_line('li', c)


@dcs.dataclass
class I:
    index: int
    name: str
    dif: str
    score: str
    another_index: int = 0

    def __post_init__(self):
        image_name = (
            str(self.index)
            + {'BASIC': 'b', 'DIFFICULT': 'd',
                'EXPERT': 'e', 'CHALLENGE': 'c'}[self.dif]
            + ('' if self.another_index == 0 else str(self.another_index)))
        self.image_path = pathlib.Path(f"./imgs/{image_name}.jpg")


selective = {
    "965k+ a L14": [I(781, "ロールプレイングゲーム", "EXPERT", "968,420")],
    "930k+ a L15": [I(921, "CyberConnect", "EXPERT", "967,700")],
    "900k+ a L16": [I(978, "Lightspeed", "EXPERT", "904,560")],
    "Clear a L15 on LIFE4": [I(949, "I Want To Do This Keep", "EXPERT", "940,920", another_index=1)],
    "Clear 30 L15s": [I(921, "CyberConnect", "EXPERT", "967,700"),
                      I(65, "MAX 300", "EXPERT", "965,950"),
                      I(892, "おーまい！らぶりー！すうぃーてぃ！だーりん！", "EXPERT", "952,350"),
                      I(946, "City Never Sleeps", "EXPERT", "946,220"),
                      I(938, "HyperTwist", "EXPERT", "944,640"),
                      # I(949, "I Want To Do This Keep", "EXPERT", "941,110"), # photo lost
                      I(949, "I Want To Do This Keep", "EXPERT", "940,330"),
                      I(951, "Our Love", "EXPERT", "935,300"),
                      I(1023, "Globe Glitter", "EXPERT", "925,890"),
                      I(889, "BLACK JACKAL", "EXPERT", "925,130"),
                      I(439, "Chronos", "CHALLENGE", "924,440"),
                      I(964, "HARD BRAIN", "EXPERT", "924,180"),
                      I(291, "Horatio", "EXPERT", "917,250"),
                      I(626, "エンドルフィン", "EXPERT", "915,840"),
                      I(817, "シュレーディンガーの猫", "EXPERT", "914,940"),
                      I(401, "ZETA～素数の世界と超越者～", "EXPERT", "910,300"),
                      I(831, "Procyon", "EXPERT", "908,530"),
                      I(606, "Cleopatrysm", "EXPERT", "908,520"),
                      I(727, "ロストワンの号哭", "CHALLENGE", "908,280"),
                      I(1005, "If", "EXPERT", "907,430"),
                      I(965, "狂水一華", "EXPERT", "907,110"),
                      I(989, "Vertigo", "EXPERT", "906,750"),
                      # I(1074, "Worst Plan", "EXPERT", "896,000"), # photo lost
                      I(1074, "Worst Plan", "EXPERT", "886,010"),
                      I(937, "Hyper Bomb", "EXPERT", "888,760"),
                      I(228, "Arrabbiata", "EXPERT", "885,350"),
                      I(1007, "Poppin' Soda", "EXPERT", "880,070"),
                      I(741, "ZEPHYRANTHES", "EXPERT", "876,120"),
                      I(971, "Going Hypersonic", "EXPERT", "870,490"),
                      I(588, "SABER WING (satellite silhouette remix)",
                        "CHALLENGE", "868,050"),
                      I(728, "Astrogazer", "EXPERT", "864,880"),
                      I(1024, "ユメブキ", "EXPERT", "861,370")],
    "Clear 20 L16s":  [I(978, "Lightspeed", "EXPERT", "904,560"),
                       I(1017, "High & Low", "EXPERT", "894,250"),
                       I(1038, "ノープラン・デイズ", "EXPERT", "892,350"),
                       I(1088, "Megalara Garuda", "DIFFICULT", "890,990"),
                       I(1008, "Sword of Vengeance", "EXPERT", "886,260"),
                       I(955, "Last Twilight", "EXPERT", "886,190"),
                       I(693, "打打打打打打打打打打", "CHALLENGE", "883,300"),
                       I(634, "POSSESSION(EDP Live Mix)", "EXPERT", "882,920"),
                       I(896, "Rampage Hero", "EXPERT", "878,980"),
                       I(991, "We're so Happy", "EXPERT", "877,580"),
                       I(923, "ナイト・オブ・ナイツ (Ryu☆Remix)", "EXPERT", "873,860"),
                       I(599, "Idola", "EXPERT", "868,350"),
                       I(359, "I'm so Happy", "CHALLENGE", "862,430"),
                       I(919, "Firestorm", "EXPERT", "857,970"),
                       I(864, "BLSTR", "EXPERT", "857,240"),
                       I(818, "ANNIVERSARY ∴∵∴ ←↓↑→", "EXPERT", "850,940"),
                       I(556, "Chinese Snowy Dance", "EXPERT", "850,780"),
                       I(608, "KHAMEN BREAK", "EXPERT", "850,600"),
                       I(557, "†渚の小悪魔ラヴリィ～レイディオ†", "EXPERT", "843,640"),
                       I(939, "In the past", "EXPERT", "842,610")],
    "Clear 3 L17s": [I(926, "び", "EXPERT", "790,110"),
                     I(765, "Be a Hero!", "EXPERT", "763,800"),
                     I(954, "DIGITALIZER", "EXPERT", "737,400")]}
mandatory = {
    "clear 40 L14s": [I(781, "ロールプレイングゲーム", "EXPERT", "968,420"),
                      I(879, "Ace out", "EXPERT", "967,420"),
                      I(1016, "勇猛無比", "EXPERT", "966,240"),
                      I(1006, "ONYX", "EXPERT", "962,210"),
                      I(995, "Hella Deep", "EXPERT", "954,270"),
                      I(759, "脳漿炸裂ガール", "CHALLENGE", "953,660"),
                      I(950, "STEP MACHINE", "EXPERT", "953,650"),
                      I(670, "neko*neko", "CHALLENGE", "950,390"),
                      I(1031, "ほしのつくりかた", "EXPERT", "949,950"),
                      I(977, "Red Cape Theorem", "EXPERT", "947,790"),
                      I(369, "New Decade", "DIFFICULT", "947,730"),
                      I(1068, "ウサテイ", "EXPERT", "946,240"),
                      I(351, "FIRE FIRE", "EXPERT", "943,140"),
                      I(595, "セツナトリップ", "EXPERT", "941,870"),
                      I(907, "Bounce Trippy", "EXPERT", "940,640"),
                      I(861, "Right Time Right Way", "EXPERT", "940,110"),
                      I(859, "F4SH10N", "EXPERT", "939,830"),
                      I(570, "HYENA", "EXPERT", "939,560"),
                      I(1013, "Uh-Oh", "EXPERT", "939,280"),
                      I(536, "Elemental Creation", "DIFFICULT", "938,550"),
                      I(403, "不沈艦CANDY", "EXPERT", "937,560"),
                      I(1015, "Jucunda Memoria", "DIFFICULT", "937,050"),
                      I(990, "BITTER CHOCOLATE STRIKER", "EXPERT", "935,210"),
                      I(749, "Ishtar", "EXPERT", "935,170"),
                      I(701, "黒髪乱れし修羅となりて～凛 edition～", "EXPERT", "935,060"),
                      I(1022, "シル・ヴ・プレジデント", "CHALLENGE", "934,520"),
                      I(729, "Cytokinesis", "EXPERT", "934,430"),
                      I(304, "PARANOiA Rebirth(X-Special)", "CHALLENGE", "934,340"),
                      I(887, "最小三倍完全数", "DIFFICULT", "933,120"),
                      I(700, "New Century", "DIFFICULT", "932,270"),
                      I(747, "恋する☆宇宙戦争っ!!", "EXPERT", "930,620"),
                      I(894, "Afterimage d'automne", "EXPERT", "928,560"),
                      I(553, "RЁVOLUTIФN", "EXPERT", "924,590"),
                      I(656, "妖隠し -あやかしかくし-", "EXPERT", "923,400"),
                      I(384, "Sakura Sunrise", "EXPERT", "921,660"),
                      I(561, "ちくわパフェだよ☆CKP", "CHALLENGE", "921,310"),
                      I(890, "Six String Proof", "EXPERT", "919,860"),
                      I(930, "GUILTY DIAMONDS", "EXPERT", "915,240"),
                      I(664, "Sakura Mirage", "EXPERT", "915,130"),
                      I(1077, "Black Emperor", "DIFFICULT", "911,800")],
    "pfc a L9 or 3 L7+s": [I(951, "Our Love", "BASIC", "999,670"),
                           I(1017, "High & Low", "BASIC", "999,590"),
                           I(50, "AFRONOVA PRIMEVAL", "BASIC", "999,690")]}


class SubmissionGen(HTMLGenerator):
    def __init__(self):
        super().__init__('GOLD II')
        self.generate()

    def body(self):
        with self.tag_of('header', 'header'):
            self.header()
        with self.tag_div('hero-body'):
            with self.tag_sec("columns", "p-4", "m-0"):
                self.display_body()
            self.back_button()

    def header(self):
        with self.tag_sec('hero', is_color(green)):
            with self.tag_div('hero-body'):
                self.line_of(f'h1', 'GOLD II submission', f'title')

    def footer(self):
        with self.tag_div('level'):
            with self.tag_div('level-item'):
                self.line_of('p', "made by hand_accident", has_text(light))
                with self.tag(
                    'a', href='https://twitter.com/hand_accident',
                    target='_blank', rel='noopener noreferrer', klass='button'):
                        self.text('twitter')
                with self.tag(
                    'a', href="https://github.com/hand-accident",
                    target='_blank', rel='noopener noreferrer', klass='button'):
                        self.text('github')

    def jump_button(self, href, button_config, button_icon, jump_config):
        with self.tag('a', href=href, **jump_config):
            with self.tag_of('button', 'button', *button_config):
                with self.tag_of('span', 'icon'):
                    with self.tag_of('i', *button_icon):
                        pass

    def display_body(self):
        self.display_index()
        with self.tag_sec('column'):
            self.line_of('h1', 'links', 'title')
            with self.tag(
                    'a', href="http://skillattack.com/sa4/dancer_profile.php?ddrcode=51449631",
                    target='_blank', rel='noopener noreferrer', klass='button'):
                self.text('skillatack')
            with self.tag(
                    'a', href="https://3icecream.com/profile/haxident",
                    target='_blank', rel='noopener noreferrer', klass='button'):
                self.text('3icecream')
            with self.tag(
                    'a', href="https://github.com/hand-accident/ddr-result",
                    target='_blank', rel='noopener noreferrer', klass='button'):
                self.text('page source(github)')
            
            self.doc.asis('<hr><hr>')

            for req_kind, reqs in {'selective': selective, 'mandatory': mandatory}.items():
                self.display_reqs(req_kind, reqs)

    def display_reqs(self, req_kind, reqs):
        self.line_of('h1', f'{req_kind} requirements', 'title', id=req_kind)
        for i, (req, musics) in enumerate(reqs.items()):
            self.display_req(req_kind, reqs, i, req, musics)

    def display_req(self, req_kind, reqs, i, req, musics):
        def button_neighbor(number, direction):
            self.jump_button(f'#{req_kind}-req{number}', [is_color(purple), is_(
                'medium')], ['fa', f'fa-arrow-{direction}'], dict(klass='level-item'))

        with self.tag_div('level-left'):
            self.line_of('h2', req, 'title',
                         'level-item', id=f'{req_kind}-req{i}')
            if i != len(reqs) - 1:
                button_neighbor(i + 1, 'down')
            if i != 0:
                button_neighbor(i - 1, 'up')

        for j, music in enumerate(musics):
            self.display_music(j, music)
        self.doc.asis('<hr>')

    def display_music(self, j, music):
        with self.tag_of('article', 'media'):
            with self.tag_of('figure', 'media-left'):
                with self.tag('a', href=str(music.image_path), target='_blank', rel='noopener noreferrer'):
                    with self.tag_of('p', 'image', is_('128x128')):
                        self.doc.asis(f'<img src={str(music.image_path)}>')
            with self.tag_div('media-content'):
                with self.tag_div('content'):
                    self.line(
                        'p', f'{j+1}: {music.name} {music.dif} {music.score}')

    def back_button(self):
        self.jump_button('#',
                         [is_color(purple), is_('medium'), is_('floating')],
                         ['fas', 'fa-chevron-up'],
                         {})

    def display_index(self):
        with self.tag_div('submenu', 'column', is_('2'), has_bg(dark_green)):
            with self.tag_of('aside', 'box', 'menu'):
                with self.tag_of('ul', 'menu-list'):
                    self.line_of('p', 'index', 'menu-label')
                    for req_kind, reqs in {'selective': selective, 'mandatory': mandatory}.items():
                        with self.tag('li'):
                            self.jump_to_id(req_kind, f'{req_kind} requirements')
                            with self.tag('ul'):
                                for i, (req, _) in enumerate(reqs.items()):
                                    with self.tag('li'):
                                        self.jump_to_id(f'{req_kind}-req{i}', req)


def to_file_and_open(path: pathlib.Path, force_overwrite=True):
    def _wrapper(func):
        def _inner(*args, **kwargs):
            if force_overwrite:
                path.unlink(missing_ok=True)

            sys.stdout = codecs.open(
                str(path.resolve()), 'ab', 'utf-8', 'ignore')

            func(*args, **kwargs)

            sys.stdout = sys.__stdout__

            subprocess.Popen(path.name, shell=True, cwd=path.parent).wait()

        return _inner

    return _wrapper


def main():
    result = SubmissionGen().out()

    print(result)


if __name__ == '__main__':
    save_path = pathlib.Path(__file__).parent / 'index.html'
    to_file_and_open(save_path)(main)()
