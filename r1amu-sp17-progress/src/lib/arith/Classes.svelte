<script context="module">
    export class Config {
        /**
         * @param {
         * {
         * cleared?: boolean,
         * failed?: boolean,
         * notPlayed?: boolean,
         * playable?: boolean,
         * deleted?: boolean,
         * locked?: boolean,
         * sort?: string}
         * } config
         */
        constructor(config) {
            /**@type {boolean}*/
            this.cleared = config.cleared || false;
            /**@type {boolean}*/
            this.failed = config.failed || false;
            /**@type {boolean}*/
            this.notPlayed = config.notPlayed || false;
            /**@type {boolean}*/
            this.playable = config.playable || false;
            /**@type {boolean}*/
            this.deleted = config.deleted || false;
            /**@type {boolean}*/
            this.locked = config.locked || false;
            /**@type {string}*/
            this.sort = config.sort || "name";
        }
    }
    export class ChartData {
        constructor(chartData) {
            /**@type {!number}*/
            this.index = chartData.index;
            /**@type {!number}*/
            this.side = chartData.side;
            /**@type {!number}*/
            this.kind = chartData.kind;
            /**@type {!number}*/
            this.dif = chartData.dif;
            /**@type {!string}*/
            this.name = chartData.name;
            /**@type {{main:!number, sub: number[]}}*/
            this.bpm = chartData.bpm;
            /**@type {number|null}*/
            this.highScore = chartData.highScore;
            /**@type {!boolean}*/
            this.isCleared = chartData.isCleared;
            /**@type {!boolean}*/
            this.isDeleted = chartData.isDeleted;
            /**@type {!boolean}*/
            this.isUnlocked = chartData.isUnlocked;
            /**@type {?{y:number, m:number, d: number}}*/
            this.clearDay = chartData.clearDay;
            /**@type {!string[]}*/
            this.alias = chartData.alias;
            /**@type {!string[]}*/
            this.note = chartData.note;
        }
    }
</script>
