include karax/prelude

import view

proc createDom: VNode =
  kxi.avoidDomDiffing
  result = buildHtml(tdiv):
    navBar()
    displaycharts()

setRenderer createDom
