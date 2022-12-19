import
  std/json,
  std/jsonutils,
  std/options,
  std/strutils,
  std/strformat
type
  DifficultyKind* = enum
    Beginner
    Basic
    Difficult
    Expert
    Challenge
  PlaySide* = enum
    Single
    Double
  BPMContener* = object
    main*: float
    sub*: seq[float]
  Date* = ref object
    y*, m*, d*: int
  ChartInfo* = object
    index*: int
    side*: PlaySide
    kind*: DifficultyKind
    dif*: int
    name*: string
    bpm*: BPMContener
    highScore*: Option[int]
    isCleared*: bool
    isDeleted*: bool
    isUnlocked*: bool
    clearDay*: Option[Date]
    alias*: seq[string]
    note*: seq[string]

proc emptyBPMContener*: BPMContener =
  result.main = 0.0
  result.sub = @[]

proc newDate(y, m, d: int): Date =
  result.new()
  result.y = y
  result.m = m
  result.d = d

proc defaultDate*: Date =
  newDate(1970, 1, 1)

proc emptyChartInfo*: ChartInfo =
  result.index = 0
  result.side = Single
  result.kind = Beginner
  result.name = ""
  result.dif = 1
  result.bpm = emptyBPMContener()
  result.highScore = int.none
  result.isCleared = false
  result.isDeleted = false
  result.isUnlocked = true
  result.clearDay = Date.none
  result.alias = newSeq[string]()
  result.note = newSeq[string]()

proc displayBpm*(c: ChartInfo): string =
  let hyphen = "-"
  if c.bpm.sub.len > 0:
    fmt"{c.bpm.main}({c.bpm.sub.join(hyphen)})"
  else:
    fmt"{c.bpm.main}(strong style)"

proc displayScore*(c: ChartInfo): string =
  if c.highScore.isSome:
    result = fmt"{c.highScore.get(0)}"
    if not c.isCleared:
      result.add " Failed"
  else:
    return "not played"

proc displayState*(c: ChartInfo): string =
  if not c.isDeleted and c.isUnlocked:
    return "Playable"
  else:
    if c.isDeleted:
      result.add "Deleted "
    if not c.isUnlocked:
      result.add "Locked "

proc displayClearDay*(c: ChartInfo): string =
  if c.isCleared:
    if c.clearDay.isSome:
      let d = c.clearDay.get defaultDate()
      return fmt"{d.y}-{d.m}-{d.d}"
    else:
      return "unkonow"
  else:
    return "Not Cleared"

proc stringify*(c: ChartInfo): string =
  fmt"[{c.index}]{c.name} {c.side}-{c.kind} {c.dif}"

import sp17

proc readChart: seq[ChartInfo] =
  result.fromJson jCharts.parseJson

let charts* = readChart()
