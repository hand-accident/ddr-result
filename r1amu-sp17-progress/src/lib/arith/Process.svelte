<script context="module">
    import { ChartData, Config } from "./Classes.svelte";
    let sanitization = {
        ÆTHER: "AETHER",
        ΔMAX: "delta max",
        ΩVER: "over",
    };
    /**
     *
     * @param {ChartData} a
     * @param {ChartData} b
     * @returns {number}
     */
    function sortByName(a, b) {
        let names = [a, b].map((x) => {
            let result = x.name;
            for (const [key, value] of Object.entries(sanitization)) {
                result = result.replace(new RegExp(key), value);
            }
            return result;
        });
        if (names[0] < names[1]) {
            return -1;
        } else if (names[0] > names[1]) {
            return 1;
        } else {
            return 0;
        }
    }
    /**
     *
     * @param {ChartData} a
     * @param {ChartData} b
     * @returns {number}
     */
    function sortByScore(a, b) {
        return (b.highScore || 0) - (a.highScore || 0);
    }
    /**
     *
     * @param {ChartData} a
     * @param {ChartData} b
     * @returns {number}
     */
    function sortByDate(a, b) {
        if (a.clearDay === null && b.clearDay === null) return 0;
        if (a.clearDay !== null && b.clearDay === null) return 1;
        if (b.clearDay !== null && a.clearDay === null) return -1;
        const y = b.clearDay.y - a.clearDay.y;
        const m = b.clearDay.m - a.clearDay.m;
        const d = b.clearDay.d - a.clearDay.d;
        const result = y * 10000 + m * 100 + d;
        return result;
    }
    /**
     *
     * @param {ChartData[]}cs
     * @param {string}kind
     * @returns {ChartData[]}
     */
    function sort(cs, kind) {
        switch (kind) {
            case "name":
                return cs.slice().sort(sortByName);
            case "score":
                return cs.slice().sort(sortByScore);
            case "date":
                return cs.slice().sort(sortByDate);
            default:
                return cs;
        }
    }
    /**
     *
     * @param {ChartData[]}cs
     * @param {Config}config
     * @returns {ChartData[]}
     */
    function filter(cs, config) {
        return cs.filter((c) => {
            return (
                [
                    config.cleared && c.isCleared,
                    config.failed && !c.isCleared && c.highScore !== null,
                    config.notPlayed && c.highScore === null,
                ].reduce((a, b) => {
                    return a || b;
                }) &&
                [
                    config.playable && !c.isDeleted && c.isUnlocked,
                    config.deleted && c.isDeleted,
                    config.locked && !c.isUnlocked,
                ].reduce((a, b) => {
                    return a || b;
                })
            );
        });
    }
    /**
     *
     * @param {ChartData[]}cs
     * @param {Config}config
     * @returns {ChartData[]}
     */
    export function process(cs, config) {
        return sort(filter(cs, config), config.sort);
    }
</script>
