import utils
import shutil as fs


def gen_simsun_cl():
    fs.copy(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf', utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular-new.ttf')

    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_simsun_names(font)

    font_ui = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular-new.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_new_simsun_names(font_ui)

    font.generateTtc(utils.OUTPUT_DIR_CL + '/simsun.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_simsun_ext_cl():
    font = utils.open_font(utils.DOWNLOAD_DIR + '/sarasa-ui-cl-regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_simsun_ext_names(font)

    font.generate(utils.OUTPUT_DIR_CL + '/simsunb.ttf')
