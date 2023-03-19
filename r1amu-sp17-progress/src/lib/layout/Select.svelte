<script>
    import SelectBordered from "../cell/SelectBordered.svelte";

    export let value;
    export let options;
</script>

<SelectBordered bind:value class="">
    <option disabled value={undefined}>---選択---</option>
    {#each Object.entries(options) as [k, v]}
        <option value={k}>{v}</option>
    {/each}
</SelectBordered>
