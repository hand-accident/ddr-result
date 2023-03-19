<script>
    export let checked, id;
    let className;
    export { className as class };
</script>

<input {id} type="checkbox" class="c {className}" bind:checked />

<style lang="postcss" module>
    .c {
        /* drawer-toggle*/
        @apply absolute h-0 w-0 appearance-none opacity-0;
    }
</style>
