<script>
    import { Config } from "../arith/Classes.svelte";
    import ConfigHeader from "../layout/ConfigHeader.svelte";
    import ConfigToggle from "../layout/ConfigToggle.svelte";
    import Drawer from "../layout/Drawer.svelte";
    import Select from "../layout/Select.svelte";

    /** @type {Config}*/
    export let config;
</script>

<Drawer>
    <svelte:fragment slot="content">
        <slot />
    </svelte:fragment>
    <svelte:fragment slot="drawer">
        <ConfigHeader>FILTER</ConfigHeader>
        <ConfigToggle bind:checked={config.cleared}>cleared</ConfigToggle>
        <ConfigToggle bind:checked={config.failed}>failed</ConfigToggle>
        <ConfigToggle bind:checked={config.notPlayed}>not played</ConfigToggle>
        <ConfigToggle bind:checked={config.playable}>available</ConfigToggle>
        <ConfigToggle bind:checked={config.deleted}>deleted</ConfigToggle>
        <ConfigToggle bind:checked={config.locked}>locked</ConfigToggle>
        <ConfigHeader>SORT</ConfigHeader>
        <Select bind:value={config.sort} options={{ name: "曲名", score: "スコア", date: "日付" }} />
    </svelte:fragment>
</Drawer>
