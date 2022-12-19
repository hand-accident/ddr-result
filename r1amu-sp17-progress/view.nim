{.push warning[UnusedImport]: off.}
{.push warning[CStringConv]: off.}

import std/[algorithm, sequtils, sugar, strformat, strutils, options]
include karax/prelude
import chartdata, stateutils
const eK = kstring""
type
  Card = ref object of VComponent
    header, content, actions: VNode
  ChartCard = ref object of VComponent
    chart: ChartInfo
  Toggle* = ref object of VComponent
    checked*: bool
  SortButton = ref object of VComponent
    order: ChartSortOrder
  NavBar = ref object of VComponent
    cts: array[AchievementEnum, Toggle]
    vts: array[AvailabilityEnum, Toggle]
    bs: array[ChartSortOrder, SortButton]
proc card(
    header, content, actions: VNode,
    classes = (ek, ek, ek, ek)): Card =
  proc render(x: VComponent): VNode =
    let self = Card(x)
    result = buildHtml:
      tdiv(class = fmt"card shadow-xl {classes[0]}"):
        tdiv(class = fmt"card-title {classes[1]}"):
          self.header
        tdiv(class = fmt"card-body {classes[2]}"):
          self.content
          tdiv(class = fmt"card-actions {classes[3]}"):
            self.actions
  result = Card.newComponent render
  result.header = header
  result.content = content
  result.actions = actions

proc chartCard(c: ChartInfo): ChartCard =
  proc render(x: VComponent): VNode =
    let hyphen = " - "
    let self = ChartCard(x)
    let header = buildHTML(tdiv(class = "flex flex-row")):
      p(self.chart.name.text)
      case self.chart.kind
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
    let content = buildHTML(tdiv):
      p(class = "text-3xl", self.chart.displayScore.text)
      p(class = "text-xl", fmt"BPM: {self.chart.bpm.main}".text)
      p(class = "text-xs", self.chart.bpm.sub.join(hyphen).text)
    let actions = tdiv.buildHTML:
      tdiv(class = "badge badge-outline", self.chart.displayClearDay.text)
      tdiv(class = "badge badge-outline", self.chart.displayState.text)
    result = buildHtml(section(id = fmt"chart-{self.chart.name}-{self.chart.kind}")):
      card(header, content, actions, (kstring"w-96 m-4", ek, ek,
          kstring"justify-end"))
  result = ChartCard.newComponent render
  result.chart = c

proc displaycharts*(chartIndices: seq[int]): VNode =
  result = buildHtml(tdiv(class = "flex flex-wrap")):
    for i in chartIndices:
      charts[i].chartCard
    tdiv(class = fmt"card shadow-xl w-96 m-4"):
      tdiv(class = fmt"card-body"):
        a(href = "#ROOT"):
          button(class = "btn btn-primary btn-lg"):
            text"back to top"

proc newToggle[T](name: string, checked: bool, val: T): Toggle =
  proc render(x: VComponent): VNode =
    let self = Toggle(x)
    result = buildHtml(tdiv(class = "p-4")):
      tdiv(class = "indicator"):
        span(class = "indicator-item indicator-start badge"):
          text(name)
        input(`type` = "checkbox", class = "toggle toggle-primary toggle-lg",
            checked = self.checked.toChecked, onclick = () => (
                state = state.changeState(val)))
  result = Toggle.newComponent render
  result.checked = checked

proc buttonColor(cond: bool): string =
  if cond:
    "btn-neutral"
  else:
    "btn-secondary"

proc sortButton(name: string, order, sOrder: ChartSortOrder): SortButton =
  proc render(x: VComponent): VNode =
    let self = SortButton(x)
    result = buildHtml(tdiv(class = "p-4")):

      button(class = fmt"btn {buttonColor(self.order == sOrder)}"):
        proc onclick = state = state.changeState order
        text(name)
  result = SortButton.newComponent render
  result.order = order

proc navBar*(prms: BtnPrms): NavBar =
  proc render(x: VComponent): VNode =
    let self = NavBar(x)
    result = buildHtml(tdiv(class = "sticky")):
      tdiv(class = "navbar bg-base-200"):
        ul(class = "menu menu-horizontal px-1"):
          for cToggle in self.cts:
            li:
              cToggle
          for vToggle in self.vts:
            li:
              vToggle
          for b in self.bs:
            li:
              b

  result = NavBar.newComponent render
  for (c, name) in AchievementEnum.toSeq.zip(@["cleared", "failed",
      "notPlayed"]):
    result.cts[c] = newToggle(name, prms.dispKind.achievement[c], c)
  for (v, name) in AvailabilityEnum.toSeq.zip(@["playable", "deleted", "locked"]):
    result.vts[v] = newToggle(name, prms.dispKind.availability[v], v)
  for (cso, name) in ChartSortOrder.toSeq.zip(@["曲名", "スコア",
      "クリア日"]):
    result.bs[cso] = sortButton(name, cso, prms.order)

proc navBar*: NavBar =
  state.btns.navBar

proc displaycharts*: VNode =
  state.chartIdcs.displaycharts
