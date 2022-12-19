import chartdata
import std/[sets, sequtils, algorithm, options]

type
  ChartSortOrder* = enum
    ByName
    ByScore
    ByClearDay
  AchievementEnum* = enum
    Cleared
    Failed
    Noplay
  AvailabilityEnum* = enum
    Playable
    Deleted
    Locked
  Kind2DispBool* = object
    achievement*: array[AchievementEnum, bool]
    availability*: array[AvailabilityEnum, bool]
  Kind2DispSet* = object
    achievement*: array[AchievementEnum, HashSet[int]]
    availability*: array[AvailabilityEnum, HashSet[int]]
  BtnPrms* = object
    order*: ChartSortOrder
    dispKind*: Kind2DispBool
  State* = object
    btns*: BtnPrms
    unfilteredIdcs: array[ChartSortOrder, seq[int]]
    idcsFilter: Kind2Dispset

proc initBtnPrms: BtnPrms =
  result.order = ByName
  for c in AchievementEnum:
    result.dispKind.achievement[c] = false
  for v in AvailabilityEnum:
    result.dispKind.availability[v] = false

proc myCmpGenerator(cso: ChartSortOrder): proc (ix, jy: (int, ChartInfo)): int =
  proc myCmp(ix, jy: (int, ChartInfo)): int {.closure.} =
    let
      x = ix[1]
      y = jy[1]
    case cso
    of ByName:
      return cmp(x.name, y.name)
    of ByScore:
      return -cmp(x.highScore.get(-1), y.highScore.get(-1))
    of ByClearDay:
      var
        xd = 0
        yd = 0
      if x.clearDay.isSome:
        let barex = x.clearDay.get(defaultDate())
        xd = barex.y * 10000 + barex.m * 100 + barex.d
      if y.clearDay.isSome:
        let barey = y.clearDay.get(defaultDate())
        yd = barey.y * 10000 + barey.m * 100 + barey.d
      return -cmp(xd, yd)
  return myCmp

proc myFilterGenerator(c: AchievementEnum): proc(ix: (int, ChartInfo)): bool =
  proc myFilter(ix: (int, ChartInfo)): bool {.closure.} =
    let
      x = ix[1]
    case c
    of Cleared:
      return x.isCleared
    of Failed:
      return (not x.isCleared) and (x.highScore.isSome)
    of Noplay:
      return x.highScore.isNone
  return myFilter

proc myFilterGenerator(v: AvailabilityEnum): proc(ix: (int, ChartInfo)): bool =
  proc myFilter(ix: (int, ChartInfo)): bool {.closure.} =
    let
      x = ix[1]
    case v
    of Playable:
      return (not x.isDeleted) and (x.isUnlocked)
    of Deleted:
      return x.isDeleted
    of Locked:
      return (not x.isUnlocked)
  return myFilter

proc initState*: State =
  result.btns = initBtnPrms()

  for cso in ChartSortOrder:
    result.unfilteredIdcs[cso] = charts.pairs.toSeq.sorted(
      cso.myCmpGenerator).mapIt(it[0])

  for c in AchievementEnum:
    result.idcsFilter.achievement[c] = charts.pairs.toSeq.filter(
        c.myFilterGenerator).mapIt(it[0]).toHashSet
  for v in AvailabilityEnum:
    result.idcsFilter.availability[v] = charts.pairs.toSeq.filter(
        v.myFilterGenerator).mapIt(it[0]).toHashSet

proc `+=`[T](x: var HashSet[T], y: HashSet[T]) =
  x = x + y

proc chartIdcs*(s: State): seq[int] =
  var
    setByAchievement: HashSet[int]
    setByAvailability: HashSet[int]

  for c in AchievementEnum:
    if s.btns.dispKind.achievement[c]:
      setByAchievement += s.idcsFilter.achievement[c]
  for v in AvailabilityEnum:
    if s.btns.dispKind.availability[v]:
      setByAvailability += s.idcsFilter.availability[v]

  return s.unfilteredIdcs[s.btns.order].filterIt(it in (setByAchievement *
      setByAvailability))


proc changeState*(s: State, c: AchievementEnum): State =
  result = s
  result.btns.dispKind.achievement[c] = not s.btns.dispKind.achievement[c]

proc changeState*(s: State, v: AvailabilityEnum): State =
  result = s
  result.btns.dispKind.availability[v] = not s.btns.dispKind.availability[v]

proc changeState*(s: State, o: ChartSortOrder): State =
  result = s
  result.btns.order = o

var state* = initState().changeState(Cleared).changeState(Playable)
