<script>
    import Header from "../layout/Header.svelte";
    export let date;
</script>

<Header>
    <svelte:fragment slot="title">SP17進捗</svelte:fragment>
    <svelte:fragment slot="update">update: {date}</svelte:fragment>
    <slot />
</Header>
