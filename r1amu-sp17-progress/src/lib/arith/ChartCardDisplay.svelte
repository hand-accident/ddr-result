<script context="module">
    export function score(score, cleared) {
        return score === null
            ? "not played"
            : score + (cleared ? "" : " Falied");
    }
    export function bpmMain(b) {
        return `BPM: ${b}`;
    }
    export function bpmSub(bs) {
        return bs.join(" - ");
    }
    export function date(cleared, day) {
        return cleared ? `${day.y}-${day.m}-${day.d}` : "not cleared";
    }
    export function availability(deleted, unlocked) {
        return !deleted && unlocked
            ? "Playable"
            : [!!deleted ? "Deleted" : "", !unlocked ? "Locked" : ""].join(" ");
    }
</script>

<slot />
