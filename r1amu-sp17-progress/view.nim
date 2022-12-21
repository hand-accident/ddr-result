{.push warning[UnusedImport]: off.}
{.push warning[CStringConv]: off.}

import std/[algorithm, sequtils, sugar, strformat, strutils, options]
include karax/prelude
import chartdata, stateutils
const eK = kstring""

proc card(
    header, content, actions: VNode,
    classes = (ek, ek, ek, ek)): VNode =
  result = buildHtml:
    tdiv(class = fmt"card shadow-xl {classes[0]}"):
      tdiv(class = fmt"card-title {classes[1]}"):
        header
      tdiv(class = fmt"card-body {classes[2]}"):
        content
        tdiv(class = fmt"card-actions {classes[3]}"):
          actions

proc chartCard(c: ChartInfo): VNode =
  let
    hyphen = " - "
    header = buildHTML(tdiv(class = "flex flex-row")):
      p(c.name.text)
      case c.kind
      of Beginner:
        tdiv(class = "badge badge-info badge-outline", text"習")
      of Basic:
        tdiv(class = "badge badge-secondary badge-outline", text"楽")
      of Difficult:
        tdiv(class = "badge badge-error badge-outline", text"踊")
      of Expert:
        tdiv(class = "badge badge-success badge-outline", text"激")
      of Challenge:
        tdiv(class = "badge badge-primary badge-outline", text"鬼")
    content = buildHTML(tdiv):
      p(class = "text-3xl", c.displayScore.text)
      p(class = "text-xl", fmt"BPM: {c.bpm.main}".text)
      p(class = "text-xs", c.bpm.sub.join(hyphen).text)
    actions = tdiv.buildHTML:
      tdiv(class = "badge badge-outline", c.displayClearDay.text)
      tdiv(class = "badge badge-outline", c.displayState.text)
  result = buildHtml(section(id = fmt"chart-{c.name}-{c.kind}")):
    card(header, content, actions, (kstring"w-96 m-4", ek, ek,
        kstring"justify-end"))

proc displaycharts*(chartIndices: seq[int]): VNode =
  result = buildHtml(tdiv(class = "flex flex-wrap")):
    for i in chartIndices:
      charts[i].chartCard
    tdiv(class = fmt"card shadow-xl w-96 m-4"):
      tdiv(class = fmt"card-body"):
        a(href = "#ROOT"):
          button(class = "btn btn-primary btn-lg"):
            text"back to top"

proc newToggle[T](name: string, checked: bool, val: T): VNode =
  result = buildHtml(tdiv(class = "p-4")):
    tdiv(class = "indicator"):
      span(class = "indicator-item indicator-start badge"):
        text(name)
      input(`type` = "checkbox", class = "toggle toggle-primary toggle-lg",
          checked = checked.toChecked, onclick = () => (
              state = state.changeState(val)))

proc buttonColor(cond: bool): string =
  if cond:
    "btn-neutral"
  else:
    "btn-secondary"

proc sortButton(name: string, order, sOrder: ChartSortOrder): VNode =
  result = buildHtml(tdiv(class = "p-4")):
    button(class = fmt"btn {buttonColor(order == sOrder)}"):
      proc onclick = state = state.changeState order
      text(name)

proc navBar*(prms: BtnPrms): VNode =
  result = buildHtml(tdiv(class = "sticky")):
    tdiv(class = "navbar bg-base-200"):
      ul(class = "menu menu-horizontal px-1"):
        for (c, name) in AchievementEnum.toSeq.zip(@["cleared", "failed", "notPlayed"]):
          li:
            newToggle(name, prms.dispKind.achievement[c], c)
        for (v, name) in AvailabilityEnum.toSeq.zip(@["playable", "deleted", "locked"]):
          li:
            newToggle(name, prms.dispKind.availability[v], v)
        for (cso, name) in ChartSortOrder.toSeq.zip(@["曲名", "スコア",
            "クリア日"]):
          li:
            sortButton(name, cso, prms.order)

proc navBar*: VNode =
  state.btns.navBar

proc displaycharts*: VNode =
  state.chartIdcs.displaycharts
