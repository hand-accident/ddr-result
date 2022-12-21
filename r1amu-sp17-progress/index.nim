include karax/prelude

import view

proc createDom: VNode =
  result = buildHtml(tdiv):
    navBar()
    displaycharts()

setRenderer createDom
